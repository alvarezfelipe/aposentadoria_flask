from flask import Flask, render_template, request
import funcoes
import regras_aposentadoria
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_data', methods=['POST'])
def send_data():    
    try:
        # 1. Coleta e Conversão de Dados
        nome = request.form.get('nome-interessado', 'Não informado')
        sexo = request.form.get('radio_sexo', 'masculino').lower()
        cargo = request.form.get('radio_cargo', 'outros').lower()
        
        data_nascimento = funcoes.txt_to_date(request.form.get('data-nascimento'))
        data_exercicio = funcoes.txt_to_date(request.form.get('data-exercicio'))
        data_pri_emprego = funcoes.txt_to_date(request.form.get('data-pri-emprego'))
        data_fechamento = funcoes.txt_to_date(request.form.get('data-fechamento'))
        
        # Tempos adicionais (em dias)
        try:
            oab = int(request.form.get('tempo-oab', 0)) if cargo == 'procurador' else 0
            inss = int(request.form.get('tempo-inss', 0))
            outros = int(request.form.get('tempo-outros', 0))
        except ValueError:
            oab = inss = outros = 0

        # 2. Processar ausências descontáveis
        ausencias_json = request.form.get('ausencias-json', '[]')
        try:
            ausencias = json.loads(ausencias_json)
        except json.JSONDecodeError:
            ausencias = []
        
        # Calcular total de dias de ausência
        total_dias_ausencia = 0
        ausencias_detalhes = []
        for ausencia in ausencias:
            dias = ausencia.get('dias', 0)
            total_dias_ausencia += dias
            ausencias_detalhes.append({
                'tipo': ausencia.get('tipo', 'Ausência'),
                'data_inicio': ausencia.get('data_inicio'),
                'data_fim': ausencia.get('data_fim'),
                'dias': dias,
                'motivo': ausencia.get('motivo', '')
            })

        # 3. Cálculos de Base (com desconto de ausências)
        idade = funcoes.calc_idade(data_nascimento, data_fechamento)
        # Subtrair dias de ausência do tempo total de contribuição
        t_contribuicao = funcoes.tempo_contrib(data_pri_emprego, data_fechamento, oab, inss, outros) - total_dias_ausencia
        t_servico_pub = funcoes.tempo_efetivo_total(data_exercicio, data_fechamento)
        t_cargo = funcoes.tempo_cargo(data_exercicio, data_fechamento, cargo, oab)

        # 4. Verificação de Regras (Status Atual)
        regras_status = [
            regras_aposentadoria.regra_permanente(sexo, idade, t_contribuicao, t_servico_pub, t_cargo),
            regras_aposentadoria.transicao_1(sexo, idade, data_exercicio, t_contribuicao, t_servico_pub, t_cargo),
            regras_aposentadoria.transicao_pontos(sexo, idade, t_contribuicao, t_servico_pub, t_cargo, data_fechamento)
        ]

        # 5. Previsões Futuras
        previsoes_lista = [
            regras_aposentadoria.previsao_regra_permanente(sexo, data_nascimento, cargo, data_pri_emprego, data_exercicio, inss, outros, oab, data_fechamento, total_dias_ausencia),
            regras_aposentadoria.previsao_transicao_pedagio(sexo, data_nascimento, cargo, data_pri_emprego, data_exercicio, inss, outros, oab, data_fechamento, total_dias_ausencia)
        ]
        
        # Formatar previsões para exibição (achatar listas em strings)
        previsoes_formatadas = [" | ".join(p) for p in previsoes_lista]

        return render_template('exibicao.html', 
                               nome=nome,
                               sexo=sexo.capitalize(),
                               idade=idade,
                               cargo=cargo.capitalize(),
                               exercicio=funcoes.format_date(data_exercicio),
                               nivel=funcoes.format_date(data_exercicio),
                               primeiro_emprego=funcoes.format_date(data_pri_emprego),
                               inss=inss,
                               outros=outros + oab,
                               fechamento=funcoes.format_date(data_fechamento),
                               tempo_cargo=funcoes.dias_para_extenso(t_cargo),
                               tempo_contribuicao=t_contribuicao,
                               previsoes=previsoes_formatadas,
                               regras=regras_status,
                               len_previsoes=len(previsoes_formatadas),
                               len_regras=len(regras_status),
                               ausencias=ausencias_detalhes,
                               total_dias_ausencia=total_dias_ausencia)
                               
    except Exception as e:
        return f"Erro ao processar dados: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

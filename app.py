from flask import Flask, render_template, request
import funcoes
import regras_aposentadoria

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_data', methods = ['POST'])
def send_data():    
    #Obtendo dados do formulário
    nome = request.form['nome-interessado']
    sexo = request.form['radio_sexo'].lower()
    data_nascimento = funcoes.txt_to_date(request.form['data-nascimento'])
    idade = funcoes.calc_idade(data_nascimento)    
    cargo = request.form['radio_cargo'].lower()
    exercicio = funcoes.txt_to_date(request.form['data-exercicio'])    

    if cargo == 'outros':                
        nivel = exercicio
    else:
        nivel = funcoes.txt_to_date(request.form['data-nivel'])

    primeiro_emprego = funcoes.txt_to_date(request.form['data-pri-emprego'])

    if cargo == 'procurador':
        oab = int(request.form['tempo-oab'])
    else:
        oab = 0
    
    inss = int(request.form['tempo-inss'])
    outros = int(request.form['tempo-outros']) + oab    
    fechamento = funcoes.txt_to_date(request.form['data-fechamento'])

    #Aplicando funções auxiliares
    cinco_anos = funcoes.cinco_anos(exercicio)
    dez_anos = funcoes.dez_anos(exercicio)
    vinte_anos = funcoes.vinte_anos(exercicio)
    tempo_contribuicao = funcoes.tempo_contrib(exercicio,fechamento,oab,inss,outros)
    tempo_cargo = funcoes.tempo_cargo(exercicio,fechamento,cargo,oab,outros)
    tempo_efetivo = funcoes.tempo_efetivo_total(exercicio,fechamento)

    #Aplicando regras aposentadoria
    def aplica_regras():
        a = regras_aposentadoria.regra_permanente(sexo,idade,tempo_contribuicao,tempo_efetivo, tempo_cargo)
        b = regras_aposentadoria.transicao_1(sexo, idade, exercicio, tempo_contribuicao, tempo_efetivo, tempo_cargo)
        # regras_aposentadoria.transicao_2(sexo, idade, exercicio, tempo_contribuicao, tempo_efetivo, tempo_cargo)        
        d = regras_aposentadoria.transicao_4(sexo, exercicio, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo, primeiro_emprego,cargo,oab)
        return (a,b,d)
    regras = aplica_regras()

    #Aplicando previsão para aposentadoria
    def previsao():
        a = regras_aposentadoria.previsao_regra_permanente(sexo,data_nascimento,cargo,primeiro_emprego,exercicio,inss,outros,oab,fechamento)
        b = regras_aposentadoria.previsao_regra_transicao1(sexo,data_nascimento,cargo,primeiro_emprego,exercicio,inss,outros,oab,fechamento)        
        d = regras_aposentadoria.previsao_regra_transicao4(sexo,data_nascimento,cargo,primeiro_emprego,exercicio,inss,outros,oab,fechamento)
        return (a,b,d)

    previsoes = previsao()
    return render_template('previsao.html', 
                           nome=nome,
                           sexo=sexo,
                           idade=idade,
                           cargo=cargo,
                           exercicio=exercicio,
                           nivel=nivel,
                           primeiro_emprego=primeiro_emprego,
                           oab=oab,
                           inss=inss,
                           outros=outros,
                           fechamento=fechamento,
                           cinco_anos=cinco_anos,
                           dez_anos=dez_anos,
                           vinte_anos=vinte_anos,
                           tempo_contribuicao=tempo_contribuicao,
                           tempo_cargo=tempo_cargo,
                           previsoes=previsoes,
                           regras=regras,
                           len_previsoes=len(previsoes),
                           len_regras=len(regras)
                           )

app.run(debug=True)
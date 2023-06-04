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
    sexo = request.form['radio_sexo']
    idade = funcoes.calc_idade(funcoes.txt_to_date(request.form['data-nascimento']))
    cargo = request.form['radio_cargo']
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
        regras_aposentadoria.regra_permanente(sexo,idade,tempo_contribuicao,tempo_efetivo, tempo_cargo)
        # regras_aposentadoria.transicao_1(sexo, idade, exercicio, tempo_contribuicao, tempo_efetivo, tempo_cargo)
        # regras_aposentadoria.transicao_2(sexo, idade, exercicio, tempo_contribuicao, tempo_efetivo, tempo_cargo)
        # regras_aposentadoria.transicao_3(sexo, exercicio, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo, primeiro_emprego)
        # regras_aposentadoria.transicao_4(sexo, idade, exercicio, tempo_contribuicao, tempo_efetivo, tempo_cargo, primeiro_emprego)

    regras = aplica_regras()
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
                           regras=regras,
                           )

app.run(debug=True)
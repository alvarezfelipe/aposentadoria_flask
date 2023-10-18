from datetime import *

def txt_to_date(a):
    b = datetime.strptime(a, '%Y-%m-%d')
    return b

def calc_idade(nascimento):
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

#Tempos de efetivo exercício
def cinco_anos(exercicio):
    return exercicio + timedelta(days=1825)

def dez_anos(exercicio):
    return exercicio + timedelta(days=3650)

def vinte_anos(exercicio):
    return exercicio + timedelta(days=7300)

def tempo_efetivo_total(exercicio, final):
    return abs((final - exercicio).days)+1

#Tempo total de contribuição
def tempo_contrib(inicio,fim,oab,inss,outro):
    outros = oab+inss+outro
    qtde_dias = abs((fim - inicio).days)+1
    return qtde_dias + outros

#Tempo no cargo
def tempo_cargo(inicio,fim,cargo,oab,outro):
    data_reforma = datetime.strptime('16/12/1998', '%d/%m/%Y')
    data_cargo = inicio
    # nivel = ''
    if cargo == 'procurador' and inicio <= data_reforma:
        # data_cargo = nivel
        tempo = (abs((fim - data_cargo).days)+1) + oab
        return tempo
    elif cargo == 'engenheiro':
        # data_cargo = nivel
        tempo = (abs((fim - data_cargo).days)+1)
        return tempo
    else:
        tempo = (abs((fim - data_cargo).days)+1)
        return tempo
    
#Cálculo para o pedágio da contribuição
def calc_pedagio(primeiro_emprego, sexo, cargo, oab):
    
    fim_conta = datetime.strptime('07/03/2020', '%d/%m/%Y') #data da reforma, que fixou parâmetro do pedágio
    data_pedagio = '' #data em que se completará o pedágio
    confere_pedagio = ''

    if cargo == 'procurador':
        total_pedagio = abs((fim_conta - primeiro_emprego).days) + oab #total de contribuição até 07/03/2020
    else:
        total_pedagio = abs((fim_conta - primeiro_emprego).days) #total de contribuição até 07/03/2020
    falta_pedagio = ''

    if sexo == 'feminino':
        if total_pedagio >= 10950:
            print('Não há pedágio a ser pago.')
            print('Completou a contribuição necessária até 07/03/2020.')
            confere_pedagio = 'Não há pedágio a ser pago. Completou a contribuição necessária até 07/03/2020.'
        else:
            falta_pedagio = 10950 - total_pedagio - 1
            data_pedagio = primeiro_emprego + timedelta(days=10950) + timedelta(days=falta_pedagio)
            print('Completará a contribuição necessário e o pedágio em: ' + datetime.strftime(data_pedagio, '%d/%m/%Y'))
            confere_pedagio = f"Completará a contribuição necessário e o pedágio em: {datetime.strftime(data_pedagio, '%d/%m/%Y')}"
    elif sexo == 'masculino':
        if total_pedagio >= 12775:
            print('Não há pedágio a ser pago.')
            print('Completou a contribuição necessária até 07/03/2020.')
            confere_pedagio = 'Não há pedágio a ser pago. Completou a contribuição necessária até 07/03/2020.'
        else:
            falta_pedagio = 12775 - total_pedagio - 1
            data_pedagio = primeiro_emprego + timedelta(days=12775) + timedelta(days=falta_pedagio)
            # return print('Completará a contribuição necessário e o pedágio em: ' + datetime.strftime(data_pedagio, '%d/%m/%Y'))
            confere_pedagio = f"Completará a contribuição necessário e o pedágio em: {datetime.strftime(data_pedagio, '%d/%m/%Y')}"
    else:
        confere_pedagio = 'Dados inválidos para o cálculo do pedágio. Revise.'
    return confere_pedagio
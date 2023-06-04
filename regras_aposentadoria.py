from datetime import datetime
from funcoes import *

completou_regra = True
regra = ''

'''
    medidas de tempo de serviço/contribuição:
    12775 = 35 anos
    10950 = 30 anos
    9125 = 25 anos
    7300 = 20 anos
    3650 = 10 anos
    1825 = 05 anos
'''

#Regra Permanente para aposentadoria
def regra_permanente(sexo, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo):
    #contribuição, efetivo e cargo são todos em dias
    if sexo == 'feminino':
        if idade>=62 and tempo_contribuicao>=9125 and tempo_efetivo>=3650 and tempo_cargo>=1825:
            completou_regra = True
            print('Completou todos os requisitos aposentar pela REGRA PERMANENTE, com fundamento no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20')
            regra = 'Completou todos os requisitos aposentar pela REGRA PERMANENTE, com fundamento no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20'
        else:
            completou_regra = False
            print('Não completou os requisitos para aposentadoria na Regra Permanente')
            regra = 'Não completou os requisitos para aposentadoria na Regra Permanente'
            print('---------------------------------------')
    elif (sexo == 'masculino'):
        if(idade >=65 and tempo_contribuicao >=9125 and tempo_efetivo >=3650 and tempo_cargo >=1825):
            completou_regra = True
            print('Completou todos os requisitos aposentar pela REGRA PERMANENTE, com fundamento no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20')
            regra = 'Completou todos os requisitos aposentar pela REGRA PERMANENTE, com fundamento no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20'
            print('---------------------------------------')
        else: 
            completou_regra = False
            print('Não completou os requisitos para aposentadoria na Regra Permanente')
            regra = 'Não completou os requisitos para aposentadoria na Regra Permanente'
            print('---------------------------------------')
    else: 
        completou_regra = False
        print('Dados inválidos')
        regra = 'Dados inválidos'
    return regra

#A Transição 1 tem como principais parâmetros a idade mínima do funcionário e 
# a data de admissão ser até 31/12/2003
#garante ao servidor integralidade e paridade
def transicao_1(sexo, idade, admissao, tempo_contribuicao, tempo_efetivo, tempo_cargo):
    data_transicao1 = datetime.strptime('31/12/2003', '%d/%m/%Y')
    if admissao <= data_transicao1:
        if sexo == 'feminino':
            if idade>=62 and tempo_contribuicao>=10950 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 1, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, II, III, IV, §§ 6º, ítem 1, alínea "a", e 7º, ítem 1 da LCE n. 1.354/20')
                print('---------------------------------------')
            else:
                completou_regra = False
                print('Não completou os requisitos para aposentadoria na Regra de Transição 1')
                print('---------------------------------------')
        elif sexo == 'masculino':
            if idade>=65 and tempo_contribuicao>=12775 and tempo_cargo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 1, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, II, III, IV, §§ 6º, ítem 1, alínea "a", e 7º, ítem 1 da LCE n. 1.354/20')
            else: 
                completou_regra = False 
                print('Não completou os requisitos para aposentadoria na Regra de Transição 1')  
                print('---------------------------------------')
        else:
            completou_regra = False
            print('Dados inválidos. Verifique e execute novamente.')
    else:
        completou_regra = False
        print('Regra de Transição 1 não se aplica ao caso.')
    return completou_regra

#A Transição 2 tem como principais parâmetros a idade mínima do funcionário e 
# a data de admissão ser até 07/03/2020 (data da reforma previdenciária)
#garante, no mínimo, 60% da média dos salários
#somar contribuicao com idade e totalizar pontos
def transicao_2(sexo, admissao, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo):
    pass
    #essa regra precisa aumentar ano a ano
    #desenvolver depois

#Regra de Transição 3
# tem como parâmetro o pedágio de 100% do tempo que faltava até 07/03/2020
# Deve verificar se a data de admissão for até 31/12/2003 para garantir integralidade e paridade
def transicao_3(sexo, admissao, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo, primeiro_emprego, cargo, oab):
    data_transicao3 = datetime.strptime('31/12/2003', '%d/%m/%Y')
    if admissao <= data_transicao3:
        if sexo == 'feminino':
            if idade>=57 and tempo_contribuicao>=10950 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 3, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20')
                print('---------------------------------------')
            else:
                print('Não completou os requisitos para aposentadoria pela Regra de Transição 3')

                completou_regra = False
        elif sexo == 'masculino':
            if idade>=60 and tempo_contribuicao>=12775 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 3, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20')
                print('---------------------------------------')
            else: 
                print('Não completou os requisitos para aposentadoria na Regra de Transição 3')
                
                completou_regra = False
        else:
            completou_regra = False
            print('Dados inválidos. Verifique e execute novamente.')
    else:
        completou_regra = False
        print('Regra de Transição 3 não se aplica ao caso.')
    return completou_regra

#A Transição 4 tem como parâmetro o pedágio de 100% do tempo que faltava até 07/03/2020
#Deve verificar se a data de admissão for até 07/03/2020 para garantir 100% da média dos salários
def transicao_4(sexo, admissao, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo, primeiro_emprego,cargo,oab):
    data_transicao = datetime.strptime('07/03/2020', '%d/%m/%Y')

    if admissao <= data_transicao:
        if sexo == 'feminino':
            if idade>=57 and tempo_contribuicao>=10950 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 4, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 11, I, II, III, IV, V, §§ 2º, ítem 2 e 3º, ítem 2 da LCE n. 1.354/20')
                print('---------------------------------------')
            else:
                print('Não completou os requisitos para aposentadoria pela Regra de Transição 4')
                
                completou_regra = False
        elif sexo == 'masculino':
            if idade>=60 and tempo_contribuicao>=12775 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 4, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 11, I, II, III, IV, V, §§ 2º, ítem 2 e 3º, ítem 2 da LCE n. 1.354/20')
                print('---------------------------------------')
            else:
                print('Não completou os requisitos para aposentadoria pela Regra de Transição 4')
                
                completou_regra = False
        else:
            completou_regra = False
            print('Dados inválidos. Verifique e execute novamente.')
    else:
        completou_regra = False
        print('Regra de Transição 4 não se aplica ao caso.')
    return completou_regra

#Previsões de aposentadoria nas regras da Reforma 2019
def previsao_regra_permanente(sexo, nascimento, cargo, inicio_contribuicao, inicio_exercicio, tempo_inss, tempo_outros, tempo_oab):
  tempo_trabalho = inicio_contribuicao
  if cargo == 'procurador' and inicio_exercicio <= datetime.strptime('16/12/1998', '%d/%m/%Y'):
    outros = tempo_inss + tempo_outros + tempo_oab 
  else:
    outros = tempo_inss + tempo_outros
  
  if sexo == 'feminino':
      completa_idade = f"Completará 62 anos em: {nascimento.day}/{nascimento.month}/{nascimento.year + 62}"
      completa_contribuicao = (tempo_trabalho - timedelta(outros)) + timedelta(days=9125)
      completa_efetivo_exercicio = inicio_exercicio + timedelta(days=3650)
      completa_nivel = inicio_exercicio + timedelta(days=1825)
      print(completa_idade)
      print(completa_contribuicao)
      print(completa_efetivo_exercicio)
      print(completa_nivel)

  elif sexo == 'masculino':
      completa_idade = f"Completará 65 anos em: {nascimento.day}/{nascimento.month}/{nascimento.year + 65}"
      completa_contribuicao = (tempo_trabalho - timedelta(outros)) + timedelta(days=9125)
      completa_efetivo_exercicio = inicio_exercicio + timedelta(days=3650)
      completa_nivel = inicio_exercicio + timedelta(days=1825)
      print(completa_idade)
      print(completa_contribuicao)
      print(completa_efetivo_exercicio)
      print(completa_nivel)
  else:
    print('Dados incorretos. Revise as informações')

def previsao_regra_transicao1(sexo, nascimento, cargo, inicio_contribuicao, inicio_exercicio, tempo_inss, tempo_outros, tempo_oab):
    tempo_trabalho = inicio_contribuicao
    data_transicao1 = datetime.strptime('31/12/2003', '%d/%m/%Y')

    if cargo == 'procurador' and inicio_exercicio <= datetime.strptime('16/12/1998', '%d/%m/%Y'):
        outros = tempo_inss + tempo_outros + tempo_oab 
    else:
        outros = tempo_inss + tempo_outros
  
    if inicio_exercicio <= data_transicao1:
        if sexo == 'feminino':
            completa_idade = f"Completará 62 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 62}"
            completa_contribuicao = f"Completará 30 anos de contribuição em: {datetime.strftime((tempo_trabalho - timedelta(outros)) + timedelta(days=10950),'%d/%m/%Y')}"
            completa_efetivo_exercicio = f"Completará 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"
            print(completa_idade)
            print(completa_contribuicao)
            print(completa_efetivo_exercicio)
            print(completa_nivel)

        elif sexo == 'masculino':
            completa_idade = f"Completará 65 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 65}"
            completa_contribuicao = f"Completará 35 anos de contribuição em: {datetime.strftime((tempo_trabalho - timedelta(outros)) + timedelta(days=12775),'%d/%m/%Y')}"
            completa_efetivo_exercicio = f"Completará 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"
            print(completa_idade)
            print(completa_contribuicao)
            print(completa_efetivo_exercicio)
            print(completa_nivel)
        else:
            print('Dados incorretos. Revise as informações')
    else:
        print('Regra de transição 1 não se aplica ao caso.')

def previsao_regra_transicao2():
    pass

def previsao_regra_transicao3(sexo, nascimento, cargo, inicio_contribuicao, inicio_exercicio, tempo_inss, tempo_outros, tempo_oab):
    
    data_transicao = datetime.strptime('31/12/2003', '%d/%m/%Y')    
  
    if inicio_exercicio <= data_transicao:
        if sexo == 'feminino':
            completa_idade = f"Completará 57 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 57}"
            completa_contribuicao = calc_pedagio(inicio_contribuicao, sexo, cargo, tempo_oab)
            completa_efetivo_exercicio = f"Completará 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"
            print(completa_idade)
            print(completa_contribuicao)
            print(completa_efetivo_exercicio)
            print(completa_nivel)

        elif sexo == 'masculino':
            completa_idade = f"Completará 60 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 60}"
            completa_contribuicao = calc_pedagio(inicio_contribuicao, sexo, cargo, tempo_oab)
            completa_efetivo_exercicio = f"Completará 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"
            print(completa_idade)
            print(completa_contribuicao)
            print(completa_efetivo_exercicio)
            print(completa_nivel)
        else:
            print('Dados incorretos. Revise as informações')
    else:
        print('Regra de transição 3 não se aplica ao caso.')

def previsao_regra_transicao4(sexo, nascimento, cargo, inicio_contribuicao, inicio_exercicio, tempo_inss, tempo_outros, tempo_oab):
    
    data_transicao = datetime.strptime('07/03/2020', '%d/%m/%Y')    
  
    if inicio_exercicio <= data_transicao:
        if sexo == 'feminino':
            completa_idade = f"Completará 57 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 57}"
            completa_contribuicao = calc_pedagio(inicio_contribuicao, sexo, cargo, tempo_oab)
            completa_efetivo_exercicio = f"Completará 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"
            print(completa_idade)
            print(completa_contribuicao)
            print(completa_efetivo_exercicio)
            print(completa_nivel)

        elif sexo == 'masculino':
            completa_idade = f"Completará 60 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 60}"
            completa_contribuicao = calc_pedagio(inicio_contribuicao, sexo, cargo, tempo_oab)
            completa_efetivo_exercicio = f"Completará 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"
            print(completa_idade)
            print(completa_contribuicao)
            print(completa_efetivo_exercicio)
            print(completa_nivel)
        else:
            print('Dados incorretos. Revise as informações')
    else:
        print('Regra de transição 4 não se aplica ao caso.')
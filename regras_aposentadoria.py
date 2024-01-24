from datetime import datetime
from funcoes import *

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
            regra = 'Completou todos os requisitos aposentar pela REGRA PERMANENTE, com fundamento no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20'
        else:            
            regra = 'Não completou os requisitos para aposentadoria na Regra Permanente'            
    elif (sexo == 'masculino'):
        if(idade >=65 and tempo_contribuicao >=9125 and tempo_efetivo >=3650 and tempo_cargo >=1825):                        
            regra = 'Completou todos os requisitos aposentar pela REGRA PERMANENTE, com fundamento no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20'            
        else:                         
            regra = "Não completou os requisitos para aposentadoria na Regra Permanente"            
    else:                 
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
                regra = 'Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 1, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, II, III, IV, §§ 6º, ítem 1, alínea "a", e 7º, ítem 1 da LCE n. 1.354/20'                
            else:                
                regra = 'Não completou os requisitos para aposentadoria na Regra de Transição 1'
                
        elif sexo == 'masculino':
            if idade>=65 and tempo_contribuicao>=12775 and tempo_cargo>=7300 and tempo_cargo>=1825:                
                regra = 'Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 1, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, II, III, IV, §§ 6º, ítem 1, alínea "a", e 7º, ítem 1 da LCE n. 1.354/20'
            else:                 
                regra = 'Não completou os requisitos para aposentadoria na Regra de Transição 1'
                
        else:
            regra = 'Dados inválidos. Verifique e execute novamente.'
    else:
        regra = 'Regra de Transição 1 não se aplica ao caso.'
    return regra

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
                regra = 'Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 3, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20'                
            else:
                regra = 'Não completou os requisitos para aposentadoria pela Regra de Transição 3'
        elif sexo == 'masculino':
            if idade>=60 and tempo_contribuicao>=12775 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                regra = 'Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 3, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20'
                
            else: 
                regra = 'Não completou os requisitos para aposentadoria na Regra de Transição 3'
        else:            
            regra = 'Dados inválidos. Verifique e execute novamente.'
    else:
        regra = 'Regra de Transição 3 não se aplica ao caso.'
    return regra

#A Transição 4 tem como parâmetro o pedágio de 100% do tempo que faltava até 07/03/2020
#Deve verificar se a data de admissão for até 07/03/2020 para garantir 100% da média dos salários
def transicao_4(sexo, admissao, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo, primeiro_emprego,cargo,oab) -> str:
    data_transicao = datetime.strptime('07/03/2020', '%d/%m/%Y')

    if admissao <= data_transicao:
        if sexo == 'feminino':
            if idade>=57 and tempo_contribuicao>=10950 and tempo_efetivo>=7300 and tempo_cargo>=1825:                
                regra = 'Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 4, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 11, I, II, III, IV, V, §§ 2º, ítem 2 e 3º, ítem 2 da LCE n. 1.354/20'
            else:
                regra = 'Não completou os requisitos para aposentadoria pela Regra de Transição 4'
        elif sexo == 'masculino':
            if idade>=60 and tempo_contribuicao>=12775 and tempo_efetivo>=7300 and tempo_cargo>=1825:                
                regra = 'Completou todos os requisitos aposentar na REGRA DE TRANSIÇÃO 4, com fundamento no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 11, I, II, III, IV, V, §§ 2º, ítem 2 e 3º, ítem 2 da LCE n. 1.354/20'
            else:
                regra = 'Não completou os requisitos para aposentadoria pela Regra de Transição 4'
        else:            
            regra = 'Dados inválidos. Verifique e execute novamente.'
    else:        
        regra = 'Regra de Transição 4 não se aplica ao caso.'
    return regra

#Previsões de aposentadoria nas regras da Reforma 2019
previsao = ''
nome_regra = ''
def previsao_regra_permanente(sexo, nascimento, cargo, inicio_contribuicao, inicio_exercicio, tempo_inss, tempo_outros, tempo_oab,fechamento):
  tempo_trabalho = inicio_contribuicao
  if cargo == 'procurador' and inicio_exercicio <= datetime.strptime('16/12/1998', '%d/%m/%Y'):
    outros = tempo_inss + tempo_outros + tempo_oab 
  else:
    outros = tempo_inss + tempo_outros

  nome_regra = 'Previsão para cumprir Regra Permanente - Art. 2º, LC 1354/2020'
  
  if sexo == 'feminino':
      completa_idade = f"Completará 65 anos em: {nascimento.day}/{nascimento.month}/{nascimento.year + 65}"
      completa_contribuicao = f"Completou/Completará 25 anos de contribuição em: {datetime.strftime(tempo_trabalho  + timedelta(days=9125), '%d/%m/%Y')}."
      completa_efetivo_exercicio = f"Completará 10 anos de exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=3650), '%d/%m/%Y')}."
      completa_nivel = f"Completará 5 anos no cargo em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}."

      previsao = (nome_regra, completa_idade, completa_contribuicao, completa_efetivo_exercicio, completa_nivel)

  elif sexo == 'masculino':
      completa_idade = f"Completará 65 anos em: {nascimento.day}/{nascimento.month}/{nascimento.year + 65}"
      completa_contribuicao = f"Completará 25 anos de contribuição em: {datetime.strftime((tempo_trabalho - timedelta(outros)) + timedelta(days=9125), '%d/%m/%Y')}."
      completa_efetivo_exercicio = f"Completará 10 anos de exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=3650), '%d/%m/%Y')}."
      completa_nivel = f"Completará 5 anos no cargo em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}."

      previsao = (nome_regra,completa_idade, completa_contribuicao, completa_efetivo_exercicio, completa_nivel)
  else:
    previsao = 'Dados incorretos. Revise as informações'
  return previsao

def previsao_regra_transicao1(sexo, nascimento, cargo, inicio_contribuicao, inicio_exercicio, tempo_inss, tempo_outros, tempo_oab, fechamento):
    tempo_trabalho = inicio_contribuicao
    data_transicao1 = datetime.strptime('31/12/2003', '%d/%m/%Y')

    nome_regra = "Previsão para cumprir Regra de Transição 1"

    if cargo == 'procurador' and inicio_exercicio <= datetime.strptime('16/12/1998', '%d/%m/%Y'):
        outros = tempo_inss + tempo_outros + tempo_oab 
    else:
        outros = tempo_inss + tempo_outros
  
    if inicio_exercicio <= data_transicao1:
        if sexo == 'feminino':
            completa_idade = f"Completará/Completou 62 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 62}"
            completa_contribuicao = f"Completará/Completou 30 anos de contribuição em: {datetime.strftime((tempo_trabalho - timedelta(outros)) + timedelta(days=10950),'%d/%m/%Y')}"
            completa_efetivo_exercicio = f"Completará/Completou 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará/Completou 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"

            previsao = (completa_idade, completa_contribuicao, completa_efetivo_exercicio, completa_nivel)


        elif sexo == 'masculino':
            completa_idade = f"Completará/Completou 65 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 65}"
            completa_contribuicao = f"Completará/Completou 35 anos de contribuição em: {datetime.strftime((tempo_trabalho - timedelta(outros)) + timedelta(days=12775),'%d/%m/%Y')}"
            completa_efetivo_exercicio = f"Completará/Completou 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará/Completou 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"

            previsao = (nome_regra, completa_idade, completa_contribuicao, completa_efetivo_exercicio, completa_nivel)


        else:
            previsao = 'Dados incorretos. Revise as informações'
    else:
        previsao = 'Regra de transição 1 não se aplica ao caso.'
    
    return previsao

#Regra de transição pela regra dos pontos
def previsao_regra_transicao2(sexo, nascimento, cargo, inicio_contribuicao, inicio_exercicio, tempo_inss, tempo_outros, tempo_oab,fechamento):
    
    data_transicao = datetime.strptime('07/03/2020', '%d/%m/%Y') 
    data_proventos = datetime.strptime('31/12/2003', '%d/%m/%Y')

    nome_regra = "Previsão para cumprir Regra de Transição - Art. 10, LC 1354/2020"

    if inicio_exercicio <= data_transicao:
        if sexo == 'feminino':
            completa_idade = f"Completará/Completou 57 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 57}"
            completa_efetivo_exercicio = f"Completará/Completou 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará/Completou 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"


#Regra de transição pela regra do pedágio
def previsao_regra_transicao4(sexo, nascimento, cargo, inicio_contribuicao, inicio_exercicio, tempo_inss, tempo_outros, tempo_oab,fechamento):
    
    data_transicao = datetime.strptime('07/03/2020', '%d/%m/%Y') 
    data_proventos = datetime.strptime('31/12/2003', '%d/%m/%Y') 

    nome_regra = "Previsão para cumprir Regra de Transição - Art. 11, LC 1354/2020"   
  
    if inicio_exercicio <= data_transicao:
        if sexo == 'feminino':
            completa_idade = f"Completará/Completou 57 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 57}"
            completa_contribuicao = calc_pedagio(inicio_contribuicao, sexo, cargo, tempo_oab)
            completa_efetivo_exercicio = f"Completará/Completou 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará/Completou 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"

            #Verifica proventos integrais ou não
            if inicio_exercicio <= data_proventos:
                proventos = 'Terá direito a proventos integrais e paridade'
            else:
                proventos = 'Proventos de acordo com média.'
            
            previsao = (nome_regra, completa_idade, completa_contribuicao, completa_efetivo_exercicio, completa_nivel, proventos)

        elif sexo == 'masculino':
            completa_idade = f"Completará/Completou 60 anos de idade em: {nascimento.day}/{nascimento.month}/{nascimento.year + 60}"
            completa_contribuicao = calc_pedagio(inicio_contribuicao, sexo, cargo, tempo_oab)
            completa_efetivo_exercicio = f"Completará/Completou 20 anos de efetivo exercício em: {datetime.strftime(inicio_exercicio + timedelta(days=7300), '%d/%m/%Y')}"
            completa_nivel = f"Completará/Completou 5 anos no cargo/nível em: {datetime.strftime(inicio_exercicio + timedelta(days=1825), '%d/%m/%Y')}"
            
            #Verifica proventos integrais ou não
            if inicio_exercicio <= data_proventos:
                proventos = 'Terá direito a proventos integrais e paridade'
            else:
                proventos = 'Proventos de acordo com média.'

            previsao = (nome_regra, completa_idade, completa_contribuicao, completa_efetivo_exercicio, completa_nivel, proventos)
        else:
            previsao = 'Dados incorretos. Revise as informações'
    else:
        previsao = 'Regra de transição do Art. 11 não se aplica ao caso.'
    return previsao
from datetime import datetime
from funcoes import *

completou_regra = True
regra = ''

#Regra Permanente para aposentadoria
def regra_permanente(sexo, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo):
    #contribuição, efetivo e cargo são todos em dias
    if sexo == 'Feminino':
        if idade>=62 and tempo_contribuicao>=9125 and tempo_efetivo>=3650 and tempo_cargo>=1825:
            completou_regra = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20')
            regra = 'Completou todos os requisitos aposentar no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20'
        else:
            completou_regra = False
            print('Não completou os requisitos para aposentadoria na Regra Permanente')
            regra = 'Não completou os requisitos para aposentadoria na Regra Permanente'
            print('---------------------------------------')
    elif (sexo == 'Masculino'):
        if(idade >=65 and tempo_contribuicao >=9125 and tempo_efetivo >=3650 and tempo_cargo >=1825):
            completou_regra = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20')
            regras = 'Completou todos os requisitos aposentar no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20'
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
        if sexo == 'Feminino':
            if idade>=62 and tempo_contribuicao>=10950 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, II, III, IV, §§ 6º, ítem 1, alínea "a", e 7º, ítem 1 da LCE n. 1.354/20')
                print('---------------------------------------')
            else:
                completou_regra = False
                print('Não completou os requisitos para aposentadoria na Regra de Transição 1')
                print('---------------------------------------')
        elif sexo == 'Masculino':
            if idade>=65 and tempo_contribuicao>=12775 and tempo_cargo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, II, III, IV, §§ 6º, ítem 1, alínea "a", e 7º, ítem 1 da LCE n. 1.354/20')
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
    return ''
    #essa regra precisa aumentar ano a ano
    #desenvolver depois

#Regra de Transição 3
# tem como parâmetro o pedágio de 100% do tempo que faltava até 07/03/2020
# Deve verificar se a data de admissão for até 31/12/2003 para garantir integralidade e paridade
def transicao_3(sexo, admissao, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo, primeiro_emprego):
    data_transicao3 = datetime.strptime('31/12/2003', '%d/%m/%Y')
    if admissao <= data_transicao3:
        if sexo == 'Feminino':
            if idade>=57 and tempo_contribuicao>=10950 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20')
                print('---------------------------------------')
            else:
                print('Não completou os requisitos para aposentadoria pela Regra de Transição 3')

                #como não completou o requisito, calcula o pedágio e informa
                calc_pedagio(primeiro_emprego, sexo)
                print('---------------------------------------')
                completou_regra = False
        elif sexo == 'Masculino':
            if idade>=60 and tempo_contribuicao>=12775 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20')
                print('---------------------------------------')
            else: 
                print('Não completou os requisitos para aposentadoria na Regra de Transição 3')
                calc_pedagio(primeiro_emprego, sexo)
                print('---------------------------------------')
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
def transicao_4(sexo, idade, admissao, tempo_contribuicao, tempo_efetivo, tempo_cargo, primeiro_emprego):
    data_transicao = datetime.strptime('07/03/2020', '%d/%m/%Y')

    if admissao <= data_transicao:
        if sexo == 'Feminino':
            if idade>=57 and tempo_contribuicao>=10950 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 11, I, II, III, IV, V, §§ 2º, ítem 2 e 3º, ítem 2 da LCE n. 1.354/20')
                print('---------------------------------------')
            else:
                print('Não completou os requisitos para aposentadoria pela Regra de Transição 4')
                calc_pedagio(primeiro_emprego, sexo)
                print('---------------------------------------')
                completou_regra = False
        elif sexo == 'Masculino':
            if idade>=60 and tempo_contribuicao>=12775 and tempo_efetivo>=7300 and tempo_cargo>=1825:
                completou_regra = True
                print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 11, I, II, III, IV, V, §§ 2º, ítem 2 e 3º, ítem 2 da LCE n. 1.354/20')
                print('---------------------------------------')
            else:
                print('Não completou os requisitos para aposentadoria pela Regra de Transição 4')
                calc_pedagio(primeiro_emprego, sexo)
                print('---------------------------------------')
                completou_regra = False
        else:
            completou_regra = False
            print('Dados inválidos. Verifique e execute novamente.')
    else:
        completou_regra = False
        print('Regra de Transição 4 não se aplica ao caso.')
    return completou_regra
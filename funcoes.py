from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

def txt_to_date(a):
    if not a:
        return None
    try:
        return datetime.strptime(a, '%Y-%m-%d')
    except ValueError:
        return None

def calc_idade(nascimento, referencia=None):
    if not nascimento:
        return 0
    if referencia is None:
        referencia = date.today()
    elif isinstance(referencia, datetime):
        referencia = referencia.date()
        
    nasc_date = nascimento.date() if isinstance(nascimento, datetime) else nascimento
    
    idade = referencia.year - nasc_date.year - ((referencia.month, referencia.day) < (nasc_date.month, nasc_date.day))
    return idade

def format_date(dt):
    if not dt:
        return ""
    return dt.strftime('%d/%m/%Y')

# Tempos de efetivo exercício usando relativedelta para precisão calendária
def somar_anos(data_base, anos):
    if not data_base:
        return None
    return data_base + relativedelta(years=anos)

def cinco_anos(exercicio):
    return somar_anos(exercicio, 5)

def dez_anos(exercicio):
    return somar_anos(exercicio, 10)

def vinte_anos(exercicio):
    return somar_anos(exercicio, 20)

def tempo_efetivo_total(exercicio, final):
    if not exercicio or not final:
        return 0
    return abs((final - exercicio).days) + 1

def tempo_contrib(inicio, fim, oab=0, inss=0, outro=0):
    if not inicio or not fim:
        return 0
    qtde_dias = abs((fim - inicio).days) + 1
    return qtde_dias + oab + inss + outro

def tempo_cargo(inicio, fim, cargo, oab=0):
    if not inicio or not fim:
        return 0
    
    # Lógica simplificada: tempo desde o início do exercício até o fim
    # Se for procurador, soma o tempo de OAB conforme regra de direito adquirido
    dias_exercicio = abs((fim - inicio).days) + 1
    
    if cargo == 'procurador':
        data_reforma_98 = datetime(1998, 12, 16)
        if inicio <= data_reforma_98:
            return dias_exercicio + oab
            
    return dias_exercicio

def dias_para_extenso(total_dias):
    anos = total_dias // 365
    resto = total_dias % 365
    meses = resto // 30
    dias = resto % 30
    
    partes = []
    if anos > 0:
        partes.append(f"{anos} {'ano' if anos == 1 else 'anos'}")
    if meses > 0:
        partes.append(f"{meses} {'mês' if meses == 1 else 'meses'}")
    if dias > 0:
        partes.append(f"{dias} {'dia' if dias == 1 else 'dias'}")
        
    return ", ".join(partes) if partes else "0 dias"

def calc_pedagio_info(primeiro_emprego, sexo, cargo, oab, inss, outros):
    if not primeiro_emprego:
        return "Data de 1º emprego não informada."
        
    data_reforma_2020 = datetime(2020, 3, 7)
    tempo_ate_reforma = tempo_contrib(primeiro_emprego, data_reforma_2020, oab, inss, outros)
    
    meta_dias = 12775 if sexo == 'masculino' else 10950
    
    if tempo_ate_reforma >= meta_dias:
        return "Não há pedágio a ser pago. Requisito de tempo cumprido antes da reforma de 2020."
    
    falta_em_2020 = meta_dias - tempo_ate_reforma
    # Pedágio de 100% significa que ele precisa trabalhar o que faltava + o mesmo tanto de pedágio
    total_dias_necessarios = meta_dias + falta_em_2020
    
    data_conclusao = primeiro_emprego + timedelta(days=total_dias_necessarios)
    return f"Completará o tempo necessário + pedágio em: {format_date(data_conclusao)}"

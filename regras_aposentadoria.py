from datetime import datetime, timedelta
from funcoes import *

# Constantes de tempo em dias
DIAS_35_ANOS = 12775
DIAS_30_ANOS = 10950
DIAS_25_ANOS = 9125
DIAS_20_ANOS = 7300
DIAS_10_ANOS = 3650
DIAS_5_ANOS = 1825

def obter_tipo_provento(admissao, regra_tipo):
    """
    Define o tipo de provento com base na data de admissão e na regra.
    Regra 1 e 3 (Pedágio 100% para pré-2003): Integralidade e Paridade.
    Regra 4 (Pedágio 100% pós-2003): 100% da Média.
    Regra Permanente: 60% + 2% por ano que exceder 20 anos.
    """
    data_limite_paridade = datetime(2003, 12, 31)
    
    if admissao <= data_limite_paridade:
        if "Permanente" in regra_tipo:
            return "Média Aritmética (60% + 2% ao ano) - Sem Paridade"
        return "Integralidade e Paridade (Último salário com reajuste dos ativos)"
    else:
        if "Pedágio" in regra_tipo or "Transição" in regra_tipo:
            return "100% da Média das Contribuições (Sem Paridade)"
        return "Média Aritmética (60% + 2% ao ano) - Sem Paridade"

# --- REGRAS DE VALIDAÇÃO ---

def regra_permanente(sexo, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo):
    idade_min = 65 if sexo == 'masculino' else 62
    if idade >= idade_min and tempo_contribuicao >= DIAS_25_ANOS and tempo_efetivo >= DIAS_10_ANOS and tempo_cargo >= DIAS_5_ANOS:
        return '✅ Atende à REGRA PERMANENTE (Art. 2º, III da LCE 1.354/20).'
    return '❌ Não atende aos requisitos da Regra Permanente.'

def transicao_1(sexo, idade, admissao, tempo_contribuicao, tempo_efetivo, tempo_cargo):
    data_limite = datetime(2003, 12, 31)
    idade_min = 60 if sexo == 'masculino' else 57
    if admissao > data_limite:
        return 'ℹ️ Regra de Transição 1 não se aplica (Admissão após 2003).'
    if idade >= idade_min and tempo_contribuicao >= (DIAS_35_ANOS if sexo == 'masculino' else DIAS_30_ANOS) \
       and tempo_efetivo >= DIAS_20_ANOS and tempo_cargo >= DIAS_5_ANOS:
        return '✅ Atende à REGRA DE TRANSIÇÃO 1 (Integralidade/Paridade).'
    return '❌ Não atende aos requisitos da Regra de Transição 1.'

def transicao_pontos(sexo, idade, tempo_contribuicao, tempo_efetivo, tempo_cargo, fechamento):
    """Regra de Transição por Pontos (Art. 10 LC 1354/20)"""
    pontos = idade + (tempo_contribuicao / 365)
    ano_atual = fechamento.year
    base_pontos = 86 if sexo == 'feminino' else 96
    meta_pontos = base_pontos + (ano_atual - 2020)
    if meta_pontos > (100 if sexo == 'feminino' else 105):
        meta_pontos = 100 if sexo == 'feminino' else 105
        
    if pontos >= meta_pontos and tempo_efetivo >= DIAS_20_ANOS and tempo_cargo >= DIAS_5_ANOS:
        return f'✅ Atende à REGRA DE PONTOS ({int(pontos)} pts atingidos, meta {meta_pontos}).'
    return f'❌ Não atende à Regra de Pontos (Possui {int(pontos)} pts, meta {meta_pontos}).'

# --- PREVISÕES ---

def previsao_regra_permanente(sexo, nascimento, cargo, primeiro_emprego, exercicio, inss, outros, oab, fechamento, total_dias_ausencia=0):
    nome = "Regra Permanente (Art. 2º LC 1354/20)"
    idade_alvo = 65 if sexo == 'masculino' else 62
    data_idade = somar_anos(nascimento, idade_alvo)
    
    # Subtrair dias de ausência do cálculo de contribuição
    tempo_contrib_efetivo = DIAS_25_ANOS - total_dias_ausencia
    data_contrib = primeiro_emprego + timedelta(days=tempo_contrib_efetivo) - timedelta(days=(inss + outros + oab))
    
    data_servico = somar_anos(exercicio, 10)
    data_cargo = somar_anos(exercicio, 5)
    data_final = max(data_idade, data_contrib, data_servico, data_cargo)
    
    provento = obter_tipo_provento(exercicio, "Permanente")
    
    observacao = ""
    if total_dias_ausencia > 0:
        observacao = f" (com desconto de {total_dias_ausencia} dias de ausência)"
    
    return [
        f"**{nome}**",
        f"💰 **Proventos:** {provento}",
        f"Idade ({idade_alvo} anos): {format_date(data_idade)}",
        f"Contribuição (25 anos{observacao}): {format_date(data_contrib)}",
        f"Serviço Público (10 anos): {format_date(data_servico)}",
        f"🎯 **Previsão Final: {format_date(data_final)}**"
    ]

def previsao_transicao_pedagio(sexo, nascimento, cargo, primeiro_emprego, exercicio, inss, outros, oab, fechamento, total_dias_ausencia=0):
    nome = "Regra de Transição - Pedágio 100% (Art. 11 LC 1354/20)"
    idade_alvo = 60 if sexo == 'masculino' else 57
    data_idade = somar_anos(nascimento, idade_alvo)
    
    data_reforma = datetime(2020, 3, 7)
    tempo_ate_reforma = tempo_contrib(primeiro_emprego, data_reforma, oab, inss, outros)
    meta_original = DIAS_35_ANOS if sexo == 'masculino' else DIAS_30_ANOS
    
    if tempo_ate_reforma >= meta_original:
        tempo_contrib_efetivo = meta_original - total_dias_ausencia
        data_contrib = primeiro_emprego + timedelta(days=tempo_contrib_efetivo) - timedelta(days=(inss + outros + oab))
    else:
        falta_em_2020 = meta_original - tempo_ate_reforma
        total_dias = meta_original + falta_em_2020 - total_dias_ausencia
        data_contrib = primeiro_emprego + timedelta(days=total_dias) - timedelta(days=(inss + outros + oab))
        
    data_servico = somar_anos(exercicio, 20)
    data_cargo = somar_anos(exercicio, 5)
    data_final = max(data_idade, data_contrib, data_servico, data_cargo)
    
    provento = obter_tipo_provento(exercicio, "Pedágio")
    
    observacao = ""
    if total_dias_ausencia > 0:
        observacao = f" (com desconto de {total_dias_ausencia} dias de ausência)"
    
    return [
        f"**{nome}**",
        f"💰 **Proventos:** {provento}",
        f"Idade ({idade_alvo} anos): {format_date(data_idade)}",
        f"Contribuição + Pedágio{observacao}: {format_date(data_contrib)}",
        f"Serviço Público (20 anos): {format_date(data_servico)}",
        f"🎯 **Previsão Final: {format_date(data_final)}**"
    ]

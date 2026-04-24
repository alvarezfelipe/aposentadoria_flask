# 🛡️ Sistema de Previsão de Aposentadoria - RH

Este é um sistema institucional desenvolvido para o setor de Recursos Humanos, focado no cálculo preciso e visualização moderna de previsões de aposentadoria para servidores públicos, em total conformidade com a **Lei Complementar Estadual nº 1.354/2020**.

## 🚀 Visão Geral

O sistema automatiza a análise de requisitos complexos da previdência, permitindo que o RH insira dados funcionais e obtenha instantaneamente as datas prováveis de aposentadoria em diferentes modalidades, além de identificar a forma de cálculo dos proventos (Integralidade ou Média).

---

## ✨ Principais Funcionalidades

### 1. Interface Moderna e Intuitiva
- **Dashboard de Entrada:** Formulário organizado em seções lógicas (Dados Pessoais, Funcionais e Tempo de Contribuição).
- **Componentes Visuais:** Uso de "Radio Cards" para seleção de sexo e cargo, facilitando a usabilidade.
- **Responsividade:** Layout adaptável para computadores, tablets e celulares.

### 2. Inteligência de Cálculo (Backend)
- **Precisão Temporal:** Utiliza a biblioteca `python-dateutil` para cálculos exatos de anos, meses e dias, considerando anos bissextos.
- **Múltiplas Regras:**
  - **Regra Permanente:** Cálculo baseado na idade mínima e tempo de contribuição geral.
  - **Regra de Transição (Pedágio 100%):** Cálculo automático do tempo faltante em 07/03/2020 e aplicação do pedágio correspondente.
  - **Regra de Pontos:** Soma de idade e tempo com metas progressivas anuais.
- **Identificação de Proventos:** Define automaticamente se o servidor terá direito a **Integralidade e Paridade** (ingresso até 2003) ou **Média das Contribuições**.

### 3. Relatório de Resultados
- **Destaque Visual:** Cards coloridos que indicam claramente a modalidade e a data final.
- **Transparência:** Listagem detalhada de cada requisito (Idade, Tempo de Cargo, Serviço Público).
- **Modo de Impressão:** Estilos CSS otimizados para gerar relatórios limpos em papel ou PDF.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia | Finalidade |
| :--- | :--- | :--- |
| **Backend** | Python 3.11 / Flask | Lógica de rotas e processamento de dados. |
| **Cálculos** | python-dateutil | Manipulação precisa de calendários e datas. |
| **Frontend** | HTML5 / CSS3 | Estrutura e estilização personalizada. |
| **Framework UI** | Bootstrap 5.3 | Componentes responsivos e grid layout. |
| **Iconografia** | Bootstrap Icons | Identificação visual de campos e seções. |
| **Tipografia** | Google Fonts (Inter) | Leitura clara e moderna. |

---

## ⚖️ Regras de Negócio Aplicadas

O sistema foi calibrado com base na **LC 1354/2020**, cobrindo:
- **Idades Mínimas:** 62 anos (Feminino) e 65 anos (Masculino) para regra permanente.
- **Tempo de Contribuição:** 25, 30 ou 35 anos conforme a modalidade.
- **Pedágio:** Exigência de 100% do tempo que faltava para a aposentadoria na data da reforma (07/03/2020).
- **Carreiras Específicas:** Lógica preparada para Procuradores e Engenheiros.

---

## 📦 Como Instalar e Rodar

1. **Clone o projeto** para sua máquina local.
2. **Instale as dependências** necessárias via terminal:
   ```bash
   pip install flask python-dateutil
   ```
3. **Estrutura de Pastas:**
   ```text
   /projeto
   ├── app.py                 # Servidor Flask
   ├── funcoes.py             # Utilitários de data
   ├── regras_aposentadoria.py # Lógica legislativa
   └── /templates
       ├── index.html         # Página inicial
       └── exibicao.html      # Página de resultados
   ```
4. **Execute o aplicativo:**
   ```bash
   python app.py
   ```
5. Acesse no seu navegador: `http://localhost:8080`

---

## 📧 Suporte e Desenvolvimento

Desenvolvido por **Felipe Alvarez dos Santos** | PR07 — Bauru.
Para dúvidas ou sugestões: [felipedossantos@sp.gov.br](mailto:felipedossantos@sp.gov.br)

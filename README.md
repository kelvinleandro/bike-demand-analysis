# Análise e Previsão de Demanda de Compartilhamento de Bicicletas

## Estrutura do Projeto

O projeto está organizado da seguinte forma para garantir clareza e modularidade:

```
├── data/
│   └── data.csv             # Conjunto de dados original
├── notebooks/
│   ├── 01-exploratory-data-analysis.ipynb  # Notebook para Análise Exploratória
│   └── 02-comparative-analysis.ipynb       # Notebook para Modelagem e Análise Comparativa
├── requirements.txt         # Lista de dependências Python para o projeto
└── utils/
    ├── __init__.py          # Torna o diretório 'utils' um pacote Python
    ├── date.py              # Funções auxiliares relacionadas a datas
    └── evaluation.py        # Funções auxiliares para avaliação de modelos
```

## Instruções para Configuração do Ambiente

Para executar este projeto, é altamente recomendado o uso de um ambiente virtual para isolar as dependências.

1. Clone o repositório

   ```
   git clone https://github.com/kelvinleandro/bike-demand-analysis.git
   cd bike-demand-analysis
   ```

2. Crie e Ative um Ambiente Virtual

   - No macOS/Linux:

     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

   - No Windows:
     ```
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. Instale as Dependências

   ```
   pip install -r requirements.txt
   ```

# Checkpoint 05 - Predição da Qualidade de Vinhos (Machine Learning)

##  Identificação do Grupo
Rafael Felix Souza - RM: 565855
*Pedro Henrique Sartorelli Ferreira - RM: 563281
*Nathália dos Santos Cordeiro - RM: 563072
*Bruno Bagattini Fernandes - RM: 562863
*Matheus Brasil Borges Sevilha Angelotti - RM: 561456

##  Proposta do Trabalho
O objetivo deste projeto é prever a qualidade sensorial de vinhos verdes tintos portugueses com base em 11 atributos físico-químicos (como acidez, pH, teor alcoólico, etc.). A qualidade é medida em uma escala contínua (0 a 10), caracterizando o problema como uma tarefa de **Regressão**. A aplicação supervisionada permite estimar a qualidade do vinho antes do engarrafamento, otimizando o controle de qualidade industrial.

##  Base de Dados
A base de dados utilizada é o **Wine Quality Dataset (Red)**.
* **Fonte:** UCI Machine Learning Repository
* **Link para download/acesso:** [UCI Repository - Wine Quality](https://archive.ics.uci.edu/ml/datasets/wine+quality)

##  Resumo e Escolha do Modelo
Foram testados e comparados os algoritmos Random Forest, XGBoost e LightGBM. A modelagem envolveu a separação rígida de dados de treino e teste e o uso de K-Fold Cross-Validation (K=5).
O modelo final escolhido foi o **LightGBM**, otimizado via **Optuna** (TPE Bayesiano). Esta configuração apresentou o melhor balanço entre viés e variância, mitigando o *overfitting* inicial sem sacrificar o poder preditivo, superando a técnica de Grid Search em eficiência temporal e precisão.

##  Como instalar e executar o projeto localmente
1. Clone este repositório para sua máquina:
   `git clone [COLOQUE_SEU_LINK_DO_GITHUB_AQUI]`
2. Acesse a pasta do projeto:
   `cd [NOME_DA_PASTA]`
3. Instale as dependências exigidas:
   `pip install -r requirements.txt`
4. Para rodar a interface web (Streamlit) localmente:
   `streamlit run app.py`

##  Links do Projeto
* **Repositório GitHub:** [INSERIR LINK DO GITHUB]
* **Aplicação Streamlit (Deploy):** [INSERIR LINK DA APLICAÇÃO NO STREAMLIT CLOUD]

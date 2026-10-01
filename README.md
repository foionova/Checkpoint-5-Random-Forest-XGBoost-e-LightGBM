#  Checkpoint 05 - Predição da Qualidade de Vinhos (Machine Learning)

> **Objetivo:** Prever a qualidade sensorial de vinhos verdes tintos portugueses com base em seus atributos físico-químicos (como acidez, pH, teor alcoólico, etc.), auxiliando produtores no controle de qualidade.

---

##  Integrantes do Grupo

- **Rafael Felix Souza** - RM: 565855
- **Pedro Henrique Sartorelli Ferreira** - RM: 563281
- **Nathália dos Santos Cordeiro** - RM: 563072
- **Bruno Bagattini Fernandes** - RM: 562863
- **Matheus Brasil Borges Sevilha Angelotti** - RM: 561456

---

##  Proposta do Trabalho

O objetivo deste projeto é prever a qualidade sensorial de vinhos verdes tintos portugueses com base em 11 atributos físico-químicos (como acidez, pH, teor alcoólico, etc.). A qualidade é medida em uma escala contínua (0 a 10), caracterizando o problema como uma tarefa de **Regressão**. A aplicação supervisionada permite estimar a qualidade do vinho antes do engarrafamento, otimizando o controle de qualidade industrial.

##  Fonte dos Dados

A base de dados utilizada é o **Wine Quality Dataset (Red)**, disponibilizado publicamente pelo *UCI Machine Learning Repository*.

**Link para a base:** [UCI Repository - Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality)

##  Resumo dos Resultados

Foram comparados os algoritmos **Random Forest, XGBoost e LightGBM**. 

O **modelo vencedor foi o LightGBM**, otimizado via **Optuna (TPE Bayesiano)**, apresentando:
- Melhor balanço entre viés e variância.
- Tempo de processamento altamente eficiente.
- RMSE final no conjunto de teste que confirmou a robustez do modelo e a ausência de *overfitting*.

---

Links do Projeto (Deploy)
Interface Online (Streamlit): https://checkpoint-5-random-forest-xgboost-e-lightgbm-bhinuwx2r8f68tgh.streamlit.app/
Repositório (GitHub): https://github.com/foionova/Checkpoint-5-Random-Forest-XGBoost-e-LightGBM

---

## Instruções de Instalação e Execução (Reprodução Local)

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter o Python instalado e instale as dependências executando:
   `pip install -r requirements.txt`
3. O modelo final já está treinado e salvo como `modelo_vinhos_lgbm.pkl`.
4. Para abrir a interface web localmente, execute o comando no terminal:
   `streamlit run app.py`

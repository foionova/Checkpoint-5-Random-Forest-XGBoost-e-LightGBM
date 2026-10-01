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

🔗 **Link para a base:** [UCI Repository - Wine Quality](https://archive.ics.uci.edu/dataset/186/wine+quality)

##  Resumo dos Resultados

Foram comparados os algoritmos **Random Forest, XGBoost e LightGBM**. 

O **modelo vencedor foi o LightGBM**, otimizado via **Optuna (TPE Bayesiano)**, apresentando:
- Melhor balanço entre viés e variância.
- Tempo de processamento altamente eficiente.
- RMSE final no conjunto de teste que confirmou a robustez do modelo e a ausência de *overfitting*.

---

##  Como instalar e executar localmente

Clone este repositório:
```bash
git clone [https://github.com/foionova/Checkpoint-5-Random-Forest-XGBoost-e-LightGBM](https://github.com/foionova/Checkpoint-5-Random-Forest-XGBoost-e-LightGBM)

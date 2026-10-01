##Checkpoint 05 - Predição da Qualidade de Vinhos (Machine Learning)
##Integrantes do Grupo

Rafael Felix Souza - RM: 565855
Pedro Henrique Sartorelli Ferreira - RM: 563281
Nathália dos Santos Cordeiro - RM: 563072
Bruno Bagattini Fernandes - RM: 562863
Matheus Brasil Borges Sevilha Angelotti - RM: 561456

##Descrição do Problema
O objetivo deste projeto é prever a qualidade sensorial de vinhos verdes tintos portugueses com base em seus atributos físico-químicos (como acidez, pH, teor alcoólico, etc.). A qualidade é medida em uma escala contínua, caracterizando o problema como uma tarefa de Regressão. A aplicação de Machine Learning permite estimar a qualidade antes do engarrafamento, auxiliando produtores no controle de qualidade.

##Fonte dos Dados
A base de dados utilizada é o Wine Quality Dataset (Red), disponibilizado publicamente pelo UCI Machine Learning Repository.

Link para a base: UCI Repository - Wine Quality

##Resumo dos Resultados
Foram comparados os algoritmos Random Forest, XGBoost e LightGBM. O modelo vencedor foi o LightGBM, otimizado via Optuna (TPE Bayesiano), apresentando o melhor balanço entre o viés e a variância e um tempo de processamento altamente eficiente. O RMSE final no conjunto de teste confirmou a robustez do modelo e a ausência de overfitting.

##Como instalar e executar o projeto localmente
Clone este repositório:
git clone <link_do_seu_repositorio>

Acesse a pasta do projeto:
cd <nome_da_pasta>

Instale as dependências exigidas:
pip install -r requirements.txt

Para rodar a interface Streamlit localmente:
streamlit run app.py

#Links do Projeto
Repositório GitHub: [[Inserir Link do GitHub]](https://github.com/foionova/Checkpoint-5-Random-Forest-XGBoost-e-LightGBM)

Aplicação Streamlit (Online): [Inserir Link do Streamlit Cloud]

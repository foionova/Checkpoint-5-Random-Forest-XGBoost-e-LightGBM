import streamlit as st
import pandas as pd
import joblib

# Configura ícone na aba do navegador e layout
st.set_page_config(page_title="Dashboard de Vinhos", layout="centered")


@st.cache_resource
def load_model():
    return joblib.load('Projeto_Vinhos/modelo_vinhos_lgbm.pkl')


modelo = load_model()

# Novo Título e Descrição
st.title(' Preditor de Qualidade de Vinhos')
st.markdown(
    'Ajuste os parâmetros químicos abaixo para descobrir a qualidade estimada da safra através de **Machine Learning**.')

st.divider()
st.subheader('Propriedades Físico-Químicas')

# Separando em colunas com categorias
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Ácidos e Açúcares**")
    fixed_acidity = st.number_input('Fixed Acidity', value=7.4, format="%.2f")
    volatile_acidity = st.number_input('Volatile Acidity', value=0.70, format="%.3f")
    citric_acid = st.number_input('Citric Acid', value=0.00, format="%.2f")
    residual_sugar = st.number_input('Residual Sugar', value=1.9, format="%.1f")
    chlorides = st.number_input('Chlorides', value=0.076, format="%.3f")

with col2:
    st.markdown("**Compostos e Outros**")
    free_sulfur_dioxide = st.number_input('Free Sulfur Dioxide', value=11.0, format="%.1f")
    total_sulfur_dioxide = st.number_input('Total Sulfur Dioxide', value=34.0, format="%.1f")
    density = st.number_input('Density', value=0.9978, format="%.4f")
    pH = st.number_input('pH', value=3.51, format="%.2f")
    sulphates = st.number_input('Sulphates', value=0.56, format="%.2f")
    alcohol = st.number_input('Alcohol', value=9.4, format="%.1f")

st.divider()

# Botão principal colorido (type="primary")
if st.button(' Prever Qualidade', type="primary", use_container_width=True):
    dados_entrada = pd.DataFrame([[
        fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
        free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol
    ]], columns=[
        'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
        'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'
    ])

    previsao = modelo.predict(dados_entrada)[0]

    # Exibe o resultado como uma "Métrica" visual bonita
    st.subheader("Resultado:")
    st.metric(label="Qualidade Estimada (Escala 3 a 8)", value=f"{previsao:.2f}")

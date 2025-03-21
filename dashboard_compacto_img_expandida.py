
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Dashboard Compacto", page_icon="📊")

# Reduzindo margens e espaçamentos
st.markdown('''
<style>
    .block-container {padding: 0.5rem 1rem;}
    h1 {font-size: 28px;}
    h2 {font-size: 20px;}
    .stMetric {font-size: 20px;}
</style>
''', unsafe_allow_html=True)

# Dados
df_amostras = pd.read_csv('2025-03-21T19-37_export.csv')
total_amostras = df_amostras['Quantidade de Amostras'].sum()

# Cabeçalho
st.title("📊 Dashboard Compacto")

# Layout ajustado com a imagem expandida
col1, col2 = st.columns([2, 1], gap='small')
with col1:
    st.subheader("📍 Furos")
    st.image('image.png', use_container_width=True)

with col2:
    st.subheader("🔢 Total Geral")
    st.metric("Amostras", total_amostras)

    df_status = pd.DataFrame({'Status': ['Finalizado', 'Em Andamento'], 'Percentual': [99, 1]})
    fig_status = px.pie(df_status, names='Status', values='Percentual',
                        color_discrete_map={'Finalizado':'green', 'Em Andamento':'orange'},
                        hole=0.6)
    fig_status.update_traces(textposition='inside', textinfo='percent+label', textfont_size=12)
    fig_status.update_layout(margin=dict(t=20, b=20, l=0, r=0), height=250)
    st.plotly_chart(fig_status, use_container_width=True)

# Segunda linha com gráficos compactos
col3, col4 = st.columns(2, gap='small')
with col3:
    st.subheader("📌 Distribuição")
    fig_pie = px.pie(df_amostras, names='Furo', values='Quantidade de Amostras', hole=0.6)
    fig_pie.update_traces(textposition='inside', textinfo='label', textfont_size=12)
    fig_pie.update_layout(showlegend=False, margin=dict(t=20, b=20, l=0, r=0), height=300)
    st.plotly_chart(fig_pie, use_container_width=True)

with col4:
    st.subheader("📈 Amostras por Furo")
    fig_bar = px.bar(df_amostras.sort_values(by='Quantidade de Amostras', ascending=False), 
                     x='Furo', y='Quantidade de Amostras', text_auto=True,
                     labels={"Quantidade de Amostras": "Qtd.", "Furo": "Furo"})
    fig_bar.update_layout(
        xaxis_tickangle=-45, margin=dict(t=20, b=20, l=0, r=0), height=300,
        xaxis=dict(
            title=dict(text="<b>Furo</b>", font=dict(color="black", size=12)),
            tickfont=dict(color="black", size=10)
        ),
        yaxis=dict(
            title=dict(text="<b>Qtd.</b>", font=dict(color="black", size=12)),
            tickfont=dict(color="black", size=10)
        )
    )
    st.plotly_chart(fig_bar, use_container_width=True)

import streamlit as st
import pandas as pd
import random
import time
import plotly.express as px

st.set_page_config(
    page_title="Competição de Pontes",
    layout="wide"
)

st.title(" Competição de Pontes de Palitos")

# ======================
# CONFIGURAÇÃO DAS PONTES
# ======================

pontes = [
    {"nome": "Equipe A", "resistencia": random.uniform(30, 50)},
    {"nome": "Equipe B", "resistencia": random.uniform(30, 50)},
    {"nome": "Equipe C", "resistencia": random.uniform(30, 50)}
]

ranking = []

# ======================
# ELEMENTOS DA INTERFACE
# ======================

col1, col2, col3 = st.columns(3)

peso_box = col1.empty()
recorde_box = col2.empty()
status_box = col3.empty()

grafico_area = st.empty()

ranking_area = st.empty()

# ======================
# VARIÁVEIS DO TESTE
# ======================

peso = 0
peso_max = 0
dados = []

# ======================
# LOOP DA SIMULAÇÃO
# ======================

for ponte in pontes:

    peso = 0
    peso_max = 0
    dados = []

    status_box.metric("Status", "TESTE EM ANDAMENTO")

    for tempo in range(100):

        incremento = random.uniform(1,10)
        peso += incremento

        if peso > peso_max:
            peso_max = peso

        dados.append({"tempo": tempo, "peso": peso})

        df = pd.DataFrame(dados)

        fig = px.line(
            df,
            x="tempo",
            y="peso",
            title=f"Teste de Resistência - {ponte['nome']}"
        )

        grafico_area.plotly_chart(fig, use_container_width=True)

        peso_box.metric("Peso Atual (kg)", f"{peso:.2f}")
        recorde_box.metric("Recorde Atual (kg)", f"{peso_max:.2f}")

        if peso >= ponte["resistencia"]:

            status_box.metric("Status", " PONTE QUEBROU")

            ranking.append({
                "Equipe": ponte["nome"],
                "Peso Suportado": round(peso_max,2)
            })

            break

        time.sleep(0.8)

    ranking_df = pd.DataFrame(ranking)
    ranking_df = ranking_df.sort_values(by="Peso Suportado", ascending=False)

    ranking_area.subheader("🏆 Ranking da Competição")
    ranking_area.dataframe(ranking_df)

    time.sleep(2)

status_box.metric("Status", "COMPETIÇÃO FINALIZADA")

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Operations KPI Dashboard", layout="wide")

st.title(" KPI Dashboard")

uploaded_file = st.file_uploader("Upload operations CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    total_cases = df["CasesProcessed"].sum()
    sla_pct = round((df["SLAStatus"].eq("Met").sum()/len(df))*100,2)
    backlog = df["PendingCases"].sum()
    agents = df["Agent"].nunique()

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Total Cases", total_cases)
    c2.metric("SLA Compliance %", sla_pct)
    c3.metric("Pending Cases", backlog)
    c4.metric("Active Agents", agents)

    st.subheader("Cases by Team")
    fig1 = px.bar(df.groupby("Team",as_index=False)["CasesProcessed"].sum(),
                  x="Team", y="CasesProcessed")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Agent Productivity")
    fig2 = px.bar(df, x="Agent", y="CasesProcessed")
    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(df)

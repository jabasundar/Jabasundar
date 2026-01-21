import streamlit as st
import sqlite3
import pandas as pd
import os
import altair as alt

DB_PATH = "aviation_data.db"
SQL_PATH = "sql_queries/test_cases.sql"

conn = sqlite3.connect(DB_PATH)

menu = st.sidebar.selectbox("Select View", ["Raw Tables", "SQL Queries", "Charts"])

if menu == "Raw Tables":
    st.title("✈ Air Tracker: Raw Tables")

    st.subheader("Airports")
    df_airport = pd.read_sql("SELECT * FROM airport", conn)
    st.dataframe(df_airport)

    st.subheader("Flights")
    df_flights = pd.read_sql("SELECT * FROM flights", conn)
    st.dataframe(df_flights)

    st.subheader("Airport Delays")
    df_delays = pd.read_sql("SELECT * FROM airport_delays", conn)
    st.dataframe(df_delays)

elif menu == "SQL Queries":
    st.title("✈ Air Tracker: SQL Queries")

    queries = {}
    if os.path.exists(SQL_PATH):
        with open(SQL_PATH, "r", encoding="utf-8") as f:
            all_queries = f.read().split(";")
            for i, q in enumerate(all_queries):
                q = q.strip()
                if q:
                    queries[f"Query {i+1}"] = q
    else:
        st.error(f"SQL file not found: {SQL_PATH}")

    if queries:
        selected_query = st.selectbox("Select Query", list(queries.keys()))
        if selected_query:
            df = pd.read_sql(queries[selected_query], conn)
            st.dataframe(df)
        else:
            st.warning("No query selected")
    else:
        st.warning("No queries found in SQL file")

elif menu == "Charts":
    st.title("✈ Air Tracker: Charts")

    st.subheader("Average Delays by Airport")
    df_delays = pd.read_sql("SELECT airport_code, avg_delay_minutes FROM airport_delays", conn)
    chart1 = alt.Chart(df_delays).mark_bar().encode(
        x='airport_code',
        y='avg_delay_minutes',
        tooltip=['airport_code', 'avg_delay_minutes']
    )
    st.altair_chart(chart1, use_container_width=True)

    st.subheader("Flights per Airline")
    df_flights = pd.read_sql("""
        SELECT airline, COUNT(*) as total_flights
        FROM flights
        GROUP BY airline
        ORDER BY total_flights DESC
    """, conn)
    chart2 = alt.Chart(df_flights).mark_bar(color='green').encode(
        x='airline',
        y='total_flights',
        tooltip=['airline', 'total_flights']
    )
    st.altair_chart(chart2, use_container_width=True)

conn.close()

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

from database import create_database, run_query
from llm_query import generate_sql

import streamlit as st

st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none;}
button[kind="header"] {display: none;}
div[data-testid="stSidebarNav"] {display: none;}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([8,1])

with col2:
    if st.button("Logout"):
        st.session_state.clear()
        st.switch_page("landing.py")

if "logged_in" not in st.session_state:

    st.warning("Please login first")

    st.switch_page("pages/login.py")



# Page settings
st.set_page_config(
    page_title="Conversational BI Dashboard",
    layout="wide"
)


# Title
st.title("Conversational BI Dashboard")

st.write("Ask your business question and AI will generate SQL and chart automatically.")


# Ensure database exists
create_database()


# User input
query = st.text_input(
    "Ask your business question",
    placeholder="Example: Show average online spend by gender"
)


# Button
if st.button("Generate Chart"):

    if query.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    try:

        # ---- Generate SQL + Chart ----
        sql_query, chart_type = generate_sql(query)

        st.subheader("Generated SQL")

        st.code(sql_query)

        # ---- Run SQL ----
        df = run_query(sql_query)

        if df.empty:
            st.warning("Query returned no results.")
            st.stop()

        # Clean dataframe
        df = df.replace([np.inf, -np.inf], 0)
        df = df.fillna(0)

        st.subheader("Query Result")
        st.dataframe(df)


        columns = df.columns


        # ---------------- HISTOGRAM ----------------
        if chart_type == "histogram":

            st.subheader("Histogram")

            fig = px.histogram(
                df,
                x=columns[0],
                nbins=20
            )


        # ---------------- SCATTER ----------------
        elif chart_type == "scatter":

            if len(columns) < 2:
                st.error("Scatter plot requires two columns.")
                st.stop()

            st.subheader("Scatter Plot")

            fig = px.scatter(
                df,
                x=columns[0],
                y=columns[1]
            )


        # ---------------- LINE ----------------
        elif chart_type == "line":

            if len(columns) < 2:
                st.error("Line chart requires two columns.")
                st.stop()

            st.subheader("Line Chart")

            fig = px.line(
                df,
                x=columns[0],
                y=columns[1]
            )


        # ---------------- PIE ----------------
        elif chart_type == "pie":

            if len(columns) < 2:
                st.error("Pie chart requires category + value.")
                st.stop()

            st.subheader("Pie Chart")

            fig = px.pie(
                df,
                names=columns[0],
                values=columns[1]
            )


        # ---------------- BAR (DEFAULT) ----------------
       
        else:

            if len(columns) < 2:
                st.error("Bar chart requires category + value.")
                st.stop()

            st.subheader("Bar Chart")

            # 🔥 CASE 1: 3 columns (2 category + 1 value)
            if len(columns) == 3:

                fig = px.bar(
                    df,
                    x=columns[0],
                    y=columns[2],
                    color=columns[1],   # 🔥 VERY IMPORTANT
                    barmode='group'
                )

            # 🔥 CASE 2: normal bar
            else:

                fig = px.bar(
                    df,
                    x=columns[0],
                    y=columns[1]
                )


        # Display chart
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:

        st.error(f"Error: {str(e)}")

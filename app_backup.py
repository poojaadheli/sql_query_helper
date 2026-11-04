import streamlit as st
import pandas as pd
import pymysql

st.set_page_config(page_title="SQL Query Helper", layout="wide")

st.title("SQL Query Helper")
st.write("Write a SELECT query to explore employee data.")

with st.expander("View table columns"):
    st.code(
        "employees: employee_id, employee_name, "
        "department, salary, city"
    )

query = st.text_area(
    "Enter your SQL query:",
    value="SELECT * FROM employees;",
    height=150
)

if st.button("Run Query"):
    if not query.strip().lower().startswith("select"):
        st.warning("Please enter a SELECT query.")
    else:
        connection = None

        try:
            connection = pymysql.connect(
                host="localhost",
                user="sql_helper",
                password="SqlHelper@123",
                database="sql_query_helper1",
                connect_timeout=10,
                read_timeout=30
            )

            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]

            result = pd.DataFrame(rows, columns=columns)

            st.success(f"Query successful! Rows returned: {len(result)}")
            st.dataframe(result, use_container_width=True)

        except pymysql.MySQLError as error:
            st.error(f"Database error: {error}")

        finally:
            if connection is not None:
                connection.close()

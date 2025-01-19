from dotenv import load_dotenv
load_dotenv()## load all the env variables
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
##Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#Function to load Google Gemini Model and provide SQL query as response
#question: user query
#prompt: How model should behave
def get_Model_Response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

#Function to execute the query
def executeSqlQuery(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

##Define the prompt
prompt=["""
        We know you are an expert in converting English questions  to SQL Query!
        The SQL database has table PRODUCTS and columns are PRODUCT_ID,PRODUCT_NAME,PRICE,CATEGORY,SALES_PERCENTAGE_2023,SALES_PERCENTAGE_2024
        Example: List all the products
        The Sql command will be something like this SELECT * FROM PRODUCTS;
        also the sql code should not have ``` in beginning or end and sql word
        """
        ]

##Creating stramlit app
st.set_page_config(page_title="Retrive SQL Query")
st.header("Gemini App to retrive SQL Data")
question=st.text_input("Input : ",key="input")
submit=st.button("Ask the Question")
if submit:
    print("User question is ",question)
    sqlQueryFromModel=get_Model_Response(question,prompt)
    print("SQL Query from Model ",sqlQueryFromModel)
    response = executeSqlQuery(sqlQueryFromModel,"products.db")
    st.subheader("The Response is ")
    for row in response:
        st.header(row)

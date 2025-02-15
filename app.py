from dotenv import load_dotenv
load_dotenv()# load all the Enviorment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai


##configuire our API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#FUNCTION TO LOAD GOOGLE GEMINI MODEL AND PROVIDE QUERY AS RESPONSE
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text



#Function to retrieve query from the sql database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define your prompt
prompt =[ """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS \n

For example,\n
Example 1 - How many entries of records are present?
the SQL command will be something like this:
SELECT COUNT(*) FROM STUDENT;\n

Example 2 - Tell me all the students studying in Data Science class?
the SQL command will be something like this:
SELECT * FROM STUDENT WHERE CLASS="Data Science";

Also, the SQL code should not have '*' in the beginning or end and sql word in output
"""
]

##streamlit app

st.set_page_config(page_title="I CAN RETRIEVE ANY SQL QUERY")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key='input')

submit=st.button("Ask the question")


#if submit is clicked

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is ")
    for row in data:
        print(row)
        st.header(row)
        
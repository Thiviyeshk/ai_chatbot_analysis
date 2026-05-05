###### **AI Data Chatbot (Natural Language to SQL)**

###### 

###### **Problem Statement**



Business users often struggle to query databases using SQL.

This project builds an \*\*AI-powered chatbot\*\* that converts natural language questions into SQL queries and returns results instantly.



###### **Project Overview**



The AI Data Chatbot allows users to:



\* Ask questions in plain English

\* Automatically generate SQL queries

\* Fetch results from a database

\* Display results in a clean tabular format



**Example:**



\*User Input: "Show bottom sales"

\*Generated SQL: `SELECT \* FROM sales`

\*Output: Table with sales data



###### **Tools \& Technologies**



\* Python

\* Pandas

\* SQLite

\* OpenAI API (for natural language understanding)

\* Streamlit (for UI)



###### **Project Workflow**



**1. Data Preparation**



&#x20;  \* Loaded dataset into SQLite database

&#x20;  \* Structured table (`sales`) for querying



**2. Query Generation**



&#x20;  \* User inputs natural language question

&#x20;  \* AI model converts it into SQL query



**3. Query Execution**



&#x20;  \* Generated SQL runs on database

&#x20;  \* Results fetched using Python



**4. Output Display**



&#x20;  \* Results shown in tabular format

&#x20;  \* Clean UI using Streamlit



###### **Key Features**



\* Natural Language → SQL Conversion

\* Real-time Data Querying

\* Instant Results Display

\* Interactive UI

\* Supports dynamic business queries



###### **Application Preview**



Example Use Cases



\* "Show top sales"

\* "Get total revenue"

\* "List all customers"

\* "Find highest selling products"



This removes the need for manual SQL writing.



###### **Business Impact**



\* Empowers non-technical users to access data

\* Reduces dependency on data teams

\* Speeds up decision-making

\* Improves productivity with AI automation



###### **How to Run**



bash id="run123"

pip install -r requirements.txt

streamlit run app.py

**Live**

https://aichatbotanalysis-hdxwurmwv4kjznxvvhv4am.streamlit.app/


###### **Future Improvements**



\* Add more complex SQL query handling

\* Improve accuracy of AI-generated queries

\* Add data visualization support

\* Connect to live databases



###### 

###### **Author**


Thiviyesh K 
Aspiring Data Analyst 




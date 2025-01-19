Text-to-SQL Large Language Models (LLMs) are AI-driven systems that transform natural language queries into structured SQL code. These models are trained on vast datasets that include natural language statements and their corresponding SQL queries, enabling them to understand and process user intent effectively. 
1. **Natural Language Understanding**: Accepts queries in plain English (or other supported languages) and maps them to the appropriate SQL commands.
2. **SQL Generation**: Outputs syntactically correct SQL queries based on the user's request.
3. **Database Schema Awareness**: Understands database structures, table relationships, and field types to ensure query accuracy.
4. **Dynamic Query Handling**: Supports basic to complex SQL constructs, including filtering, joins, aggregation, and nested queries.

### Use Cases:
- Querying databases without requiring SQL expertise.
- Automating data retrieval tasks in business intelligence tools.
- Providing SQL assistance for developers and analysts.

### Implementation
1.SQLLite: Insert some records through Python Prgramming Language.
2.Creating LLM Application, LLM generate the Query
3.Query hit the database and get the records.

### Commads
1 Creating Virtual env: python -m venv <local_path>/Text-To-SQL-LLM/textSqlVenv
2.Activate Virtual env: python -m venv textSqlVenv
3.Installing required modules: pip install -r .\requirements.txt

##Examples:
 User question is  Which soap achieved the highest sales in 2024?
SQL Query from Model  SELECT PRODUCT_NAME FROM PRODUCTS
					  WHERE CATEGORY = 'Soap'
					  AND SALES_PERCENTAGE_2024 = (SELECT MAX(SALES_PERCENTAGE_2024) FROM PRODUCTS WHERE CATEGORY = 'Soap');

User question is  Which product achieved the highest sales in 2024?
SQL Query from Model  SELECT PRODUCT_NAME FROM PRODUCTS
                      WHERE SALES_PERCENTAGE_2024 = (SELECT MAX(SALES_PERCENTAGE_2024) FROM PRODUCTS);



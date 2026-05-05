def generate_sql(question, columns):
    q = question.lower()

    if "total" in q:
        return "SELECT SUM(amount) FROM sales"
    elif "product" in q:
        return "SELECT product FROM sales"
    else:
        return "SELECT * FROM sales"
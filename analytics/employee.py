import pandas as pd
from db import engine

def get_employee_stats():
    # Get all sales with cashier info
    query = """
        SELECT 
            s.cashierName,
            COUNT(s.id) as total_sales,
            SUM(s.total) as total_revenue,
            SUM(s.profit) as total_profit,
            HOUR(s.ts) as hour
        FROM Sale s
        GROUP BY s.cashierName, HOUR(s.ts)
        ORDER BY total_revenue DESC
    """
    df = pd.read_sql(query, engine)
    return df.to_json(orient="records")
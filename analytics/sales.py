import pandas as pd
from db import engine

def get_sales_stats():
    query = """
        SELECT 
            DATE(s.ts) as date,
            DAYNAME(s.ts) as day_name,
            COUNT(s.id) as total_transactions,
            SUM(s.total) as total_revenue,
            SUM(s.profit) as total_profit,
            s.paymentMethod
        FROM Sale s
        GROUP BY DATE(s.ts), DAYNAME(s.ts), s.paymentMethod
        ORDER BY date ASC
    """
    df = pd.read_sql(query, engine)
    return df.to_json(orient="records")
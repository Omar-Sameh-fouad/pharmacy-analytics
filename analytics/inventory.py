import pandas as pd
from db import engine

def get_inventory_stats():
    query = """
        SELECT 
            m.name,
            SUM(si.qty) as total_sold,
            SUM(si.qty * si.unitPrice) as total_revenue,
            SUM(si.qty * (si.unitPrice - si.unitCost)) as total_profit
        FROM SaleItem si
        JOIN Medicine m ON si.medicineId = m.id
        GROUP BY m.name
        ORDER BY total_revenue DESC
    """
    df = pd.read_sql(query, engine)
    
    # ABC Analysis
    df['cumulative_pct'] = df['total_revenue'].cumsum() / df['total_revenue'].sum() * 100
    df['category'] = pd.cut(df['cumulative_pct'], 
                           bins=[0, 70, 90, 100], 
                           labels=['A', 'B', 'C'])
    return df.to_json(orient="records")
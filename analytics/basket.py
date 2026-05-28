import pandas as pd
from db import engine
from itertools import combinations
from collections import Counter

def get_basket_stats():
    query = """
        SELECT 
            si.saleId,
            si.medicineName
        FROM SaleItem si
    """
    df = pd.read_sql(query, engine)
    
    # Group medicines by sale
    baskets = df.groupby('saleId')['medicineName'].apply(list)
    
    # Find pairs bought together
    pairs = Counter()
    for basket in baskets:
        if len(basket) > 1:
            for pair in combinations(sorted(basket), 2):
                pairs[pair] += 1
    
    # Convert to dataframe
    result = pd.DataFrame([
        {'medicine1': k[0], 'medicine2': k[1], 'times_bought_together': v}
        for k, v in pairs.most_common(20)
    ])
    
    if result.empty:
        return "[]"
    
    return result.to_json(orient="records")
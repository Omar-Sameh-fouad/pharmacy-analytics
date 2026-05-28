# Pharmacy Analytics Module

A data analytics dashboard built with Python & Flask that connects 
to the pharmacy's MySQL database and provides visual insights.

## Requirements
- Python 3.13+
- MySQL database (Railway)

## Setup

1. Create a virtual environment:
python -m venv venv
venv\Scripts\activate

2. Install dependencies:
pip install -r requirements.txt

3. Create a .env file:
DATABASE_URL=mysql+pymysql://your_database_url_here

4. Run the dashboard:
python app.py

5. Open browser at:
http://localhost:5000

## Analytics Modules
- Employee Performance & Heatmap
- Inventory ABC Analysis
- Sales Trends
- Market Basket Analysis
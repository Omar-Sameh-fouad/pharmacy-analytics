from db import engine

try:
    with engine.connect() as conn:
        print("✅ Connected to the database successfully!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
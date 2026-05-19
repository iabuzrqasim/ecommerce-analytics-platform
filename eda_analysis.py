import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root123@localhost/ecommerce_db')

# Load from MySQL
dataframes = {
    'orders': pd.read_sql('SELECT * FROM orders', engine),
    'customers': pd.read_sql('SELECT * FROM customers', engine),
    'order_items': pd.read_sql('SELECT * FROM order_items', engine),
    'products': pd.read_sql('SELECT * FROM products', engine),
    'sellers': pd.read_sql('SELECT * FROM sellers', engine),
}
print("="*60)
print("       E-COMMERCE DATA QUALITY REPORT")
print("="*60)

for table_name, df in dataframes.items():
    print(f"\n TABLE: {table_name.upper()}")
    print(f"   Total Rows: {len(df)}")
    print(f"   Total Columns: {len(df.columns)}")
    
    missing = df.isnull().sum()
    
    # Condition — sirf woh columns dikhao jisme missing values hain
    if missing.sum() == 0:
        print(" No missing values found!")
    else:
        print(f" Missing Values Found:")
        for col, count in missing.items():
            if count > 0:
                percentage = round((count / len(df)) * 100, 2)
                print(f" → {col}: {count} missing ({percentage}%)")

print("\n" + "="*60)
print(" REPORT COMPLETE")
print("="*60)
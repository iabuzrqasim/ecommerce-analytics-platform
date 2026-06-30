import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

# MySQL connection
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')

try:
    with engine.connect() as conn:
        print("MySQL Connected!")
except Exception as e:
    print(f"Error: {e}")
    exit()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, 'dataset') + os.sep

# Load CSV files
orders = pd.read_csv(path + 'olist_orders_dataset.csv')
customers = pd.read_csv(path + 'olist_customers_dataset.csv')
order_items = pd.read_csv(path + 'olist_order_items_dataset.csv')
products = pd.read_csv(path + 'olist_products_dataset.csv')
sellers = pd.read_csv(path + 'olist_sellers_dataset.csv')

# ================================
# DATA CLEANING
# ================================
print("\nCleaning data...")

# Orders cleaning
orders = orders.fillna({
    'order_approved_at': 'Not Approved',
    'order_delivered_carrier_date': 'Not Shipped',
    'order_delivered_customer_date': 'Not Delivered'
})

# Products cleaning
products = products.fillna({
    'product_category_name': 'Unknown',
    'product_name_lenght': 0,
    'product_description_lenght': 0,
    'product_photos_qty': 0,
    'product_weight_g': products['product_weight_g'].mean(),
    'product_length_cm': products['product_length_cm'].mean(),
    'product_height_cm': products['product_height_cm'].mean(),
    'product_width_cm': products['product_width_cm'].mean()
})

print(" Data cleaned!")

# ================================
# LOAD INTO MYSQL
# ================================
tables = {
    'orders': orders,
    'customers': customers,
    'order_items': order_items,
    'products': products,
    'sellers': sellers
}

for table, df in tables.items():
    print(f"Loading {table}...")
    df.to_sql(table, engine, if_exists='replace', index=False)
    print(f" {table} done! ({len(df)} rows)")

print("\n All clean data loaded into MySQL!")

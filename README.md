# E-Commerce CSV Project

This project loads a Brazilian e-commerce dataset into a MySQL database and includes SQL queries for sales analysis.

## Files

- `load_data.py`: Python script that reads CSV files from the local `dataset/` folder, cleans the data, and loads five tables into MySQL using SQLAlchemy.
- `eda_analysis.py`: Python script that reads those MySQL tables and prints a data quality / missing-values report for each table.
- `analysis_queries.sql`: SQL script with example analytics queries for the e-commerce dataset.

## Dataset

The project expects Olist dataset CSV files in the local `dataset/` folder next to the scripts.

Expected files used by `load_data.py`:

- `olist_orders_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`

Other files in the repository (not loaded by the current loader script):

- `olist_order_payments_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_geolocation_dataset.csv`
- `product_category_name_translation.csv`

## Setup

1. Install dependencies:

```bash
pip install pandas sqlalchemy pymysql
```

2. Configure MySQL credentials in `load_data.py` and `eda_analysis.py` if needed:

```python
engine = create_engine('mysql+pymysql://root:root123@localhost/ecommerce_db')
```

3. Ensure the `ecommerce_db` database exists in MySQL.

> Note: When you change code, update this README to keep the documentation in sync.

## Usage

Run the loader script to import the data into MySQL:

```bash
python load_data.py
```

Then run the EDA report script to inspect the loaded tables and missing values:

```bash
python eda_analysis.py
```

After loading data, execute `analysis_queries.sql` in the MySQL database to perform the sample analysis.

## Analysis examples

The SQL file includes example queries for:

- Top 10 product categories by orders
- Monthly revenue analysis
- Top 10 cities by orders
- Order status distribution
- Average order value

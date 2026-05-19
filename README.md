# E-Commerce CSV Project

This project loads a Brazilian e-commerce dataset into a MySQL database and includes SQL queries for sales analysis.

## Files

- `load_data.py`: Python script that reads CSV files and loads them into MySQL using SQLAlchemy.
- `eda_analysis.py`: Python script that loads the MySQL tables back into pandas and prints a data quality / missing-values report for each table.
- `analysis_queries.sql`: SQL script with example analytics queries for the e-commerce dataset.

## Dataset

The project expects Olist dataset CSV files in the local path:

`C:/Users/SAEECOMPUTER/Downloads/ecommerce_db/`

Expected files:

- `olist_orders_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`

## Setup

1. Install dependencies:

```bash
pip install pandas sqlalchemy pymysql
```

2. Configure MySQL credentials in `load_data.py`:

```python
engine = create_engine('mysql+pymysql://root:root123@localhost/ecommerce_db')
```

3. Ensure the `ecommerce_db` database exists in MySQL.

## Usage

Run the loader script to import the data:

```bash
python load_data.py
```

Use the EDA script to inspect loaded tables and missing values:

```bash
python eda_analysis.py
```

Then execute `analysis_queries.sql` in the MySQL database to perform the sample analysis.

## Analysis examples

The SQL file includes example queries for:

- Top 10 product categories by orders
- Monthly revenue analysis
- Top 10 cities by orders
- Order status distribution
- Average order value

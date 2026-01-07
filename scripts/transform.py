import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# --------------------------
# STEP 1: Load staging tables
# --------------------------

stg_customers = pd.read_sql("SELECT * FROM stg_customers", engine)
stg_products = pd.read_sql("SELECT * FROM stg_products", engine)
stg_orders = pd.read_sql("SELECT * FROM stg_orders", engine)
stg_order_items = pd.read_sql("SELECT * FROM stg_order_items", engine)

# --------------------------
# STEP 2: Transform Dimensions
# --------------------------

# Customers dimension
dim_customers = stg_customers.drop_duplicates(subset=["customer_id"])
dim_customers.to_sql("dim_customers", engine, if_exists="replace", index=False)

# Products dimension
dim_products = stg_products.drop_duplicates(subset=["product_id"])
dim_products.to_sql("dim_products", engine, if_exists="replace", index=False)

# Dates dimension
all_dates = pd.to_datetime(stg_orders['order_date']).drop_duplicates()
dim_dates = pd.DataFrame({
    'date_id': all_dates,
    'year': all_dates.dt.year,
    'month': all_dates.dt.month,
    'day': all_dates.dt.day
})
dim_dates.to_sql("dim_dates", engine, if_exists="replace", index=False)

# --------------------------
# STEP 3: Transform Fact Table
# --------------------------

# Merge orders with order_items
fact_sales = stg_order_items.merge(
    stg_orders,
    how='left',
    on='order_id'
).merge(
    stg_products,
    how='left',
    on='product_id'
)

# Calculate revenue
fact_sales['revenue'] = fact_sales['quantity'] * fact_sales['unit_price'] * (1 - fact_sales['discount'])

# Map date_id
fact_sales['date_id'] = pd.to_datetime(fact_sales['order_date'])

# Keep only required columns
fact_sales_final = fact_sales[['order_id', 'customer_id', 'product_id', 'date_id', 'quantity', 'revenue', 'discount']]

# Load into fact_sales table
fact_sales_final.to_sql("fact_sales", engine, if_exists="replace", index=False)

print("Dimension and Fact tables populated successfully!")

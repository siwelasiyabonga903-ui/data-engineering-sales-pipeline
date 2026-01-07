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

# File paths
base_path = "data/raw"

files = {
    "customers.csv": "stg_customers",
    "products.csv": "stg_products",
    "orders.csv": "stg_orders",
    "order_items.csv": "stg_order_items"
}

for file, table in files.items():
    df = pd.read_csv(f"{base_path}/{file}")
    df.to_sql(table, engine, if_exists="append", index=False)
    print(f"Loaded {file} into {table}")

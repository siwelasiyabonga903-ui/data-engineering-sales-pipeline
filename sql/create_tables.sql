-- STAGING TABLES (RAW DATA)

CREATE TABLE IF NOT EXISTS stg_customers (
    customer_id INT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    region VARCHAR(50),
    created_at DATE
);

CREATE TABLE IF NOT EXISTS stg_products (
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS stg_orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    payment_method VARCHAR(50),
    discount NUMERIC(5,2)
);

CREATE TABLE IF NOT EXISTS stg_order_items (
    order_item_id INT,
    order_id INT,
    product_id INT,
    quantity INT
);

-- DIMENSION TABLES

CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS dim_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS dim_dates (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

-- FACT TABLE

CREATE TABLE IF NOT EXISTS fact_sales (
    sales_id SERIAL PRIMARY KEY,
    order_id INT,
    customer_id INT,
    product_id INT,
    date_id DATE,
    quantity INT,
    revenue NUMERIC(12,2),
    discount NUMERIC(5,2)
);

 End-to-End Data Engineering Sales Pipeline

 Project Overview
This project demonstrates a complete end-to-end data engineering pipeline designed to ingest raw business data, transform it into a structured data warehouse, and expose it for analytics and reporting using Power BI.

The pipeline follows industry best practices including staging layers, star schema design, and separation of ingestion and transformation logic.


 Architecture
- Raw Layer: Source CSV files representing operational systems
- Staging Layer: Raw data loaded into PostgreSQL without business logic
- Transformation Layer: Data cleaning, deduplication, and enrichment
- Warehouse Layer: Optimized fact and dimension tables
- Analytics Layer: Power BI dashboards connected to PostgreSQL

 Technology Stack
- Programming Language: Python
- Data Processing: Pandas
- Database: PostgreSQL
- ETL & Database Connectivity: SQLAlchemy, psycopg2
- Business Intelligence: Power BI
- Version Control: Git, GitHub
- Development Environment: VS Code

 Project Structure


 Data Warehouse Design (Star Schema)

 Fact Table
- order_id
- customer_id
- product_id
- date_id
- quantity
- revenue
- discount

Dimension Tables
- dim_customers – customer details and region
- dim_products – product and category information
- dim_dates – date attributes for time-based analysis
![Star Schema Model](images/powerbi_data_model.png)



     ETL Workflow

 Extract
- Raw CSV files are extracted using Python and Pandas.

 Transform
- Data is cleaned and deduplicated
- Business logic is applied to calculate revenue
- Dates are standardized and enriched
- Dimension and fact tables are created

 Load
- Transformed data is loaded into PostgreSQL warehouse tables
- Tables are optimized for analytics and reporting


 Analytics & Reporting
Power BI connects directly to the PostgreSQL data warehouse to provide:
- Revenue by product category
- Revenue by customer region
- Monthly sales trends
 Sales Performance Dashboard
![Power BI Dashboard](images/powerbi_dashboard.png)


The star schema enables fast query performance and clean visual modeling.


   Key Learning Outcomes

- Built a full data pipeline from ingestion to analytics
- Designed a star schema data warehouse
- Applied ETL best practices
- Integrated PostgreSQL with Power BI
# Superstore Sales Analysis

An end-to-end sales data pipeline built in Python using the Superstore dataset (~10,000 records).

The project demonstrates a complete ETL workflow, including data extraction, cleaning, transformation, loading into SQLite, SQL-based analysis, logging, and error handling.

---

Source: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

The dataset contains information about:
- Orders
- Customers
- Products
- Sales
- Profit
- Discounts
- Shipping information

---

## Features

# Data Extraction
- Reads raw sales data from CSV files
- Validates input files before processing

# Data Cleaning
- Removes duplicate records
- tandardizes column names
- Converts data types
- Handles missing values

# Feature Engineering

Creates additional business metrics:

- Delivery days
- Order year
- Order month
- Order month name
- Order quarter
- Profit margin
- Profitability flag

# Data Storage
- Saves cleaned data to CSV
- Loads processed data into SQLite

# SQL Analytics

Performs automated analysis:

- Sales by region
- Profit by category
- Top-selling products
- Monthly sales trends
- Average delivery time

# Logging & Error Handling
- Pipeline execution logging
- Exception handling
- SQLite error handling
- File validation


---

## Tech Stack

- Python
- pandas
- SQLite

---

## Project Structure

The project architecture:

```bash
superstore_sales_analysis/ 
├── data/ 
│ ├── raw/ 
│ │ └── sales.csv 
│ │ 
│ ├── cleaned/ 
│ │ └── sales_cleaned.csv 
│ │ 
│ ├── analysis/ 
│ │ ├── sales_by_region.csv 
│ │ ├── profit_by_category.csv 
│ │ ├── top_products.csv 
│ │ ├── monthly_sales.csv 
│ │ └── avg_delivery_time.csv 
│ │ 
│ └── sales.db 
│ 
├── logs/ 
│ └── pipeline.log 
│ 
├── scripts/ 
│ ├── extract.py 
│ ├── transform.py 
│ ├── load.py 
│ ├── load_sqlite.py 
│ ├── analyze.py 
│ └── logger.py 
│ 
├── main.py 
├── requirements.txt 
└── README.md
```

---

## Installation & Configuration

Clone the repository:

```bash
git clone https://github.com/BaranIga/superstore-sales-analysis.git
cd superstore_sales_analysis
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows:

```
venv\Scripts\activate
```

Linux / macOS:

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```


---


## Usage

### Run the ETL pipeline

```bash
python main.py
```

### Pipeline Overview

Raw CSV 
  ↓ 
Data Extraction 
  ↓ 
Data Cleaning 
  ↓ 
Feature Engineering 
  ↓ 
Cleaned CSV 
  ↓ 
SQLite Database 
  ↓ 
SQL Analysis 
  ↓ 
Analysis CSV Files

### Notes

- Analysis results are automatically exported to the data/analysis directory
- Logs are stored in logs/pipeline.log
- SQLite database is generated automatically

---

## Architecture

saless.csv -> Extract -> Transform -> Clean CSV -> SQLite -> SQL Analysis -> CSV Reports

## Example Outputs

Generated files:
- `data/cleaned/sales_cleaned.csv`
- `data/sales.db`
- `data/analysis/` 


---

## Future Improvements

- Power BI dashboard integration


## Author

Created by Iga Baran
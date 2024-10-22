import os
from dotenv import load_dotenv
import mysql.connector
from faker import Faker
import csv
from datetime import datetime

load_dotenv()

db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_port = os.getenv('DB_PORT')

conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    port=db_port
)

COUNTRIES_COUNT = 227
CORPORATIONS_COUNT = 8297
EVENTS_COUNT = 1046
NEWS_ARTICLES_COUNT = 505956

cursor = conn.cursor()
fake = Faker()

def handle_numeric_value(value, is_decimal=False):
    """Safely parse numeric values with optional decimal conversion."""
    if value is None or value.strip() == "":
        return None
    try:
        if is_decimal:
            return float(value.replace(',', '.'))
        else:
            return int(value.replace(',', ''))
    except ValueError:
        return None

def parse_scientific_notation(value):
    """Converts scientific notation to float, and normalizes large values like trillions."""
    try:
        num = float(value)
        return round(num, 2)
    except (ValueError, TypeError):
        return None

def parse_event_date(year, month, day):
    """Parses dates and handles BC years and zero-padded year formats."""
    try:
        if year == '0':
            year = '0001'

        if len(year) < 4:
            year = year.zfill(4)
        
        month = month if month.isdigit() else "01" 
        day = day if day.isdigit() else "01"
        
        date_str = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except Exception as e:
        print(f"Invalid date format: {year}-{month}-{day} ({e})")
        return None

def insert_countries_from_csv(csv_file):
    """Insert countries from CSV into the Countries table."""
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            literacy = handle_numeric_value(row['Literacy (%)'], is_decimal=True)
            gdp_per_capita = handle_numeric_value(row['GDP ($ per capita)'], is_decimal=True)
            population = handle_numeric_value(row['Population'])
            cursor.execute("""
                INSERT INTO Countries (country_name, region, population, gdp_per_capita, literacy)
                VALUES (%s, %s, %s, %s, %s)
            """, (row['Country'].strip(), row['Region'].strip(), population, gdp_per_capita, literacy))
        conn.commit()

def insert_corporations_from_csv(csv_file):
    """Insert corporations from CSV into the Corporations table."""
    with open(csv_file, mode='r', encoding='utf-8', errors='replace') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = {k.strip(): v for k, v in row.items()}
            
            total_assets = parse_scientific_notation(row.get('total_assets (USD) in Trillion'))

            share_price = handle_numeric_value(row.get('share price (USD)'), is_decimal=True)

            cursor.execute("""
                INSERT INTO Corporations (name, stock_symbol, total_assets, share_price, country_id)
                VALUES (%s, %s, %s, %s, (SELECT country_id FROM Countries WHERE country_name=%s))
            """, (row.get('company').strip(), row.get('stock Symbol').strip(), total_assets, share_price, row.get('company origin').strip()))
        conn.commit()

def insert_events_from_csv(csv_file):
    """Insert events from CSV into the Events table."""
    with open(csv_file, mode='r', encoding='utf-8', errors='replace') as file:
        reader = csv.DictReader(file)
        for row in reader:
            event_date = parse_event_date(row['Year'], row['Month'], row['Date'])
            if event_date is None:
                continue

            cursor.execute("""
                INSERT INTO Events (event_name, event_date, event_type, country_id, impact)
                VALUES (%s, %s, %s, (SELECT country_id FROM Countries WHERE country_name=%s), %s)
            """, (row['Name of Incident'].strip(), event_date, row['Type of Event'].strip(), row['Country'].strip(), row['Impact'].strip()))
        conn.commit()

def insert_news_articles_from_csv(csv_file):
    """Insert news articles from CSV into the NewsArticles table."""
    with open(csv_file, mode='r', encoding='utf-8-sig', errors='replace') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row['title'].strip()
            up_votes = handle_numeric_value(row['up_votes'])

            cursor.execute("""
                INSERT INTO NewsArticles (title, date_created, up_votes, theory_id)
                VALUES (%s, %s, %s, %s, NULL)
            """, (title, row['date_created'], up_votes))
        conn.commit()

# Insert data from CSVs
insert_events_from_csv('real_tables/events.csv')
insert_corporations_from_csv('real_tables/corporations.csv')
insert_countries_from_csv('real_tables/countries.csv')
insert_news_articles_from_csv('real_tables/worldnews.csv')

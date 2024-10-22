import csv
from initialization._database_config import conn, cursor
from initialization._data_parsers import handle_numeric_value, parse_scientific_notation, parse_event_date
from initialization._db_helpers import get_country_id

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
            country_id = get_country_id(row.get('company origin').strip())
            if country_id is None:
                continue
            cursor.execute("""
                INSERT INTO Corporations (name, stock_symbol, total_assets, share_price, country_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (row.get('company').strip(), row.get('stock Symbol').strip(), total_assets, share_price, country_id))
        conn.commit()

def insert_events_from_csv(csv_file):
    """Insert events from CSV into the Events table."""
    with open(csv_file, mode='r', encoding='utf-8', errors='replace') as file:
        reader = csv.DictReader(file)
        for row in reader:
            event_date = parse_event_date(row['Year'], row['Month'], row['Date'])
            if event_date is None:
                continue
            country_id = get_country_id(row['Country'].strip())
            if country_id is None:
                continue
            cursor.execute("""
                INSERT INTO Events (event_name, event_date, event_type, country_id, impact, responsible, outcome)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (row['Name of Incident'].strip(), event_date, row['Type of Event'].strip(), country_id, row['Impact'].strip(), row['Important Person/Group Responsible'].strip(), row['Outcome'].strip()))
        conn.commit()

def insert_news_articles_from_csv(csv_file):
    """Insert news articles from CSV into the NewsArticles table."""
    with open(csv_file, mode='r', encoding='utf-8-sig', errors='replace') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row['title'].strip()
            if len(title) > 255:
                title = title[:255]
            up_votes = handle_numeric_value(row['up_votes'])

            cursor.execute("""
                INSERT INTO NewsArticles (title, date_created, up_votes)
                VALUES (%s, %s, %s)
            """, (title, row['date_created'], up_votes))
        conn.commit()


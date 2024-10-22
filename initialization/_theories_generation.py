import random
from faker import Faker
from _database_config import conn, cursor

def get_table_record_count(table_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]

COUNTRY_RECORD_COUNT = get_table_record_count('Countries')
CORPORATION_RECORD_COUNT = get_table_record_count('Corporations')
EVENT_RECORD_COUNT = get_table_record_count('Events')
NEWS_ARTICLE_RECORD_COUNT = get_table_record_count('NewsArticles')

fake = Faker()

def get_random_id(max_id):
    return random.randint(1, max_id) if max_id > 0 else None

def insert_conspiracy_theory():
    """Generate and insert a new conspiracy theory into the ConspiracyTheories table."""
    
    country_id = get_random_id(COUNTRY_RECORD_COUNT)
    corporation_id = get_random_id(CORPORATION_RECORD_COUNT)
    event_id = get_random_id(EVENT_RECORD_COUNT)
    article_id = get_random_id(NEWS_ARTICLE_RECORD_COUNT)
    
    title = fake.catch_phrase()
    description = fake.paragraph(nb_sentences=5)
    creation_date = fake.date_this_century()

    cursor.execute("""
        INSERT INTO ConspiracyTheories (title, description, creation_date, country_id, corporation_id, event_id, article_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (title, description, creation_date, country_id, corporation_id, event_id, article_id))

    conn.commit()
    # print(f"Inserted theory: {title} with country_id {country_id}, corporation_id {corporation_id}, event_id {event_id}, article_id {article_id}")

def generate_conspiracy_theories(count=10):
    for _ in range(count):
        insert_conspiracy_theory()

generate_conspiracy_theories(880)

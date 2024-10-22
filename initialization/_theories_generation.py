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

A_FEW = 5
fake = Faker()

used_country_pairs = set()      # Track (theory_id, country_id)     (many-to-many)
used_corporation_pairs = set()  # Track (theory_id, corporation_id) (many-to-many)
used_article_pairs = set()      # Track (theory_id, article_id)     (one-to-many)

def insert_conspiracy_theory():
    """Insert a new conspiracy theory and link it to countries, corporations, and articles."""
    title = fake.catch_phrase()
    description = fake.paragraph(nb_sentences=5)
    creation_date = fake.date()
    event_id = random.randint(1, EVENT_RECORD_COUNT)

    cursor.execute("""
        INSERT INTO ConspiracyTheories (title, description, creation_date, event_id)
        VALUES (%s, %s, %s, %s)
    """, (title, description, creation_date, event_id))
    theory_id = cursor.lastrowid

    for _ in range(random.randint(1, A_FEW)):
        country_id = random.randint(1, COUNTRY_RECORD_COUNT)
        if country_id and (theory_id, country_id) not in used_country_pairs:
            cursor.execute("""
                INSERT INTO TheoryCountries (theory_id, country_id)
                VALUES (%s, %s)
            """, (theory_id, country_id))
            used_country_pairs.add((theory_id, country_id))

    for _ in range(random.randint(1, A_FEW)):
        corporation_id = random.randint(1, CORPORATION_RECORD_COUNT)
        if corporation_id and (theory_id, corporation_id) not in used_corporation_pairs:
            cursor.execute("""
                INSERT INTO TheoryCorporations (theory_id, corporation_id)
                VALUES (%s, %s)
            """, (theory_id, corporation_id))
            used_corporation_pairs.add((theory_id, corporation_id))

    for _ in range(random.randint(1, A_FEW)):
        article_id = random.randint(1, NEWS_ARTICLE_RECORD_COUNT)
        if article_id and theory_id not in used_article_pairs:
            cursor.execute("""
                INSERT INTO TheoryArticles (theory_id, article_id)
                VALUES (%s, %s)
            """, (theory_id, article_id))
            used_article_pairs.add(theory_id)

    conn.commit()

def generate_conspiracy_theories(count=10):
    """Generate and insert a specified number of conspiracy theories."""
    for _ in range(count):
        insert_conspiracy_theory()

generate_conspiracy_theories(2000)

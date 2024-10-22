
def generate_fake_theories(num_theories=100):
    for _ in range(num_theories):
        country_id = fake.random_int(min=1, max=227)
        corporation_id = fake.random_int(min=1, max=8391)
        event_id = fake.random_int(min=1, max=1081)
        title = fake.catch_phrase()
        description = fake.text(max_nb_chars=500)
        creation_date = fake.date_this_decade()
        cursor.execute("""
            INSERT INTO ConspiracyTheories (title, description, creation_date, country_id, corporation_id, event_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (title, description, creation_date, country_id, corporation_id, event_id))

    conn.commit()

generate_fake_theories(500)
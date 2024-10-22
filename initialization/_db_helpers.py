from _database_config import cursor

def get_country_id(country_name):
    """Fetch country_id based on country name."""
    cursor.execute("SELECT country_id FROM Countries WHERE country_name = %s", (country_name,))
    result = cursor.fetchone()
    return result[0] if result else None

def get_event_id(event_name, event_date):
    """Fetch event_id based on event name and date."""
    cursor.execute("SELECT event_id FROM Events WHERE event_name = %s AND event_date = %s", (event_name, event_date))
    result = cursor.fetchone()
    return result[0] if result else None

def get_corporation_id(corporation_name):
    """Fetch corporation_id based on corporation name."""
    cursor.execute("SELECT corporation_id FROM Corporations WHERE name = %s", (corporation_name,))
    result = cursor.fetchone()
    return result[0] if result else None

from _data_inserters import insert_events_from_csv, insert_corporations_from_csv, insert_countries_from_csv, insert_news_articles_from_csv

# Insert data from CSVs
insert_countries_from_csv('real_tables/countries.csv')
insert_news_articles_from_csv('real_tables/worldnews.csv')
insert_corporations_from_csv('real_tables/corporations.csv')
insert_events_from_csv('real_tables/events.csv')

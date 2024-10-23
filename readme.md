# Conspiracy Chronicles Database 🕵️‍♂️💼

Welcome to the **Conspiracy Chronicles Database**, where reality meets imagination in a whirlwind of intrigue and data! 🌍✨ This highly operational database is your gateway to a world of conspiracy theories, woven intricately with real-world facts about countries, corporations, news, and events. Here, we embrace the wildest of theories while keeping our feet firmly planted in reality—because everything you find here is real... except the theories! 🎭🔍

## Why This Database is a Game Changer

### **1. A Treasure Trove of Information**

Our database integrates rich datasets that allow you to explore a plethora of facts and figures:

- **Countries**: Get to know your nation better—population, GDP, literacy rates, and more!
- **Corporations**: Dive into the financial depths of businesses—discover their assets and stock prices!
- **News Articles**: Stay updated with the latest and greatest stories that shape our world.
- **Events**: Examine significant events that have rocked the globe and their lasting impacts.

### **2. Unleash Your Inner Detective** 🔎

Curious about the patterns that link corporations to conspiracy theories? Or perhaps you want to analyze how events in different countries shape narratives? With our expertly crafted tables and relationships, you can do just that! Each conspiracy theory is intricately connected to various entities, providing a rich tapestry for analysis.

### **3. Optimized for High Volume Queries**

Whether you're a data analyst or just a conspiracy enthusiast, this database is designed to handle high-volume queries with ease. Say goodbye to slow load times and hello to lightning-fast responses as you dig deep into the shadows of information.

### **4. Generate Your Own Conspiracies!** 🎉

Thanks to the magic of Python’s Faker library, you can populate our database with a multitude of conspiracy theories. Have fun creating narratives that intertwine with real-world events, and who knows? You might just stumble upon the next big theory!

### **5. Use Cases Galore**

- **Research**: Perfect for academic projects or curious minds wanting to explore socio-political dynamics.
- **Data Analysis**: Analyze correlations between corporate behaviors and conspiracy narratives.
- **Content Creation**: Fuel your next story or blog post with data-backed insights from real-world connections.

### Database Schema

This is the database schema for the project:

```mermaid
erDiagram
    COUNTRIES {
        INT country_id PK
        VARCHAR(255) country_name
        VARCHAR(255) region
        INT population
        INT gdp_per_capita
        DECIMAL literacy
    }

    NEWS_ARTICLES {
        INT article_id PK
        VARCHAR(255) title
        DATE date_created
        INT up_votes
    }

    CORPORATIONS {
        INT corporation_id PK
        VARCHAR(255) name
        VARCHAR(50) stock_symbol
        DECIMAL total_assets
        DECIMAL share_price
        INT country_id FK
    }

    EVENTS {
        INT event_id PK
        VARCHAR(255) event_name
        DATE event_date
        VARCHAR(255) event_type
        INT country_id FK
        VARCHAR(255) impact
        VARCHAR(255) responsible
        ENUM(Mixed-Positive-Negative-Ongoing) outcome
    }

    CONSPIRACY_THEORIES {
        INT theory_id PK
        VARCHAR(255) title
        TEXT description
        DATE creation_date
        INT event_id FK
    }

    THEORY_ARTICLES {
        INT theory_id PK
        INT article_id PK
    }

    THEORY_CORPORATIONS {
        INT theory_id PK
        INT corporation_id PK
    }

    THEORY_COUNTRIES {
        INT theory_id PK
        INT country_id PK
    }

    COUNTRIES ||--o{ CORPORATIONS : "is home to"
    COUNTRIES ||--o{ EVENTS : "hosts"
    EVENTS ||--o| CONSPIRACY_THEORIES : "involves"
    CONSPIRACY_THEORIES ||--o{ THEORY_ARTICLES : "mentions"
    CONSPIRACY_THEORIES ||--o{ THEORY_CORPORATIONS : "targets"
    CONSPIRACY_THEORIES ||--o{ THEORY_COUNTRIES : "impacts"
    NEWS_ARTICLES ||--o{ THEORY_ARTICLES : "reports"
    CORPORATIONS ||--o{ THEORY_CORPORATIONS : "is mentioned in"
    COUNTRIES ||--o{ THEORY_COUNTRIES : "is implicated in"

```
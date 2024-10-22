CREATE TABLE Countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(255) NOT NULL,
    region VARCHAR(255),
    population INT,
    gdp_per_capita INT,
    literacy DECIMAL(5,2)
);

CREATE TABLE Corporations (
    corporation_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    stock_symbol VARCHAR(50),
    total_assets DECIMAL(20,2),
    share_price DECIMAL(10,2),
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id)
);

CREATE TABLE Events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255),
    event_date DATE,
    event_type VARCHAR(255),
    country_id INT,
    impact VARCHAR(255),
    responsible VARCHAR(255), -- Important Person/Group Responsible
    outcome ENUM('Mixed', 'Positive', 'Negative') NOT NULL,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id)
);

CREATE TABLE ConspiracyTheories (
    theory_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    creation_date DATE,
    country_id INT,
    corporation_id INT,
    event_id INT,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id),
    FOREIGN KEY (corporation_id) REFERENCES Corporations(corporation_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE NewsArticles (
    article_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    date_created DATE,
    up_votes INT,
    theory_id INT,
    FOREIGN KEY (theory_id) REFERENCES ConspiracyTheories(theory_id)
);

CREATE TABLE Countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(255) NOT NULL UNIQUE,
    region VARCHAR(255),
    population INT CHECK (population >= 0),                         -- Non-negative population
    gdp_per_capita INT CHECK (gdp_per_capita >= 0),                 -- Non-negative GDP per capita
    literacy DECIMAL(5,2) CHECK (literacy >= 0 AND literacy <= 100) -- Literacy percentage
);

CREATE TABLE NewsArticles (
    article_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    date_created DATE NOT NULL,
    up_votes INT DEFAULT 0 CHECK (up_votes >= 0)    -- Non-negative up votes
);

CREATE TABLE Corporations (
    corporation_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    stock_symbol VARCHAR(50) UNIQUE,                                            -- Unique stock symbol
    total_assets DECIMAL(20,2) CHECK (total_assets >= 0),                       -- Non-negative total assets
    share_price DECIMAL(10,2) CHECK (share_price >= 0),                         -- Non-negative share price
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id) ON DELETE SET NULL
);

CREATE TABLE Events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    event_type VARCHAR(255),
    country_id INT,
    impact VARCHAR(255),
    responsible VARCHAR(255),
    outcome ENUM('Mixed', 'Positive', 'Negative', 'Ongoing') NOT NULL,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id) ON DELETE SET NULL
);

CREATE TABLE ConspiracyTheories (
    theory_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    creation_date DATE NOT NULL,
    event_id INT,
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE SET NULL
);

-- one-to-many relationship between ConspiracyTheories and NewsArticles
CREATE TABLE TheoryArticles (
    theory_id INT,
    article_id INT,
    PRIMARY KEY (theory_id, article_id),
    FOREIGN KEY (theory_id) REFERENCES ConspiracyTheories(theory_id) ON DELETE CASCADE,
    FOREIGN KEY (article_id) REFERENCES NewsArticles(article_id) ON DELETE CASCADE
);

-- one-to-many relationship between ConspiracyTheories and Corporations
CREATE TABLE TheoryCorporations (
    theory_id INT,
    corporation_id INT,
    PRIMARY KEY (theory_id, corporation_id),
    FOREIGN KEY (theory_id) REFERENCES ConspiracyTheories(theory_id) ON DELETE CASCADE,
    FOREIGN KEY (corporation_id) REFERENCES Corporations(corporation_id) ON DELETE CASCADE
);

-- many-to-many relationship between ConspiracyTheories and Countries
CREATE TABLE TheoryCountries (
    theory_id INT,
    country_id INT,
    PRIMARY KEY (theory_id, country_id),
    FOREIGN KEY (theory_id) REFERENCES ConspiracyTheories(theory_id) ON DELETE CASCADE,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id) ON DELETE CASCADE
);

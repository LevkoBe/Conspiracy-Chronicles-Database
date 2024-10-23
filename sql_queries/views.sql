CREATE VIEW CountryConspiracyImpact AS
SELECT 
    c.country_name,
    ct.title AS conspiracy_title,
    e.event_name,
    e.event_date,
    e.impact
FROM 
    Countries c
JOIN 
    TheoryCountries tc ON c.country_id = tc.country_id
JOIN 
    ConspiracyTheories ct ON tc.theory_id = ct.theory_id
JOIN 
    Events e ON ct.event_id = e.event_id;

CREATE VIEW NewsConspiracyArticles AS
SELECT 
    na.title AS article_title,
    na.date_created,
    ct.title AS conspiracy_title,
    ct.description
FROM 
    NewsArticles na
JOIN 
    TheoryArticles ta ON na.article_id = ta.article_id
JOIN 
    ConspiracyTheories ct ON ta.theory_id = ct.theory_id;

SELECT *
FROM CountryConspiracyImpact
WHERE country_name = 'Albania';

SELECT *
FROM NewsConspiracyArticles
WHERE conspiracy_title = 'Synergized multimedia capacity';

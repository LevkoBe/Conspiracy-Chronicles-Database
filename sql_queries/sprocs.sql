DELIMITER //

CREATE PROCEDURE GetTheoryNewsArticles (
    IN p_theory_id INT
)
BEGIN
    SELECT na.title, na.date_created, na.up_votes
    FROM NewsArticles na
    JOIN TheoryArticles ta ON na.article_id = ta.article_id
    WHERE ta.theory_id = p_theory_id;
END //


CREATE PROCEDURE GetTheoriesByCorporation(
    IN corporationName VARCHAR(255)
)
BEGIN
    SELECT ct.title, ct.description, ct.creation_date
    FROM ConspiracyTheories ct
    JOIN TheoryCorporations tc ON ct.theory_id = tc.theory_id
    JOIN Corporations c ON tc.corporation_id = c.corporation_id
    WHERE c.name = corporationName;
END //

DELIMITER ;

CALL GetTheoryNewsArticles(1);

CALL GetTheoriesByCorporation('China Construction Bank');
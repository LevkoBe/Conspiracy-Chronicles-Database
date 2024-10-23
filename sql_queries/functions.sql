CREATE FUNCTION TotalUpVotesForTheory(theoryId INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total_votes INT;
    
    SELECT SUM(na.up_votes) INTO total_votes
    FROM NewsArticles na
    JOIN TheoryArticles ta ON na.article_id = ta.article_id
    WHERE ta.theory_id = theoryId;
    
    RETURN total_votes;
END;

CREATE FUNCTION CountTheoriesForCorporation(corporationId INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE theory_count INT;
    
    SELECT COUNT(1) INTO theory_count
    FROM TheoryCorporations
    WHERE corporation_id = corporationId;
    
    RETURN theory_count;
END;

SELECT TotalUpVotesForTheory(1) AS total_upvotes;
SELECT CountTheoriesForCorporation(3) AS theory_count;
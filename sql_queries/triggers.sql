CREATE TRIGGER Update_Corporation_Assets_After_Article_Insert
AFTER INSERT ON NewsArticles
FOR EACH ROW
BEGIN
    UPDATE Corporations
    SET total_assets = total_assets + 10000
    WHERE corporation_id IN (
        SELECT corporation_id
        FROM TheoryCorporations
        WHERE theory_id IN (
            SELECT theory_id
            FROM TheoryArticles
            WHERE article_id = NEW.article_id
        )
    );
END;

CREATE TRIGGER Append_Impact_Note_After_Outcome_Update
AFTER UPDATE ON Events
FOR EACH ROW
BEGIN
    IF OLD.outcome != NEW.outcome THEN
        UPDATE Events
        SET impact = CONCAT(impact, ' (Outcome changed to: ', NEW.outcome, ')')
        WHERE event_id = NEW.event_id;
    END IF;
END;

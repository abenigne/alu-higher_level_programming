-- lists the number of records for each score, sorted by count (descending)
SELECT score, COUNT(*) AS number FROM second_table
    GROUP BY score ORDER BY number DESC;

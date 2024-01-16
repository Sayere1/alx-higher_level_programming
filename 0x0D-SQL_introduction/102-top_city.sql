-- script that displays top 3 cities temp during July n August ordered by temp(descending)
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month`
BETWEEN 7 AND 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;

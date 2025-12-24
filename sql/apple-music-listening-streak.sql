-- Context: You are working on the Apple Music Data Engineering team. The product team wants to identify "Super Fans" to target with a special promotion. A "Super Fan" is defined as a user who has listened to music for at least 3 consecutive days.

-- The Data: You have a table named listening_history that logs every song played by a user.
-- user_id (integer)
-- song_id (integer)
-- event_date (date)

-- The Challenge: Write a SQL query to identify all users who have a listening streak of 3 or more consecutive days. Your output should look like this: user_id | streak_start_date | streak_end_date | streak_length_days


-- Solution --

WITH unique_date AS (
	SELECT DISTINCT
		user_id,
		event_date
	FROM
		listening_history

),
groups AS (
	SELECT
		user_id,
		event_date,
		DATE_ADD(event_date, INTERVAL - DENSE_RANK() OVER (PARTITION BY user_id, ORDER BY event_date) DAY) AS group_id
	FROM
		unique_date
)


SELECT
	user_id,
	MIN(event_date) AS streak_start_date,
	MAX(event_date) AS streak_end_date,
	COUNT(*) AS streak_length_days
FROM
	groups
GROUP BY
	user_id,
	group_id
HAVING
	COUNT(*) > 3
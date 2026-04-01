-- SELECT
--     contest_id,
--     ROUND(COUNT(*) * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage
-- FROM Register AS r
-- GROUP BY
--     r.contest_id
-- ORDER BY
--     percentage DESC,
--     contest_id ASC;

SELECT
    r.contest_id,
    ROUND(
        COUNT(DISTINCT r.user_id) * 100.0 / COUNT(DISTINCT u.user_id),
        2
    ) AS percentage
FROM Register AS r
CROSS JOIN Users AS u
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id;
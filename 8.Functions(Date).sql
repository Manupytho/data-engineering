-- Date Functions in MySQL

-- Introduction
-- Date functions in MySQL are used to perform operations on date and time values.
-- They allow to manipulate the query date and time data effectively.

-- Example 1: Using NOW() to Get the Current Date and Time

-- Query: Retrieve the current date and time.
SELECT NOW() AS current_datetime;

-- Explanation:
-- NOW() returns the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.

-- Example 2: Using CURDATE() to Get the Current Date

-- Query: Retrieve the current date.
SELECT CURDATE() AS current_date;

-- Explanation:
-- CURDATE() returns the current date in the format 'YYYY-MM-DD'.
-- It does not include the time component.

-- Example 3: Using DATE_ADD() to Add a Time Interval to a Date

-- Query: Add 10 days to a specific date.
SELECT DATE_ADD('2024-01-01', INTERVAL 10 DAY) AS new_date;

-- Explanation:
-- DATE_ADD(date, INTERVAL n unit) adds an interval of 'n' units to the specified date.
-- In this case, 10 days are added to '2024-01-01', resulting in '2024-01-11'.

-- Example 4: Using DATE_SUB() to Subtract a Time Interval from a Date

-- Query: Subtract 1 month from a specific date.
SELECT DATE_SUB('2024-01-01', INTERVAL 1 MONTH) AS new_date;

-- Explanation:
-- DATE_SUB(date, INTERVAL n unit) subtracts an interval of 'n' units from the specified date.
-- In this case, 1 month is subtracted from '2024-01-01', resulting in '2023-12-01'.

-- Example 5: Using DATEDIFF() to Calculate the Difference Between Two Dates

-- Query: Calculate the number of days between two dates.
SELECT DATEDIFF('2024-01-01', '2023-12-01') AS days_difference;

-- Explanation:
-- DATEDIFF(date1, date2) returns the number of days between 'date1' and 'date2'.
-- In this case, it calculates the number of days between '2023-12-01' and '2024-01-01', resulting in 31.

-- Example 6: Using DATE_FORMAT() to Format a Date

-- Query: Format a date using a specific format string.
SELECT DATE_FORMAT('2024-01-01', '%M %d, %Y. %W') AS formatted_date;

-- Explanation:
-- DATE_FORMAT(date, format) formats a date according to the specified format string.
-- In this case, '%W, %M %d, %Y' formats the date as 'Monday, January 01, 2024'.

-- Example 7: Using YEAR() to Extract the Year from a Date

-- Query: Extract the year from a date.
SELECT (year('2024-01-01')) AS year_extracted;

-- Explanation:
-- YEAR(date) extracts the year part from the specified date.
-- In this case, it returns 2024.

-- Example 8: Using MONTH() to Extract the Month from a Date

-- Query: Extract the month from a date.
SELECT MONTH('2024-01-01') AS month_extracted;

-- Explanation:
-- MONTH(date) extracts the month part from the specified date.
-- In this case, it returns 1 for January.

-- Example 9: Using DAY() to Extract the Day of the Month

-- Query: Extract the day of the month from a date.
SELECT DAY('2024-01-01') AS day_extracted;

-- Explanation:
-- DAY(date) extracts the day of the month from the specified date.
-- In this case, it returns 1.

-- Example 10: Using WEEKDAY() to Get the Day of the Week

-- Query: Get the index of the weekday for a date.
SELECT WEEKDAY('2024-01-01') AS weekday_index;

-- Explanation:
-- WEEKDAY(date) returns the index of the weekday (0 for Monday, 1 for Tuesday, etc.).
-- In this case, it returns 0 for Monday.

-- Summary
-- Date functions such as NOW(), CURDATE(), DATE_ADD(), DATE_SUB(), DATEDIFF(), DATE_FORMAT(), YEAR(), MONTH(), DAY(), and WEEKDAY() 
-- are used to manipulate the query date and time values in MySQL. 
-- They allow for effective data analysis and reporting based on date and time information.
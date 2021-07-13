# Write your MySQL query statement below
SELECT id,
SUM(CASE WHEN month='Jan' then revenue else null end) Jan_Revenue,
SUM(CASE WHEN month='Feb' then revenue else null end) Feb_Revenue,
SUM(CASE WHEN month='Mar' then revenue else null end) Mar_Revenue,
SUM(CASE WHEN month='Apr' then revenue else null end) Apr_Revenue,
SUM(CASE WHEN month='May' then revenue else null end) May_Revenue,
SUM(CASE WHEN month='Jun' then revenue else null end) Jun_Revenue,
SUM(CASE WHEN month='Jul' then revenue else null end) Jul_Revenue,
SUM(CASE WHEN month='Aug' then revenue else null end) Aug_Revenue,
SUM(CASE WHEN month='Sep' then revenue else null end) Sep_Revenue,
SUM(CASE WHEN month='Oct' then revenue else null end) Oct_Revenue,
SUM(CASE WHEN month='Nov' then revenue else null end) Nov_Revenue,
SUM(CASE WHEN month='Dec' then revenue else null end) Dec_Revenue
From
Department
Group By id
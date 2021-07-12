# Write your MySQL query statement below
SELECT Email From Person Group BY Email Having Count(Email)>1;
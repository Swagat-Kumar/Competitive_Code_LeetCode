# Write your MySQL query statement below
select t.id from Weather as t, Weather as y where DATEDIFF(t.RecordDate,y.RecordDate)=1 AND t.Temperature > y.Temperature; 
# Write your MySQL query statement below
# select salary as secondhighestsalary from employee where salary<>(select salary from employee order by salary desc limit 1) order by salary desc limit 1;
SELECT MAX(Salary) AS SecondHighestSalary FROM Employee 
WHERE Salary < (SELECT MAX(Salary) FROM Employee);
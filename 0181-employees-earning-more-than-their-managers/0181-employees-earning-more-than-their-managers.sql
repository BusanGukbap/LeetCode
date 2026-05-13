# Write your MySQL query statement below
Select A.Name as Employee
From Employee as A
    Inner Join Employee as B
    ON A.managerId = B.id
Where A.salary > B.salary
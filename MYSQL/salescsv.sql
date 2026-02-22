USE company_db;

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    region VARCHAR(50),
    salesperson VARCHAR(100),
    sale_date DATE,
    revenue DECIMAL(10, 2)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/sales.csv'
INTO TABLE sales
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT region, sum(revenue) as regional_rev
from sales
group by region;

select salesperson, avg(revenue) as avg_rev
from sales
group by salesperson
having avg_rev > 400;


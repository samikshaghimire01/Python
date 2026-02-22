
USE company_db;

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10, 2)
);
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/orders.csv'
INTO TABLE orders
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT MIN(amount) AS smallest_order, MAX(amount) AS largest_order 
FROM orders;

Select customer_id, sum(amount) as total_spent
from orders
group by customer_id;

select customer_id, sum(amount) as total_spent
from orders
group by customer_id
having total_spent > 500;

SELECT customer_id, order_date, amount,
SUM(amount) OVER(PARTITION BY customer_id ORDER BY order_date) AS running_total
FROM orders;

SELECT customer_id, order_date, amount,
LAG(amount) OVER(PARTITION BY customer_id ORDER BY order_date) AS previous_order_amount
FROM orders;

WITH CustomerTotals AS (
    SELECT customer_id, SUM(amount) as total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT customer_id, total_spent,
RANK() OVER(ORDER BY total_spent DESC) as customer_rank
FROM CustomerTotals;

SELECT customer_id, order_date AS current_order_date,
LEAD(order_date) OVER(PARTITION BY customer_id ORDER BY order_date) AS next_order_date
FROM orders;

SELECT order_id, customer_id, order_date, amount,
SUM(amount) OVER(ORDER BY order_date) AS total_cumulative_spend
FROM orders;
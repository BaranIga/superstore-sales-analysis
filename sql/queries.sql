-- 1. sprzedaż per region
SELECT region, SUM(sales) as total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- 2. profit per category
SELECT category, SUM(profit) as total_profit
FROM sales
GROUP BY category
ORDER BY total_profit DESC;

-- 3. straty
SELECT *
FROM sales
WHERE profit < 0;
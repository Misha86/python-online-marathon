SELECT PRODUCT_NAME, SUM(AMOUNT)
FROM ORDERS
GROUP BY PRODUCT_NAME
ORDER BY PRODUCT_NAME;
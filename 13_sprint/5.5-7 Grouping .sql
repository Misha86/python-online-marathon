SELECT PRODUCT_NAME, SUM(AMOUNT) FROM ORDERS GROUP BY PRODUCT_NAME ORDER BY PRODUCT_NAME;

SELECT PRODUCT_NAME, SUM(AMOUNT), SUM(PRODUCT_PRICE*AMOUNT) 
FROM ORDERS 
GROUP BY PRODUCT_NAME 
ORDER BY PRODUCT_NAME;

SELECT O.PRODUCT_NAME, COUNT(C.ID) 
FROM ORDERS O, CUSTOMERS C
WHERE O.ID_CUSTOMER = C.ID
GROUP BY PRODUCT_NAME 
ORDER BY PRODUCT_NAME;
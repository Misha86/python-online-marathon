SELECT O.PRODUCT_NAME, O.PRODUCT_PRICE
FROM ORDERS O, ORDERS M
GROUP BY O.PRODUCT_NAME, O.PRODUCT_PRICE
HAVING O.PRODUCT_PRICE = MAX(M.PRODUCT_PRICE)
ORDER BY O.PRODUCT_NAME;
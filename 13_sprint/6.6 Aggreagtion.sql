SELECT C.FIRSTNAME, C.LASTNAME
FROM CUSTOMERS C JOIN ORDERS O ON C.ID = O.ID_CUSTOMER
GROUP BY C.FIRSTNAME, C.LASTNAME
HAVING O.PRODUCT_PRICE*O.AMOUNT > (SELECT AVG(PRODUCT_PRICE*AMOUNT)
                                   FROM ORDERS)
ORDER BY C.FIRSTNAME, C.LASTNAME
SELECT C.FIRSTNAME, C.LASTNAME
FROM CUSTOMERS C JOIN ORDERS O ON C.ID = O.ID_CUSTOMER 
GROUP BY C.FIRSTNAME, C.LASTNAME
HAVING O.AMOUNT = (SELECT MAX(AMOUNT)
                  FROM ORDERS ORD, CUSTOMERS CUS
                  WHERE ORD.ID_CUSTOMER = CUS.ID)
ORDER BY C.FIRSTNAME, C.LASTNAME;



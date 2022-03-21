SELECT C.LASTNAME FROM CUSTOMERS C
WHERE NOT EXISTS (
     SELECT * FROM ORDERS O WHERE O.ID_CUSTOMER = C.ID) 
ORDER BY C.ID;

SELECT C.LASTNAME FROM CUSTOMERS C
      LEFT JOIN ORDERS O ON C.ID = O.ID_CUSTOMER
WHERE O.ID_CUSTOMER IS NULL
ORDER BY C.ID;
SELECT LASTNAME,
  (SELECT COUNT(*)
   FROM ORDERS
   WHERE ID_CUSTOMER = CUSTOMERS.ID)
FROM CUSTOMERS
ORDER BY LASTNAME;




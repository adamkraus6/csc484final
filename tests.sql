use warehouse;

-- SELECT * from customers;
-- SELECT * from employees;
-- SELECT * from injuryreports;
-- SELECT * from products;
-- SELECT * from orders;
-- SELECT * from orderitems;

select p.productName, numberOrdered, numberFulfilled from orderItems oi, products p where orderID=500 and oi.productID = p.productID;
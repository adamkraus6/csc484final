use warehouse;

INSERT INTO customers VALUES(100, "Jason", "Johnson", "jjohnson@gmail.com", "1234567890", "123 Oak St. Fake Town CA, 12345");
INSERT INTO customers VALUES(101, "Leo", "Paris", "mlbfan01@aol.com", "4445556789", "603 Chelsea Ct. Centerville AL, 77539");
INSERT INTO customers VALUES(102, "Joe", "Random", "jrandom@yahoo.com", "9874461089", "123 This St. Miami FL, 51948");
INSERT INTO customers VALUES(103, "Alex", "Christiansen", "achrist@gmail.com", "1937618955", "456 That St. Pierre SD, 91740");
INSERT INTO customers VALUES(104, "Randy", "Compton", "rcomp@aol.com", "9186134870", "789 Other St. Fake Town MA, 10874");

INSERT INTO employees VALUES(200, "Jose", "Fernandez", "Manager", "9713497134", "97 North St. Fake Town TX, 12312", 12345.0, true);
INSERT INTO employees VALUES(201, "Cody", "Bacon", "Supervisor", "1398875412", "102 South St. Fake Town SD, 08245", 9176.0, false);
INSERT INTO employees VALUES(202, "Sarah", "Alison", "Assistant", "9614106140", "200. West St. Fake Town KS, 10863", 2933.0, true);
INSERT INTO employees VALUES(203, "Jessica", "Smith", "Assistant", "7913476138", "415 East St. Fake Town PA, 19868", 15000.0, true);
INSERT INTO employees VALUES(204, "Mason", "Crosby", "Manager", "8163086134", "86 Albert Ln. Fake Town OR, 19624", 25969.0, false);

INSERT INTO injuryReports VALUES(300, 200, "1998-12-12", "Sprained ankle");
INSERT INTO injuryReports VALUES(301, 200, "1999-04-17", "Broken wrist");
INSERT INTO injuryReports VALUES(302, 202, "2002-05-14", "Explosion");
INSERT INTO injuryReports VALUES(303, 203, "2002-05-14", "Explosion");
INSERT INTO injuryReports VALUES(304, 204, "2002-05-14", "Explosion");

INSERT INTO products VALUES(400, "Printer", 215, 14);
INSERT INTO products VALUES(401, "Printer Ink", 25, 30);
INSERT INTO products VALUES(402, "Shovel", 15, 10);
INSERT INTO products VALUES(403, "Desk", 150, 5);
INSERT INTO products VALUES(404, "Chair", 50, 0);
INSERT INTO products VALUES(405, "Laptop", 500, 12);
INSERT INTO products VALUES(406, "Keyboard", 25, 25);
INSERT INTO products VALUES(407, "Mouse", 15, 22);
INSERT INTO products VALUES(408, "Water Bottle", 15, 40);
INSERT INTO products VALUES(409, "T-Shirt", 20, 36);

INSERT INTO orders VALUES(500, 100, 202, "2015-05-17", "2015-06-17", "Completed");
INSERT INTO orders VALUES(501, 103, 200, "2017-02-03", NULL, "In Progress");
INSERT INTO orders VALUES(502, 101, 204, "2012-07-22", NULL, "Cancelled");

INSERT INTO orderItems VALUES(500, 400, 2, 2);
INSERT INTO orderItems VALUES(500, 401, 5, 5);
INSERT INTO orderItems VALUES(500, 405, 1, 1);
INSERT INTO orderItems VALUES(501, 403, 2, 2);
INSERT INTO orderItems VALUES(501, 404, 2, 1);
INSERT INTO orderItems VALUES(501, 405, 1, 1);
INSERT INTO orderItems VALUES(502, 402, 5, 5);
INSERT INTO orderItems VALUES(502, 408, 4, 4);
INSERT INTO orderItems VALUES(502, 409, 10, 10);
INSERT INTO orderItems VALUES(502, 403, 1, 1);
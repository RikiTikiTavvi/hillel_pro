CREATE TABLE warehouses(
	id SERIAL NOT NULL PRIMARY KEY,
    name varchar(100) NOT NULL,
    location varchar(100) NOT NULL
);

CREATE TABLE goods(
    id SERIAL NOT NULL PRIMARY KEY,
    name varchar(255) NOT NULL,
    price integer NOT NULL,
    warehouses_id INTEGER NOT NULL REFERENCES warehouses(id),
    updated_at TIMESTAMP NOT NULL
);

INSERT INTO warehouses (name, location) VALUES
    ('storage 1', 'location 1'),
    ('storage 2', 'location 2'),
    ('storage 3', 'location 3');
   
INSERT INTO goods (name, price, warehouses_id, updated_at) VALUES
    ('product 1', 10.99, 1, '2023-06-20 19:38:21'),
    ('product 2', 15.99, 1,'2023-06-20 19:38:22'),
    ('product 3', 5.99, 2,'2023-06-20 19:38:23'),
    ('product 4', 5.99, 2,'2023-06-20 19:38:24'),
    ('product 5', 5.99, 2,'2023-06-20 19:38:25'),
    ('product 6', 5.99, 2,'2023-06-20 19:38:26'),
    ('product 7', 5.99, 2,'2023-06-20 19:38:27'),
    ('product 8', 5.99, 2,'2023-06-20 19:38:28'),
    ('product 9', 5.99, 2,'2023-06-20 19:38:29'),
    ('product 10', 5.99, 2,'2023-06-20 19:38:30');
 
UPDATE goods SET price = 9.99 WHERE id = 1;

DELETE FROM goods WHERE warehouses_id = 1;

CREATE INDEX index_ ON goods (name);

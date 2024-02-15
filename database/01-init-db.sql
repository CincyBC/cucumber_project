
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS shippers;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_details;

CREATE USER user1 WITH PASSWORD 'password';

CREATE TABLE categories
(      
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(25),
    description VARCHAR(255)
);

CREATE TABLE customers
(      
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    contact_name VARCHAR(50),
    address VARCHAR(50),
    city VARCHAR(20),
    postal_code VARCHAR(10),
    country VARCHAR(15)
);

CREATE TABLE employees
(
    employee_id SERIAL PRIMARY KEY,
    last_name VARCHAR(15),
    first_name VARCHAR(15),
    birth_date TIMESTAMP,
    Photo VARCHAR(25),
    Notes VARCHAR(1024)
);

CREATE TABLE shippers(
    shipper_id SERIAL PRIMARY KEY,
    shipper_name VARCHAR(25),
    phone VARCHAR(15)
);

CREATE TABLE suppliers(
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(50),
    contact_name VARCHAR(50),
    address VARCHAR(50),
    city VARCHAR(20),
    postal_code VARCHAR(10),
    country VARCHAR(15),
    phone VARCHAR(15)
);

CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(50),
    supplier_id INTEGER,
    category_id INTEGER,
    unit VARCHAR(25),
    price NUMERIC,
	FOREIGN KEY (category_id) REFERENCES categories (category_id),
	FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
);

CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    employee_id INTEGER,
    order_date TIMESTAMP,
    shipper_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employees (employee_id),
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
    FOREIGN KEY (shipper_id) REFERENCES shippers (shipper_id)
);

CREATE TABLE order_details(
    order_detail_id SERIAL PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    Quantity INTEGER,
	FOREIGN KEY (order_id) REFERENCES orders (order_id),
	FOREIGN KEY (product_id) REFERENCES products (product_id)
);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO user1;
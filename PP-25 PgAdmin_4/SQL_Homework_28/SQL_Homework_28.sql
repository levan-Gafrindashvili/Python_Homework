-- customers c
-- customer_profiles cp
-- products p
-- suppliers s

CREATE TABLE customers (
	customer_id SERIAL PRIMARY KEY,
	customer_name VARCHAR(30) NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE customer_profiles (
	profile_id SERIAL PRIMARY KEY,
	customer_id INT REFERENCES customers(customer_id) UNIQUE,
	phone_number VARCHAR(10),
	address VARCHAR(30)
);
SELECT customer_name, email FROM customers c
JOIN customer_profiles cp ON c.customer_id = cp.customer_id;

CREATE TABLE suppliers (
	supplier_id SERIAL PRIMARY KEY,
	supplier_name VARCHAR(30) NOT NULL,
	contact_email VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE products (
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(30) NOT NULL,
	price DECIMAL(6, 2) NOT NULL,
	supplier_id INT  REFERENCES suppliers(supplier_id) NOT NULL
);

CREATE TABLE orders (
	order_id SERIAL PRIMARY KEY,
	customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE,
	order_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE ordered_items (
	order_id INT REFERENCES orders(order_id),
	product_id INT REFERENCES products(product_id),
	quantity INT NOT NULL CHECK(quantity > 0),
	PRIMARY KEY (order_id, product_id)
)










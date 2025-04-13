-- 1)
-- UPDATE cars
-- SET Price = 6000.00
-- WHERE Brand = 'Nissan' AND Model = 'Altima';

-- UPDATE cars
-- SET Info_text = Info_text || ' Low mileage car.'
-- WHERE Mileage_KM < 100000;

-- ALTER TABLE cars
-- ADD COLUMN Color VARCHAR(20);

-- ALTER TABLE cars
-- DROP COLUMN is_sold;

-- ALTER TABLE cars
-- RENAME COLUMN Year_Of_Prouction TO Year_Of_Production;

-- ALTER TABLE cars
-- ALTER COLUMN Engine_size TYPE FLOAT;






-- 2)
-- CREATE TABLE cars1 (
-- 	car_id SERIAL PRIMARY KEY,
-- 	date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	is_sold BOOLEAN NOT NULL
-- );

-- CREATE TABLE car_general_info (
-- 	info_id SERIAL PRIMARY KEY,
-- 	brand VARCHAR(30) NOT NULL,
-- 	model VARCHAR(30) NOT NULL,
-- 	year_Of_Production INT NOT NULL,
-- 	engine_size DECIMAL(3,1) CHECK (Engine_size > 0.5)
-- );

-- CREATE TABLE car_specific_info(
-- 	vin_code VARCHAR(17) PRIMARY KEY,
-- 	car_id int NOT NULL,
-- 	info_id INT NOT NULL,
-- 	mileage_KM INT,
-- 	price DECIMAL(10, 2) NOT NULL,
-- 	is_custom_cleared BOOLEAN NOT NULL,
-- 	info_text TEXT,
-- 	FOREIGN KEY (car_id) REFERENCES cars1(car_id) ON DELETE CASCADE,
-- 	FOREIGN KEY (info_id) REFERENCES car_general_info(info_id) ON DELETE SET NULL
-- )

-- ALTER TABLE car_specific_info
-- ADD COLUMN Color VARCHAR(20); -- car_specific_info რო დავწერე მერე დავაკვირდი და ჩავამატე


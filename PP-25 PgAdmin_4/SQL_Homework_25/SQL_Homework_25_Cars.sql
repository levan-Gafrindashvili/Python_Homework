-- CREATE TABLE cars(
-- 	Car_id SERIAL PRIMARY KEY,
-- 	Brand VARCHAR(30) NOT NULL,
-- 	Model VARCHAR(30) NOT NULL,
-- 	Year_Of_Prouction INT NOT NULL,
-- 	Vin_code VARCHAR(17) UNIQUE NOT NULL,
-- 	Date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	Engine_size DECIMAL(3,1) CHECK (Engine_size > 0.5),
-- 	Mileage_KM INT,
-- 	Is_custom_cleared BOOLEAN NOT NULL,
-- 	Price DECIMAL(10, 2) NOT NULL,
-- 	Info_text TEXT,
-- 	is_sold BOOLEAN NOT NULL
-- )

-- INSERT INTO cars (Brand, Model, Year_Of_Prouction, Vin_code, Engine_size, Mileage_KM, Is_custom_cleared, Price, Info_text, is_sold)
-- VALUES
-- ('Toyota', 'Camry', 2020, 'IH8TR4FFIC7777777', 2.5, 100069, TRUE, 25000.0, 'Comes with a GPS that screams every time you hit traffic.',FALSE),
-- ('BMW', 'X5', 2018, 'BEEPBEEPIMAJ33P00', 3.0, 145000, TRUE, 15000.0, 'Conquers any terrain... except smooth roads.',FALSE),
-- ('Mercedes', 'C-Class', 2021, 'LOL4UHAHA1234567', 2.0, 80000, TRUE, 40000.0, 'This car comes with built-in sarcasm and a honk that sounds like laughter.',FALSE),
-- ('Honda', 'Civic', 2019, 'C4TLOV3RS12345678', 1.8, 300000, TRUE, 8000.00, 'Warning: This car may refuse to start if your cat isnt inside.', FALSE),
-- ('Ford', 'Mustang', 2022, 'OMGFASTCAR987654', 5.0, 40000, FALSE, 50000.00, 'Sporty and fast. Goes 0-60... eventually. Downhill. With a tailwind.', FALSE),
-- ('Audi', 'A4', 2020, 'M1N3CR4FTC4R99999', 2.0, 25000, TRUE, 30000.00, 'Powered by redstone. Breaks when touched.', FALSE),
-- ('Chevrolet', 'Tahoe', 2017, 'C0D3R5DRV3FAST999', 5.3, 60000, TRUE, 28000.00, 'Powered by caffeine and last-minute deadlines.', FALSE),
-- ('Volkswagen', 'Passat', 2018, 'A1NTN0BR4K3S12345', 1.4, 40000, TRUE, 20000.00, 'Stops when it feels like it. Hold on tight!', FALSE),
-- ('Hyundai', 'Elantra', 2021, 'T0OBROK3F0RGAS999', 2.0, 20000, TRUE, 22000.00, 'Fuel-efficient because its always parked!', FALSE),
-- ('Nissan', 'Altima', 2019, 'BR0K3NC4R0000000', 2.5, 550000, TRUE, 5500.00, 'Runs great! (If you push it.)', FALSE),

-- ('Audi', 'RS7', 2023, 'G0TSPD99999999999', 4.0, 5000, TRUE, 150000.00, 
--  'This Audi RS7 doesn’t just drive—it teleports. Twin-turbo V8? Check. 0-60 in ‘blink and you’ll miss it’? Absolutely. 
--   If Batman had a daily driver, this would be it. Comes with a built-in ego boost, a soundtrack of turbo whooshes, 
--   and enough horsepower to make your neighbor’s car develop self-esteem issues And Lastly Its Black,', 
--   FALSE);

SELECT * FROM cars;

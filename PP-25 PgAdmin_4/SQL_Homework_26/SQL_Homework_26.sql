
-- SELECT * FROM public.cars
-- ORDER BY car_id ASC 

-- SELECT brand, model, year_of_prouction, price FROM cars
-- ORDER BY brand ASC

-- SELECT * FROM cars
-- WHERE Brand = 'Audi';

-- SELECT * FROM cars
-- WHERE price BETWEEN 20000 AND 50000

-- SELECT * FROM cars
-- WHERE year_of_prouction > 2000
	-- AND is_custom_cleared = TRUE; -- აქ = TRUE რო არ დამეწერა მაინც იგივე სიას მიგდებდა და ეს უფრო სწორი მიდგომაა თუ = TRUE ამის გარეშე ?

-- DELETE FROM cars
-- 	WHERE (
--     SELECT Car_id FROM cars
--     ORDER BY Car_id
--     LIMIT 2
-- );

-- DELETE FROM cars
-- 	WHERE is_sold = TRUE

-- DELETE FROM cars

-- TRUNCATE TABLE cars RESTART IDENTITY

-- DROP TABLE cars


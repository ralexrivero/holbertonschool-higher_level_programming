-- creates a table in the current database if doesnt exist
-- create id (INT) and name (VARCHAR(256)), database passed as argument
CREATE TABLE IF NOT EXISTS `first_table` (
	`id` int,
	`name` varchar(256)
	);

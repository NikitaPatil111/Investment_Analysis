CREATE DATABASE Investment_DB;
USE Investment_DB;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Cleaned_data.csv'
INTO TABLE  Cleaned_Data
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; -- Skip header row if present


CREATE TABLE Cleaned_Data (
    gender VARCHAR(50),
    age INT,
    Objective VARCHAR(255),
    Mutual_Funds FLOAT,
    Equity_Market FLOAT,
    Debentures FLOAT,
    Government_Bonds FLOAT,
    Fixed_Deposits FLOAT,
    PPF FLOAT,
    Gold FLOAT,
    Expect VARCHAR(255),
    Avenue VARCHAR(255),
    Reason_Equity VARCHAR(255),
    Reason_Mutual VARCHAR(255),
    Reason_Bonds VARCHAR(255),
    Reason_FD VARCHAR(255),
    Source VARCHAR(255)
);



ALTER TABLE Cleaned_Data
ADD COLUMN Sr_no INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE Cleaned_Data
MODIFY COLUMN Sr_no INT FIRST;


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Cleaned_Investment_Data.csv'
INTO TABLE  staging_cleaned_data_2
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; -- Skip header row if present


CREATE TABLE staging_cleaned_data_2 (
    gender VARCHAR(10),
    age INT,
    Investment_Avenues VARCHAR(255),
    Mutual_Funds VARCHAR(5),
    Equity_Market VARCHAR(5),
    Debentures VARCHAR(5),
    Government_Bonds VARCHAR(5),
    Fixed_Deposits VARCHAR(5),
    PPF VARCHAR(5),
    Gold VARCHAR(5),
    Stock_Marktet VARCHAR(5),
    Factor VARCHAR(255),
    Objective VARCHAR(255),
    Purpose VARCHAR(255),
    Duration VARCHAR(50),
    Invest_Monitor VARCHAR(5),
    Expect VARCHAR(255),
    Avenue VARCHAR(255),
    What_are_your_savings_objectives VARCHAR(255),
    Reason_Equity VARCHAR(255),
    Reason_Mutual VARCHAR(255),
    Reason_Bonds VARCHAR(255),
    Reason_FD VARCHAR(255),
    Source VARCHAR(255)
);

SELECT * FROM Cleaned_Data AS A 
LEFT JOIN staging_cleaned_data_2 AS B 
ON A.Sr_no=B.Sr_no
UNION
SELECT * FROM Cleaned_Data AS A 
RIGHT JOIN staging_cleaned_data_2 AS B 
ON A.Sr_no=B.Sr_no;





ALTER TABLE staging_cleaned_data_2
ADD COLUMN Sr_no INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE staging_cleaned_data_2
MODIFY COLUMN Sr_no INT FIRST;

ALTER TABLE staging_cleaned_data_2
MODIFY COLUMN Invest_Monitor VARCHAR(90);

SELECT * FROM Cleaned_Data;
SELECT * FROM Cleaned_Data LIMIT 10;

SELECT COUNT(*) as Total, MIN(Mutual_Funds) as Minimum_Mutual_Funds, MAX(Equity_Market) as Maximum_Equity_Market, AVG(Fixed_Deposits) as AVG_Fixed_Deposite
FROM Cleaned_Data;

SELECT age, COUNT(*)
FROM Cleaned_Data
GROUP BY age;


SELECT * FROM Cleaned_Data
INTO OUTFILE 'C:/Users/nikit/OneDrive/Desktop/Data Analytics Material\Full project/Cleaned_data_from_sql'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';


SHOW VARIABLES LIKE 'secure_file_priv';







    




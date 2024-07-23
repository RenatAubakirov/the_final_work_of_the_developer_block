-- Создание базы данных
CREATE DATABASE IF NOT EXISTS Human_Friends;
USE Human_Friends;

-- Создание таблиц
CREATE TABLE IF NOT EXISTS Pets (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Type VARCHAR(50),
    BirthDate DATE,
    Commands VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS PackAnimals (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Type VARCHAR(50),
    BirthDate DATE,
    Commands VARCHAR(255)
);

-- Заполнение таблиц данными
INSERT INTO Pets (Name, Type, BirthDate, Commands) VALUES
('Fido', 'Dog', '2020-01-01', 'Sit, Stay, Fetch'),
('Whiskers', 'Cat', '2019-05-15', 'Sit, Pounce'),
('Hammy', 'Hamster', '2021-03-10', 'Roll, Hide'),
('Buddy', 'Dog', '2018-12-10', 'Sit, Paw, Bark'),
('Smudge', 'Cat', '2020-02-20', 'Sit, Pounce, Scratch'),
('Peanut', 'Hamster', '2021-08-01', 'Roll, Spin'),
('Bella', 'Dog', '2019-11-11', 'Sit, Stay, Roll'),
('Oliver', 'Cat', '2020-06-30', 'Meow, Scratch, Jump');

INSERT INTO PackAnimals (Name, Type, BirthDate, Commands) VALUES
('Thunder', 'Horse', '2015-07-21', 'Trot, Canter, Gallop'),
('Sandy', 'Camel', '2016-11-03', 'Walk, Carry Load'),
('Eeyore', 'Donkey', '2017-09-18', 'Walk, Carry Load, Bray'),
('Storm', 'Horse', '2014-05-05', 'Trot, Canter'),
('Dune', 'Camel', '2018-12-12', 'Walk, Sit'),
('Burro', 'Donkey', '2019-01-23', 'Walk, Bray, Kick'),
('Blaze', 'Horse', '2016-02-29', 'Trot, Jump, Gallop'),
('Sahara', 'Camel', '2015-08-14', 'Walk, Run');

-- Создание таблицы с верблюдами
CREATE TABLE IF NOT EXISTS Camels AS
SELECT * FROM PackAnimals WHERE Type = 'Camel';

-- Создание таблицы без верблюдов
CREATE TABLE IF NOT EXISTS NonCamels AS
SELECT * FROM PackAnimals WHERE Type != 'Camel';

-- Создание таблицы для лошадей и ослов
CREATE TABLE IF NOT EXISTS Horses_Donkeys AS
SELECT * FROM NonCamels WHERE Type IN ('Horse', 'Donkey');

-- Создание таблицы для животных в возрасте от 1 до 3 лет
CREATE TABLE IF NOT EXISTS YoungAnimals AS
SELECT ID, Name, Type, BirthDate, Commands, TIMESTAMPDIFF(MONTH, BirthDate, CURDATE()) AS AgeInMonths
FROM (
    SELECT ID, Name, Type, BirthDate, Commands FROM Pets
    UNION ALL
    SELECT ID, Name, Type, BirthDate, Commands FROM Horses_Donkeys
) AS AllAnimals
WHERE BirthDate BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

-- Объединение всех таблиц в одну
CREATE TABLE IF NOT EXISTS AllAnimals AS
SELECT 'Pets' AS SourceTable, ID, Name, Type, BirthDate, Commands FROM Pets
UNION ALL
SELECT 'Camels' AS SourceTable, ID, Name, Type, BirthDate, Commands FROM Camels
UNION ALL
SELECT 'NonCamels' AS SourceTable, ID, Name, Type, BirthDate, Commands FROM NonCamels
UNION ALL
SELECT 'YoungAnimals' AS SourceTable, ID, Name, Type, BirthDate, Commands FROM YoungAnimals;

-- Вывод всех таблиц для проверки
SELECT * FROM Pets;
SELECT * FROM PackAnimals;
SELECT * FROM Camels;
SELECT * FROM NonCamels;
SELECT * FROM Horses_Donkeys;
SELECT * FROM YoungAnimals;
SELECT * FROM AllAnimals;

/* 1. Используя тестовую БД sqlite „chinook.db“ определите:
1) Сколько всего байт «занимают» песни из таблицы tracks
2) Сколько записей находится в таблицах employees и customers
3) Получить список треков tracks из альбома «A-Sides»
4) Используя группировку (https://www.w3schools.com/sql/sql_groupby.asp) определите общую стоимость треков в каждом альбоме */


--1)
SELECT SUM(Bytes) as sum FROM tracks

--2)
SELECT COUNT(*) as count FROM customers 
UNION SELECT COUNT(*) as count FROM employees

--3)
SELECT Title, Name 
FROM  tracks 
LEFT JOIN albums
USING (AlbumId) 
WHERE Title='A-Sides'

--4)
SELECT AlbumId, SUM(UnitPrice) as sum FROM tracks GROUP BY AlbumId
""" 1. Используя тестовую БД sqlite „chinook.db“ определите:
1) Сколько всего байт «занимают» песни из таблицы tracks
2) Сколько записей находится в таблицах employees и customers
3) Получить список треков tracks из альбома «A-Sides»
4) Используя группировку определите общую стоимость треков в каждом альбоме """



from peewee import * 


# Сколько всего байт «занимают» песни из таблицы tracks
conn = SqliteDatabase('chinook.db') 
cursor = conn.cursor()
cursor.execute("SELECT SUM(Bytes) as sum FROM tracks") 
results = cursor.fetchall() 
print(results)
conn.close()

# Сколько записей находится в таблицах employees и customers
conn = SqliteDatabase('chinook.db') 
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) as count FROM customers UNION SELECT COUNT(*) as count FROM employees") 
results = cursor.fetchall() 
print(results)
conn.close()

# Получить список треков tracks из альбома «A-Sides»
conn = SqliteDatabase('chinook.db') 
cursor = conn.cursor()
cursor.execute("SELECT Title, Name FROM  tracks LEFT JOIN albums USING (AlbumId) WHERE Title='A-Sides'") 
results = cursor.fetchall() 
print(results)
conn.close()

#Используя группировку определите общую стоимость треков в каждом альбоме
conn = SqliteDatabase('chinook.db') 
cursor = conn.cursor()
cursor.execute("SELECT AlbumId, SUM(UnitPrice) as sum FROM tracks GROUP BY AlbumId") 
results = cursor.fetchall() 
print(results)
conn.close()


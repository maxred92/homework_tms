""" 2. Используя ORM peewee создайте функцию которая получает от пользователя название альбома через input и выводит список всех треков в этом альбоме """
from peewee import *

# Создаем соединение с нашей базой данных
conn = SqliteDatabase('chinook.db')

# Определяем базовую модель о которой будут наследоваться остальные
class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой, из шаблона выше

# Определяем модель исполнителя
class Tracks(BaseModel):
    albums_id = AutoField(column_name='AlbumId')
    name = TextField(column_name='Name', null=True)

    class Meta:
        table_name = 'tracks'

class Albums(BaseModel):
    albums_id = AutoField(column_name='AlbumId')
    title = TextField(column_name='Title', null=True)

    class Meta:
        table_name = 'albums'

# Создаем курсор - специальный объект для запросов и получения данных с базы
cursor = conn.cursor()
file = input('Enter Album: ')
query = (Albums.select(Albums.title, Tracks.name)
            .join(Tracks, on=(Tracks.albums_id == Albums.albums_id))
            .where(Albums.title == file))

# SELECT Title, Name FROM  tracks LEFT JOIN albums USING (AlbumId) WHERE Title='A-Sides'


""" query = Albums.select().where(Artist.artist_id < 10).limit(5).order_by(Artist.artist_id.desc())
print(query)
# SELECT "t1"."ArtistId", "t1"."Name" FROM "Artist" AS "t1"
# WHERE ("t1"."ArtistId" < 10) ORDER BY "t1"."ArtistId" DESC LIMIT 5 """

# Ответ в виде словаря
artists_selected = query.dicts().execute()
for artist in artists_selected:
    print('artist: ', artist)

conn.close()
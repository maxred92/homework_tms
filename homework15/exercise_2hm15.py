""" 2. Используя ORM peewee создайте функцию которая получает от пользователя название альбома через input и выводит список всех треков в этом альбоме """
from peewee import *

conn = SqliteDatabase('chinook.db')

class BaseModel(Model):
    class Meta:
        database = conn  

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

cursor = conn.cursor()

file = input('Enter Album: ')

query = (Albums.select(Albums.title, Tracks.name)
            .join(Tracks, on=(Tracks.albums_id == Albums.albums_id))
            .where(Albums.title == file))

tracks_selected = query.dicts().execute()
for tracks in tracks_selected:
    print('Tracks: ', tracks)

conn.close()
from peewee import *

db = PostgresqlDatabase(
    'countries',
    host = 'localhost',
    port = '5432',
    user = 'superman',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Countries(BaseModel):
    name = CharField(max_length=255, null=False)
    official_name = CharField(max_length=255, null=False)
    capital = CharField(max_length=255, null=False)
    region = CharField(max_length=255, null=False)
    subregion = CharField(max_length=255, null=False)
    population = IntegerField()
    continents = CharField(max_length=255, null=False)
    timezones = CharField(max_length=255, null=False)

db.create_tables([Countries])    

db.close()
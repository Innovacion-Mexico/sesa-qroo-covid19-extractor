from peewee import *
import os, datetime
from dotenv import load_dotenv

load_dotenv()
databaseDb = os.getenv('DATABASE')
userDb = os.environ.get('DB_USER')
passDb = os.environ.get('DB_PASSWORD')
hostDb = os.environ.get('DB_HOST')
portDb = os.environ.get('DB_PORT', 5432)

database = PostgresqlDatabase(databaseDb, user=userDb, password=passDb,
                        host=hostDb, port=int(portDb))
def create_tables():
    with database:
        database.create_tables([GeneralCase])

class BaseModel(Model):
    class Meta:
        database = database

class GeneralCase(BaseModel):
    id = PrimaryKeyField()
    uuid = CharField(max_length=250, unique=True)
    created = DateTimeField(default=datetime.date.today)
    negative = IntegerField()
    positives = IntegerField()
    deaths = IntegerField()
    analyzing = IntegerField()
    recovered = IntegerField()



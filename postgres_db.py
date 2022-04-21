from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from config import get_postgres_settings

settings = get_postgres_settings()
print(settings.POSTGRES_DB_NAME)
SQLALCHEMY_DATABASE_URL_POSTGRES = 'postgresql://'+settings.POSTGRES_USER+':'+settings.POSTGRES_PASSWORD+'@'+settings.POSTGRES_HOST+'/'+settings.POSTGRES_DB_NAME
engine = create_engine(SQLALCHEMY_DATABASE_URL_POSTGRES)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):

    __tablename__ ='accounts'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    password = Column(String,nullable=False)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
    






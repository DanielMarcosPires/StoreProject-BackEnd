from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///./database.db"

engine = create_engine(db_url,connect_args={"check_same_thread":False})

session_local = sessionmaker(autocommit=False,autoflush=False,bind=engine)

base = declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:1119@localhost/deliver', 
                       echo=True)

Base = declarative_base()
Session = sessionmaker()
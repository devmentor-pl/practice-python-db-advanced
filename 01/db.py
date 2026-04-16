from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql+psycopg2://postgres:mojehaslo@localhost:5432/mojabaza"

DATABASE_URL = "sqlite:///mydatabase.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)



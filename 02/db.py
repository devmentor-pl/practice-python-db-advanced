from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
postgres_pass = os.getenv("postgres_pass")

DATABASE_URL = f"postgresql+psycopg2://postgres:{postgres_pass}@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import DateTime, func
from datetime import datetime

con_str = "postgresql+psycopg2://postgres:grosales@localhost:5432/postgres"

engine = create_engine(con_str)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Measurment(Base):

    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    device_name = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)


Base.metadata.create_all(engine)

measurements = [
    Measurment(device_name='thermometer_1', value=22.5,
               timestamp=datetime(2025, 8, 1, 10, 0)),
    Measurment(device_name='thermometer_1', value=23.0,
               timestamp=datetime(2025, 8, 1, 11, 0)),
    Measurment(device_name='barometer_1', value=1012.3,
               timestamp=datetime(2025, 8, 1, 10, 30)),
    Measurment(device_name='hygrometer_1', value=55.2,
               timestamp=datetime(2025, 8, 1, 10, 15)),
]

session.add_all(measurements)
session.commit()

measurements_count = session.query(
    func.count(Measurment.id).group_by(Measurment.device_name).all())

for device_name, count in measurements_count:
    print(f'{device_name} : {count}')

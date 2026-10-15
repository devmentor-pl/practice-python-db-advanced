from models import Base, Measurement
from db import engine, Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session() as session:
    try:

        now = datetime.now(ZoneInfo("Europe/Warsaw"))

        measurements = [
            Measurement(
                device_name="Multimetr", 
                value=3.3,  
                timestamp=now - timedelta(seconds=1)
            ),
            Measurement(
                device_name="Multimetr", 
                value=5,  
                timestamp=now - timedelta(seconds=2)
            ),
            Measurement(
                device_name="Multimetr", 
                value=12,  
                timestamp=now - timedelta(seconds=3)
            ),
            Measurement(
                device_name="Multimetr", 
                value=24,  
                timestamp=now - timedelta(seconds=4)
            ),
            Measurement(
                device_name="Decybelomierz", 
                value=60.3,  
                timestamp=now - timedelta(minutes=1)
            ),
            Measurement(
                device_name="Decybelomierz", 
                value=65,  
                timestamp=now - timedelta(minutes=2)
            ),
            Measurement(
                device_name="Decybelomierz", 
                value=70.1,  
                timestamp=now - timedelta(minutes=3)
            ),
            Measurement(
                device_name="Termometr", 
                value=20.5,  
                timestamp=now - timedelta(hours=1)
            ),
            Measurement(
                device_name="Termometr", 
                value=22.4,  
                timestamp=now - timedelta(hours=2)
            )
        ]
        
        session.add_all(measurements)
        
        session.commit()
        
        measurements_count = session.query(Measurement.device_name, func.count(Measurement.id)).group_by(Measurement.device_name).all()
        
        if measurements_count:
            print(measurements_count)
        else:
            print("Nie znaleziono!")
            
        avg_value = session.query(Measurement.device_name, func.avg(Measurement.value)).group_by(Measurement.device_name).all()
                
        if avg_value:
            print(avg_value)
        else:
            print("Nie znaleziono!")
        
    except SQLAlchemyError as e:
        
        session.rollback()
        print(f"Błąd: {e}")

from datetime import datetime, timedelta, timezone
from db import session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from models import Measurement, clear_database

def create_measurements():
    with session:
        try:
            now = datetime.now(timezone.utc)
            
            measurements = [
                Measurement(device_name="Sensor A", value=22.5, timestamp=now),
                Measurement(device_name="Sensor A", value=23.1, timestamp=now - timedelta(minutes=10)),
                Measurement(device_name="Sensor A", value=21.9, timestamp=now - timedelta(minutes=20)),
                
                Measurement(device_name="Sensor B", value=30.2, timestamp=now),
                Measurement(device_name="Sensor B", value=29.8, timestamp=now - timedelta(minutes=5)),
                Measurement(device_name="Sensor B", value=30.5, timestamp=now - timedelta(minutes=15)),
                
                Measurement(device_name="Sensor C", value=18.0, timestamp=now),
                Measurement(device_name="Sensor C", value=17.5, timestamp=now - timedelta(minutes=7)),
            ]
            
            session.add_all(measurements)
            session.commit()
        except SQLAlchemyError as e:
            print(f"Error: {e}")


def main():
    
    create_measurements()
    
    with session:
        try:
            # Oblicz i wypisz: liczbę pomiarów dla każdego urządzenia,
            result = session.query(Measurement.device_name, func.count(Measurement.id)).group_by(Measurement.device_name).all()
            print(result)
            
            # średnią wartość pomiaru dla każdego urządzenia.
            result2 = session.query(Measurement.device_name, func.avg(Measurement.value)).group_by(Measurement.device_name).all()
            print(result2)
            
        except SQLAlchemyError as e:
            print(f"Error: {e}")
             
    clear_database()

if __name__ == "__main__":
    main()
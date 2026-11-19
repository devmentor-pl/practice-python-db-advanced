from db import engine, Session
from models import Base, Measurement
from sqlalchemy import func

Base.metadata.create_all(engine)
session = Session()

## 1. Dodaj przykładowe dane dla kilku urządzeń (każde z wieloma pomiarami).
measure1 = Measurement(device_name="Kraków", value=-1, timestamp="2025-01-01 10:00:00")
measure2 = Measurement(device_name="Kraków", value=0.4, timestamp="2025-02-01 10:00:00")
measure3 = Measurement(device_name="Kraków", value=4.1, timestamp="2025-03-01 10:00:00")
measure4 = Measurement(device_name="Kraków", value=9.8, timestamp="2025-04-01 10:00:00")
measure5 = Measurement(device_name="Warszawa", value=-1.4, timestamp="2025-01-01 10:00:00")
measure6 = Measurement(device_name="Warszawa", value=-0.4, timestamp="2025-02-01 10:00:00")
measure7 = Measurement(device_name="Warszawa", value=3.2, timestamp="2025-03-01 10:00:00")
measure8 = Measurement(device_name="Warszawa", value=9.4, timestamp="2025-04-01 10:00:00")
measure9 = Measurement(device_name="Wrocław", value=0, timestamp="2025-01-01 10:00:00")
measure10 = Measurement(device_name="Wrocław", value=1.1, timestamp="2025-02-01 10:00:00")
measure11 = Measurement(device_name="Wrocław", value=4.3, timestamp="2025-03-01 10:00:00")
measure12 = Measurement(device_name="Wrocław", value=9.7, timestamp="2025-04-01 10:00:00")
measure13 = Measurement(device_name="Wrocław", value=14.3, timestamp="2025-05-01 10:00:00")

session.add_all([measure1, measure2, measure3, measure4, measure5, measure6, measure7, measure8, measure9, measure10, measure11, measure12, measure13])

# 2. Oblicz i wypisz: 
#    - liczbę pomiarów dla każdego urządzenia,
#    - średnią wartość pomiaru dla każdego urządzenia.
number_of_measurements = session.query(Measurement.device_name, func.count(Measurement.id)).group_by(Measurement.device_name).all()
for device_name, count in number_of_measurements:
    print(f'Liczba pomiarów w: {device_name} to {count}')

average_measurement = session.query(Measurement.device_name, func.avg(Measurement.value)).group_by(Measurement.device_name).all()
for device_name, average in average_measurement:
    print(f'Średnia temperatura w: {device_name} to {average}')

session.close()
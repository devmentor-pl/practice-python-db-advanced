from models import Base, Item
from db import engine, Session
from sqlalchemy.exc import SQLAlchemyError

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

with Session() as session:
    try:

        item_list = [
            Item(name="Zrobić backup bazy danych przed wdrożeniem", priority=241),
            Item(name="Wymienić filtr kabinowy i sprawdzić poziom oleju", priority=118),
            Item(name="Napisać testy jednostkowe do modułu autoryzacji", priority=194),
            Item(name="Odkamienić ekspres do kawy", priority=42),
            Item(name="Przejrzeć otwarte Pull Requesty na GitHubie", priority=215),
            Item(name="Uporządkować kable pod biurkiem", priority=13),
            Item(name="Zaktualizować pakiety na serwerze i zrestartować kontenery", priority=176),
            Item(name="Kupić zapas kawy ziarnistej i baterii AA", priority=89),
            Item(name="Naprawić skrypt parsujący logi z czujników", priority=250),
            Item(name="Wyczyścić nieużywane obrazy i wolumeny w Dockerze", priority=67),
            Item(name="Opłacić faktury za hosting i domeny", priority=233),
            Item(name="Skalibrować parametry podawania na stanowisku testowym", priority=159),
            Item(name="Skonfigurować automatyczne odnawianie certyfikatu SSL", priority=204),
            Item(name="Sprawdzić ciśnienie w oponach przed dłuższą trasą", priority=132),
            Item(name="Zoptymalizować zapytania SQL zwalniające generowanie raportów", priority=228),
            Item(name="Wymienić pastę termoprzewodzącą w laptopie", priority=74),
            Item(name="Przetestować obsługę błędów przy zerwaniu połączenia TCP", priority=187),
            Item(name="Posprzątać warsztat i posegregować klucze nasadowe", priority=29),
            Item(name="Dodać walidację danych wejściowych w formularzu rejestracji", priority=165),
            Item(name="Zarchiwizować stare projekty na zewnętrznym dysku SSD", priority=95),
        ]
        
        session.add_all(item_list)
        
        session.commit()
        
        results = session.query(Item).order_by(Item.priority.asc()).limit(5).offset(10).all()
        
        if results:
            for result in results:
                print(result.id, result.name, result.priority)
        else:
            print("Nie znaleziono!")
        
    except SQLAlchemyError as e:
        
        session.rollback()
        print(f"Błąd: {e}")

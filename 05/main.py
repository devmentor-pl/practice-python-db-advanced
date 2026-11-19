from db import engine, Session
from models import Base, Item

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session = Session()

# 1. Dodaj co najmniej 20 przykładowych elementów o różnych nazwach i priorytetach.
item1 = Item(name="Armin van Buuren, Sacha - Everlasting", priority=6)
item2 = Item(name="Artur Rojek - Mirafiori", priority=11)
item3 = Item(name="Ashe - Stop The Wedding!", priority=2)
item4 = Item(name="Dawid Kwiatkowski, Margaret - Później Ci opowiem", priority=1)
item5 = Item(name="Ely Oaks, LAVINIA - Reasons", priority=17)
item6 = Item(name="Fast Boy - Music Sounds", priority=19)
item7 = Item(name="Jasiek Piwowarczyk - obłoki", priority=3)
item8 = Item(name="Kuba i Kuba - Chłopaki", priority=5)
item9 = Item(name="Kygo, Max McNown - Take Me Back", priority=14)
item10 = Item(name="Margaret - Primabalerina", priority=13)
item11 = Item(name="Marissa - Będzie pięknie", priority=7)
item12 = Item(name="Mrozu, Kacperczyk - Wszystko czego chciałem", priority=16)
item13 = Item(name="Naarly, Major League Djz - Wasted", priority=4)
item14 = Item(name="Neptunica - What If?", priority=8)
item15 = Item(name="Ofenbach, Starsailor - Four To The Floor", priority=12)
item16 = Item(name="Take That, Michael Patrick Kelly - Feel My Love", priority=9)
item17 = Item(name="Taylor Swift - Patient Zero", priority=10)
item18 = Item(name="Temper City - Reverse Psychology", priority=20)
item19 = Item(name="Wiktor Waligóra - To jest to!", priority=15)
item20 = Item(name="Zalia - tylko kochaj mnie", priority=18)

session.add_all([
    item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, 
    item11, item12, item13, item14, item15, item16, item17, item18, item19, item20
])
session.commit()

# 2. Posortuj elementy rosnąco po `priorytecie.
items_sorted = session.query(Item).order_by(Item.priority).all()
print(f'Elementy posortowane rosnąco po priorytecie:')
for item in items_sorted:
    print(item.priority, item.name)

# 3. Zaimplementuj paginację: wypisz tylko elementy od 11 do 15 miejsca (strona 3 przy 5 elementach na stronę).
items_sorted_3page = session.query(Item).order_by(Item.priority).limit(5).offset(10).all()
print(f'\nElementy od 11 do 15 miejsca (3 strona)')
for item in items_sorted_3page:
    print(item.priority, item.name)

session.close()
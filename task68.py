books = [
    {"название": "Алые паруса", "автор": "Грин", "год выпуска": 2002},
    {"название": "Дюймовочка", "автор": "Андерсон", "год выпуска": 1666},
    {"название": "Война и мир", "автор": "Толстой", "год выпуска": 1778}
]

for book in books:
    if book["год выпуска"] > 2000:
        print("Название:", book["название"])
        print("Автор:", book["автор"])
        print("Год выпуска:", book["год выпуска"])
        print()

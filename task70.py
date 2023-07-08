employees = [
    {"имя": "Мария", "должность": "директор", "зарплата": 100000},
    {"имя": "Настя", "должность": "уборщик помещений", "зарплата": 10000},
    {"имя": "Михаил", "должность": "директор", "зарплата": 2000000}
]

managers = []

for employee in employees:
    if employee["должность"] == "директор":
        managers.append(employee["имя"])

print("директора:")
for manager in managers:
    print(manager)


from models import Transaction
import json
from dataclasses import asdict 
transactions = [
    Transaction(
    amount=100.0,
    date="2026-9-1",
    category="student fees",
 description="first term fees",
 transaction_type="Income",
 is_planned=True,
is_recurring=False,
id=1


),
Transaction (
    amount=1000,
    date="2026-9-2",
    category="cafeteria",
 description=" yearsly cafeteria rent",
 transaction_type="Income",
 is_planned=True,
is_recurring=True,
id=2
),
Transaction (
    amount=200,
    date="2026-12-5",
    category="maintenance",
    description="fixing the broken computer",
    transaction_type="expense",
    is_planned=True,
    is_recurring=False,   
id=3
)
]

data_to_save=[asdict(t) for t in transactions]
with open("transaction.json","w") as file :
     json.dump(data_to_save,file,indent=4)
print("Data saved to transaction.json")
with open("transaction.json","r") as file: 
 loaded_data=json.load(file)
print("Data loaded from transaction.json:")
print(loaded_data)
new_t = Transaction(
    amount=50.0,
    date="2026-12-10",
    category="Stationery",
    description="Whiteboard pens",
    transaction_type="expense",
    is_planned=True,
    is_recurring=False,
    id=4
) 
loaded_data.append(asdict(new_t))
with open("transaction.json","w") as file:
 json.dump(loaded_data,file,indent=4)
 print("New transaction added and saved to transaction.json")    
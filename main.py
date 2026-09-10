from models import Transaction

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
for t in transactions:
    print(t)
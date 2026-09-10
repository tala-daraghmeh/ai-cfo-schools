from dataclasses import dataclass
@dataclass
class Transaction:
    amount:float
    date:str
    category:str
    description:str
    transaction_type:str
    is_planned:bool
    is_recurring:bool
    id:int 
INCOME_CATEGORIES = [
    "Student Fees",
    "Cafeteria",
    "Donations"
]
EXPENSE_CATEGORIES = [
    "Maintenance",
    "Utilities",
    "Equipment",
    "Activities",
    "Stationery"
]






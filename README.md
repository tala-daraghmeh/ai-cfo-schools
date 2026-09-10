# AI CFO for Public Schools 🏫💰

An AI-powered Financial Planning & Decision-Support Assistant designed specifically for public school funds.

The system helps school financial supervisors understand their financial health, plan for unexpected operational expenses, simulate what-if scenarios, and receive data-grounded recommendations.

---

## 🎯 Core Value Proposition

Turning raw financial numbers into actionable future decisions:

Historical Financial Data ➡️ Deterministic Analysis ➡️ Forecasting & Scenarios ➡️ Explainable AI Recommendations

---

## 🧱 Project Structure

- **models.py**: Data models and standard school fund categories (Transaction entity, constants).
- **main.py**: Entry point containing sample data and execution test.

---

## 📊 Core Data Model (Transaction)

The foundational entity representing school cash flow:

- `id`: Unique identifier (Primary Key).
- `amount`: Transaction amount.
- `date`: Transaction date.
- `category`: Approved category (e.g. Student Fees, Cafeteria, Maintenance, Utilities).
- `description`: Purpose of the transaction.
- `transaction_type`: INCOME or EXPENSE.
- `is_planned`: Planned budget vs unplanned / emergency.
- `is_recurring`: Regular recurring vs one-time.

---

## 🚀 How to Run Locally

Clone the repository and run:


```bash
python main.py


 🗓️ 20-Day Development Roadmap

- [x] **Day 1: Data Modeling & Foundational Architecture
- [] **Days 2–4**: Data Persistence & Validation Engine
- [] **Days 5–8**: Financial Engine (IncomeExpenses, Balance, Reserve Tracking)

- [] **Days 9–12**: Forecasting & What-If Scenario Engine

- [] **Days 13–16**: AI Explanation & Data-Grounded Recommendations Layer

- [] **Days 17–20**: UI Integration, Polish, Demo & Final Pitch

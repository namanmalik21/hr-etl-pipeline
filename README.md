# HR ETL Pipeline 🚀

An end-to-end ETL (Extract, Transform, Load) pipeline built with Python that processes real HR data, cleans and transforms it, and loads it into a SQLite database for analysis.

---

## 📌 Project Overview

This project simulates a real-world data engineering workflow:
- **Extract** raw HR data from a CSV file
- **Transform** the data by cleaning missing values, filtering records, and creating derived columns
- **Load** the cleaned data into a SQLite database and query it using SQL

---

## 🛠️ Tech Stack

- **Python 3.13**
- **Pandas** — data manipulation and transformation
- **SQLAlchemy** — database connection and loading
- **SQLite** — lightweight database storage
- **Git & GitHub** — version control

---

## 📂 Project Structure

```
hr-etl-pipeline/
│
├── etl_pipeline.py          # Main ETL script
├── hrdept.csv               # Raw HR dataset (311 records, 36 columns)
├── HRDataset_cleaned.csv    # Cleaned and transformed dataset
├── active_employees.csv     # Filtered active employees
├── dept_salary_report.csv   # Department salary summary
├── hr_database.db           # SQLite database
└── README.md                # Project documentation
```

---

## ⚙️ How It Works

### Step 1 — Extract
Loads raw HR data from CSV into a Pandas DataFrame:
```python
df = pd.read_csv("hrdept.csv")
```

### Step 2 — Transform
- Handles missing values in `DateofTermination` and `ManagerID`
- Filters active employees
- Calculates total salary by department
- Identifies top 3 highest paid employees
- Creates a new `Salary_Grade` column (A/B/C/D) based on salary bands

### Step 3 — Load
Loads cleaned data into a SQLite database and runs SQL queries:
```python
engine = create_engine('sqlite:///hr_database.db')
df.to_sql('employees', con=engine, if_exists='replace', index=False)
```

---

## 📊 Sample Output

### Average Salary by Department
| Department           | Avg Salary |
|----------------------|------------|
| Admin Offices        | 71,791     |
| Executive Office     | 250,000    |
| IT/IS                | 97,064     |
| Production           | 59,953     |
| Sales                | 69,061     |
| Software Engineering | 94,989     |

### Salary Grades
| Grade | Salary Range     |
|-------|-----------------|
| A     | Above 100,000   |
| B     | 70,000 - 99,999 |
| C     | 50,000 - 69,999 |
| D     | Below 50,000    |

---

## 🚀 How to Run

1. Clone the repository:
```
git clone https://github.com/namanmalik21/hr-etl-pipeline.git
```

2. Install dependencies:
```
pip install pandas sqlalchemy
```

3. Run the pipeline:
```
python etl_pipeline.py
```

---

# ============================================================
# HR Data ETL Pipeline
# Author: Naman
# Description: Extracts HR data, transforms and cleans it,
#              and loads it into a SQLite database
# ============================================================

import pandas as pd
from sqlalchemy import create_engine


# ─────────────────────────────────────────
# STEP 1: EXTRACT — Load raw data from CSV
# ─────────────────────────────────────────

df = pd.read_csv("hrdept.csv")

print("=== Dataset Overview ===")
print(df.head())
print(f"Shape: {df.shape}")
print(df.dtypes)


# ─────────────────────────────────────────
# STEP 2: TRANSFORM — Clean and enrich data
# ─────────────────────────────────────────

# Check for missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Fill missing values
df['DateofTermination'] = df['DateofTermination'].fillna('Still Active')
df['ManagerID'] = df['ManagerID'].fillna(0)
print("\nMissing values after cleaning:")
print(df[['DateofTermination', 'ManagerID']].isnull().sum())

# Filter only active employees
active_emp = df[df['EmploymentStatus'] == 'Active']
print(f"\nActive employees: {len(active_emp)}")

# Total salary by department
dept_salary = df.groupby('Department')['Salary'].sum().reset_index()
dept_salary.columns = ['Department', 'Total_Salary']
print("\n=== Total Salary by Department ===")
print(dept_salary)

# Top 3 highest paid employees
highest_salary = df.sort_values(by='Salary', ascending=False).head(3)
print("\n=== Top 3 Highest Paid Employees ===")
print(highest_salary[['Employee_Name', 'Salary']])

# Add salary grade column
def salary_grade(salary):
    if salary > 100000:
        return 'A'
    elif salary >= 70000:
        return 'B'
    elif salary >= 50000:
        return 'C'
    else:
        return 'D'

df['Salary_Grade'] = df['Salary'].apply(salary_grade)
print("\n=== Salary Grades (Sample) ===")
print(df[['Employee_Name', 'Salary', 'Salary_Grade']].head(10))

# Save cleaned data to CSV
df.to_csv("HRDataset_cleaned.csv", index=False)
active_emp.to_csv("active_employees.csv", index=False)
dept_salary.to_csv("dept_salary_report.csv", index=False)
print("\nCleaned files saved successfully!")


# ─────────────────────────────────────────
# STEP 3: LOAD — Save data into SQLite DB
# ─────────────────────────────────────────

engine = create_engine('sqlite:///hr_database.db')

df.to_sql('employees', con=engine, if_exists='replace', index=False)
print("\nData loaded into database successfully!")

# Query the database to verify
query = "SELECT Department, AVG(Salary) as Avg_Salary FROM employees GROUP BY Department"
result = pd.read_sql(query, con=engine)
print("\n=== Average Salary by Department (from DB) ===")
print(result)
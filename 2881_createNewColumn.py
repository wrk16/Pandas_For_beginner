# Question : Write a solution to create a new column "employee_salary" in the employees DataFrame with the following values: [50000, 60000, 70000, 80000, 90000].

import pandas as pd

def createNewColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column "employee_salary"
    employees["employee_salary"] = [50000, 60000, 70000, 80000, 90000]
    return employees

# Test the solution
if __name__ == "__main__":
    employees = pd.DataFrame({
        "employee_id": [1, 2, 3, 4, 5],
        "employee_name": ["John", "Alice", "Bob", "David", "Eva"],
        "employee_age": [25, 22, 24, 23, 26]
    })

    result = createNewColumn(employees)
    print(result) # Expected output: employee_id employee_name  employee_age  employee_salary
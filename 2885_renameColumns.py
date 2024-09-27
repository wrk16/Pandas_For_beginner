# Question : Write a solution to rename the columns of the employees DataFrame as follows: "employee_id" -> "id", "employee_name" -> "name", "employee_age" -> "age", "employee_salary" -> "salary".


import pandas as pd

def renameColumns(employees: pd.DataFrame) -> pd.DataFrame:
    # Rename the columns
    employees = employees.rename(columns={
        "employee_id": "id",
        "employee_name": "name",
        "employee_age": "age",
        "employee_salary": "salary"
    })
    return employees

# Test the solution
if __name__ == "__main__":
    employees = pd.DataFrame({
        "employee_id": [1, 2, 3, 4, 5],
        "employee_name": ["John", "Alice", "Bob", "David", "Eva"],
        "employee_age": [25, 22, 24, 23, 26],
        "employee_salary": [50000, 60000, 70000, 80000, 90000]
    })

    result = renameColumns(employees)
    print(result) # Expected output: id   name  age  salary
                 #                 0   1   John   25   50000
                 #                 1   2  Alice   22   60000
                 #                 2   3    Bob   24   70000
                 #                 3   4  David   23   80000
                 #                 4   5    Eva   26   90000
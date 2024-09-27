# Question : Write a solution to change the data type of the 'employee_age' column to float in the employees DataFrame.

import pandas as pd

def changeDataType(employees: pd.DataFrame) -> pd.DataFrame:
    # Change the data type of the 'employee_age' column to float
    employees["employee_age"] = employees["employee_age"].astype(float)
    return employees

# Test the solution
if __name__ == "__main__":
    employees = pd.DataFrame({
        "employee_id": [1, 2, 3, 4, 5],
        "employee_name": ["John", "Alice", "Bob", "David", "Eva"],
        "employee_age": [25, 22, 24, 23, 26],
        "employee_salary": [50000, 60000, 70000, 80000, 90000]
    })
    result = changeDataType(employees)
    print(result) # Expected output:    employee_id employee_name  employee_age  employee_salary
                 #                 0           1   John   25          50000
                 #                 1           2  Alice   22          60000
                 #                 2           3    Bob   24          70000
                 #                 3           4  David   23          80000
                 #                 4           5    Eva   26          90000
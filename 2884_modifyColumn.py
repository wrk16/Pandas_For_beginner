# Question : A company intends to give its employees a pay rise. Write a solution to modify the salary column by multiplying each salary by 2.

import pandas as pd

def modifyColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Modify the salary column by multiplying each salary by 2
    employees["employee_salary"] = employees["employee_salary"] * 2
    return employees

# Test the solution
if __name__ == "__main__":
    employees = pd.DataFrame({
        "employee_id": [1, 2, 3, 4, 5],
        "employee_name": ["John", "Alice", "Bob", "David", "Eva"],
        "employee_age": [25, 22, 24, 23, 26],
        "employee_salary": [50000, 60000, 70000, 80000, 90000]
    })
    result = modifyColumn(employees)
    print(result) # Expected output: employee_id employee_name  employee_age  employee_salary
                 #                 0           1   John   25          100000
                 #                 1           2  Alice   22          120000
                 #                 2           3    Bob   24          140000
                 #                 3           4  David   23          160000
                 #                 4           5    Eva   26          180000
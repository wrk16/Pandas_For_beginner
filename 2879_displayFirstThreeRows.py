# Question : Write a solution to display the first 3 rows of this DataFrame.

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Display the first 3 rows
    result = employees.head(3)
    return result

# Test the solution
if __name__ == "__main__":
    employees = pd.DataFrame({
        "employee_id": [1, 2, 3, 4, 5],
        "employee_name": ["John", "Alice", "Bob", "David", "Eva"],
        "employee_age": [25, 22, 24, 23, 26]
    })

    result = selectFirstRows(employees)
    print(result)

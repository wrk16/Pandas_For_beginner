# Question : Write a solution to drop duplicate rows from the employees DataFrame.

import pandas as pd

def dropDuplicateRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicate rows
    result = employees.drop_duplicates()
    return result

# Test the solution
# Example usage:
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
})

result = dropDuplicateRows(customers)
print(result)
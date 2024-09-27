# Question : There are some rows having missing values in the name column. Write a solution to remove the rows with missing values.


import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Drop rows with missing values in the 'name' column
    students = students.dropna(subset=['name'])
    return students

# Test the solution
if __name__ == "__main__":
    students = pd.DataFrame({
        "student_id": [101, 102, 103, 104, 105],
        "name": ["John", "Alice", None, "David", "Eva"],
        "age": [25, 22, 24, 23, 26]
    })

    result = dropMissingData(students)
    print(result) # Expected output: student_id   name  age
                 #                 0     101   John   25
                 #                 1     102  Alice   22
                 #                 3     104  David   23
                 #                 4     105    Eva   26
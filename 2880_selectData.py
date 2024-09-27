# Question : Write a solution to select the name and age of the student with student_id = 101.

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Select the name and age of the student with student_id = 101
    result = students[students["student_id"] == 101][["student_name", "student_age"]]
    return result

# Test the solution
if __name__ == "__main__":
    students = pd.DataFrame({
        "student_id": [101, 102, 103, 104, 105],
        "student_name": ["John", "Alice", "Bob", "David", "Eva"],
        "student_age": [25, 22, 24, 23, 26]
    })

    result = selectData(students)
    print(result) # Expected output: student_name student_age
                  #                 0         John          25
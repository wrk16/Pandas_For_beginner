# Question : Write a solution to list the names of animals that weigh strictly more than 100 kilograms.
# Return the animals sorted by weight in descending order.
# The result format is in the following example.
# Example 1:
# Input: 
# DataFrame animals:
# +----------+---------+-----+--------+
# | name     | species | age | weight |
# +----------+---------+-----+--------+
# | Tatiana  | Snake   | 98  | 464    |
# | Khaled   | Giraffe | 50  | 41     |
# | Alex     | Leopard | 6   | 328    |
# | Jonathan | Monkey  | 45  | 463    |
# | Stefan   | Bear    | 100 | 50     |
# | Tommy    | Panda   | 26  | 349    |
# +----------+---------+-----+--------+
# Output: 
# +----------+
# | name     |
# +----------+
# | Tatiana  |
# | Jonathan |
# | Tommy    |
# | Alex     |
# +----------+


import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(by='weight', ascending=False)[['name']]
    
    
# Test the solution
if __name__ == "__main__":
    animals = pd.DataFrame({
        "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
        "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
        "age": [98, 50, 6, 45, 100, 26],
        "weight": [464, 41, 328, 463, 50, 349]
    })
    result = findHeavyAnimals(animals)
    print(result) 
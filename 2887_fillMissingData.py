# Question : There are some missing values in the 'employee_name' column. Write a solution to fill the missing values with "Unknown".

# Example 1:
# Input:+-----------------+----------+-------+
# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | None     | 135   |
# | WirelessEarbuds | None     | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+
# Output:
# +-----------------+----------+-------+
# | name            | quantity | price |
# +-----------------+----------+-------+
# | Wristwatch      | 0        | 135   |
# | WirelessEarbuds | 0        | 821   |
# | GolfClubs       | 779      | 9319  |
# | Printer         | 849      | 3051  |
# +-----------------+----------+-------+


import pandas as pd

def fillMissingData(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products

# Test the solution
if __name__ == "__main__":
    products = pd.DataFrame({
        "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
        "quantity": [None, None, 779, 849],
        "price": [135, 821, 9319, 3051]
    })
    result = fillMissingData(products)
    print(result) # Expected output:              name  quantity  price
                 # 0      Wristwatch       0  135
                 # 1  WirelessEarbuds       0  821
                 # 2        GolfClubs     779  9319
                 # 3          Printer     849  3051
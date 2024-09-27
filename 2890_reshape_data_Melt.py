# Question : Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.
# The result format is in the following example.
# Example 1:
# Input:
# +-------------+-----------+-----------+-----------+-----------+
# | product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
# +-------------+-----------+-----------+-----------+-----------+
# | Umbrella    | 417       | 224       | 379       | 611       |
# | SleepingBag | 800       | 936       | 93        | 875       |
# +-------------+-----------+-----------+-----------+-----------+
# Output:
# +-------------+-----------+-------+
# | product     | quarter   | sales |
# +-------------+-----------+-------+
# | Umbrella    | quarter_1 | 417   |
# | SleepingBag | quarter_1 | 800   |
# | Umbrella    | quarter_2 | 224   |
# | SleepingBag | quarter_2 | 936   |
# | Umbrella    | quarter_3 | 379   |
# | SleepingBag | quarter_3 | 93    |
# | Umbrella    | quarter_4 | 611   |
# | SleepingBag | quarter_4 | 875   |
# +-------------+-----------+-------+

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    melted_report = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    return melted_report

# Test the solution
if __name__ == "__main__":
    report = pd.DataFrame({
        "product": ["Umbrella", "SleepingBag"],
        "quarter_1": [417, 800],
        "quarter_2": [224, 936],
        "quarter_3": [379, 93],
        "quarter_4": [611, 875]
    })
    result = meltTable(report)
    print(result)
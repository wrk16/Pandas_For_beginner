# Write a solution to calculate and display the number of rows and columns of players.
# Return the result as an array:
# [number of rows, number of columns]

import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # Get the number of rows and columns in the DataFrame
    num_rows, num_cols = players.shape
    return [num_rows, num_cols]
    
# test the solution
players = pd.DataFrame({
    "player_id": [1, 2, 3, 4],
    "player_name": ["John", "Alice", "Bob", "David"],
    "player_age": [25, 22, 24, 23]
})
print(getDataframeSize(players)) # Expected output: [4, 3]
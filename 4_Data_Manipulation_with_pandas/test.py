import pandas as pd
import matplotlib.pyplot as plt

# dogs = pd.read_csv("4_Data_Manipulation_with_pandas\Resources\dogs.csv", index_col='date_of_birth', parse_dates=['date_of_birth'])
# dogs["height_cm"].hist()
# plt.show()


# # multiple, sequential `plt.show()` will do exactly that...
# # shows multiple, sequential graphs (has to close each one to get to the next graph)
# dogs["height_cm"].hist(bins=20)
# plt.show()

# dogs["height_cm"].hist(bins=5)
# plt.show()


sully = pd.read_csv("4_Data_Manipulation_with_pandas\Resources\sully.csv")
print(sully.head())

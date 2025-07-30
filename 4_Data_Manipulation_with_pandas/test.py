import pandas as pd
import matplotlib.pyplot as plt

dogs = pd.read_csv("Resources\dogs.csv", index_col='date_of_birth', parse_dates=['date_of_birth'])
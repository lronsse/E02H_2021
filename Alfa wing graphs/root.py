import pandas as pd
import matplotlib.pyplot as plt

inboard = pd.read_excel(r'dataset.xlsx', sheet_name='INBOARD')
loaddis = pd.read_excel(r'dataset.xlsx', sheet_name='LOAD & DISPLACEMENT')
inboard = inboard[inboard.columns[:9]]
inboard = inboard[:81]
# print(inboard)

load = loaddis["LOADCELL"]

topgauges = inboard[inboard.columns[1::2]]
bottomgauges = inboard[inboard.columns[::2]]

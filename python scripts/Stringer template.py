import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

zlevels = [50, -0.5, 50]
# stringer holes
nstringers = 6
rivet_spacing1 = 50
top_spacing = 10.8
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [29, 29, 28, 27, 26, 24]

xcords, ycords, zcords = [], [], []

for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)

# printing and csv output
data = {"xcords": xcords, "ycords": ycords, "zcords": zcords}
frame = pd.DataFrame(data)
frame["i"] = 0
frame["j"] = 0
frame["k"] = -1
frame.to_csv("WB1_sheet_C1.csv", header=False, index=False)

import pandas as pd
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

zlevels = [50, -0.5, 50]
xcords, ycords, zcords = [], [], []

# top row
rivetsperrow = 10
top_spacing = 10
side_spacing = 8.13
spacing = 0.0
for j in range(rivetsperrow):
    if j == 0:
        spacing = side_spacing
    elif j % 2 == 0:
        spacing += 45.67
    elif j % 2 != 0:
        spacing += 30.01
    for k in zlevels:
        xcords.append(top_spacing)
        ycords.append(spacing)
        zcords.append(k)
# bottom row
rivetsperrow = 6
top_spacing = 180.15
side_spacing = 8.13
ys = [68.53, 118.53, 168.53, 271.33, 321.33, 371.33]
for j in range(rivetsperrow):
    for k in zlevels:
        xcords.append(top_spacing)
        ycords.append(ys[j])
        zcords.append(k)

# side rows
rivetsperrow = 3
rivet_spacing = 38.2
top_spacing = 56.88
side_spacing = 10
ys = [10, 430]
for i in ys:
    for j in range(rivetsperrow):
        for k in zlevels:
            xcords.append(top_spacing+j*rivet_spacing)
            ycords.append(i)
            zcords.append(k)
xcords = [-round(entry, 2) for entry in xcords]
ycords = [round(entry, 2) for entry in ycords]
zcords = [round(entry, 2) for entry in zcords]

print(os.path.basename(__file__))
# printing and csv output
data = {"xcords": xcords, "ycords": ycords, "zcords": zcords}
frame = pd.DataFrame(data)
frame["i"] = 0
frame["j"] = 0
frame["k"] = -1
frame.to_csv("rib_path.csv", header=False, index=False)

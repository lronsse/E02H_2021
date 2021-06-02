import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

zlevels = [50, -0.5, 50]
# stringer holes
nstringers = 3
rivet_spacing1 = 50
top_spacing = 10.8
side_spacing = 50
rowspacing = 189.2

rivetsperrow1 = [26, 28, 29]

xcords, ycords, zcords = [], [], []

for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*rowspacing)
            zcords.append(k)

# rib holes
rivetsperrow2 = 6
top_spacing = 48.6
rowys = [230.0, 420.0, 1020.0]
spacing = 0.0
for i in range(len(rowys)):
    spacing = 0.0
    for j in range(rivetsperrow2):
        if j == 0:
            spacing += top_spacing
        elif j == 3:
            spacing += 102.8
        elif j == 1 or j == 4:
            spacing += 50
        elif j == 2 or j == 5:
            spacing += 50
        for k in zlevels:
            xcords.append(spacing)
            ycords.append(rowys[i])
            zcords.append(k)


xcords = [-round(entry, 2) for entry in xcords]
ycords = [round(entry, 2) for entry in ycords]
zcords = [round(entry, 2) for entry in zcords]

# printing and csv output
data = {"xcords": xcords, "ycords": ycords, "zcords": zcords}
frame = pd.DataFrame(data)
frame["i"] = 0
frame["j"] = 0
frame["k"] = -1
frame.to_csv("WB1_sheet_C2.csv", header=False, index=False)

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

zlevels = [50, -0.5, 50]
# stringer holes
nstringers = 2
rivet_spacing1 = 50
top_spacing = 10
side_spacing = 50
rowspacing = 128.4

rivetsperrow1 = [29, 29]

xcords, ycords, zcords = [], [], []

for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*rowspacing)
            zcords.append(k)
for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            if j == 5 or j == 12:
                ycords.append(float(side_spacing+j*rivet_spacing1))
                xcords.append(74.2)
                zcords.append(k)


# rib holes
rivetsperrow2 = 6
top_spacing = 36
rowys = [230.0, 420., 1020.]
spacing = 0.0
for i in range(len(rowys)):
    spacing = 0.0
    for j in range(rivetsperrow2):
        if j == 0:
            spacing += top_spacing
        elif j == 1 or j == 2:
            spacing += 38.2
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
frame.to_csv("WB1_sheet_A.csv", header=False, index=False)

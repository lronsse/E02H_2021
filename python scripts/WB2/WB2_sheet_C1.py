import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

zlevels = [50, -0.5, 50]
# stringer holes
nstringers = 4
rivet_spacing1 = 50
top_spacing = 10.8
y_spacing = [300, 226.53, 163.47, 100]
rowspacing = 126.14

rivetsperrow1 = [24, 24, 24, 24, 24, 24]

xcords, ycords, zcords = [], [], []
rowxs = []

for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(y_spacing[i]+j*rivet_spacing1))
            xcords.append(top_spacing+i*rowspacing)
            zcords.append(k)

# rib holes
rivetsperrow2 = 6
top_spacing = 48.6
rowys = [1150]
spacing = 0.0
for i in range(len(rowys)):
    spacing = 0.0
    for j in range(rivetsperrow2):
        if j == 0:
            spacing += top_spacing
        elif j % 2 != 0:
            spacing += 55.33
        elif j % 2 == 0:
            spacing += 70.8
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
frame.to_csv("WB2_sheet_C1.csv", header=False, index=False)

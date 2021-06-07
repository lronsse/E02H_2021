import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
CornerCords = [440, 880, 950, 1020, 1090, 1160, 1230, 1300, 1370, 1440, 1510, 1580, 1650]
#WB2_sheet_C1

zlevels = [50, -0.5, 50]
## stringer holes
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



#WB2_Sheet_C2

nstringers = 2
rivet_spacing1 = 50
top_spacing = 10.8 + CornerCords[0]
y_spacing = [300, 100]
rowspacing = 378.4

rivetsperrow1 = [24, 24]

rowxs = []

for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(y_spacing[i]+j*rivet_spacing1))
            xcords.append(top_spacing+i*rowspacing)
            zcords.append(k)

# rib holes
rivetsperrow2 = 7
top_spacing = 48.6 + CornerCords[0]
rowys = [1150]
spacing = 0.0
for i in range(len(rowys)):
    spacing = 0.0
    for j in range(rivetsperrow2):
        if j == 0:
            spacing += top_spacing
        else:
            spacing += 50
        for k in zlevels:
            xcords.append(spacing)
            ycords.append(rowys[i])
            zcords.append(k)



#Stringer B1

nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[1]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)

#Stringer B1

nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[2]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#Stringer B2
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[3]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#Stringer B2
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[4]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)

#B1
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[5]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#B1
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[6]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#B2
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[7]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#B4
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[8]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#B1
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[9]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
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
frame.to_csv("Config_3.csv", header=False, index=False)

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
CornerCords = [440, 645, 880, 950, 1020, 1090, 1160, 1230, 1300, 1370, 1440, 1510, 1580, 1650]
#WB1_sheet_C1

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
            xcords.append(top_spacing+i*rowspacing)
            zcords.append(k)

# rib holes
rivetsperrow2 = 10
top_spacing = 33.64
rowys = [230.0, 420.0, 730.0, 1020.0]
spacing = 0.0
for i in range(len(rowys)):
    spacing = 0.0
    for j in range(rivetsperrow2):
        if j == 0:
            spacing += top_spacing
        elif j % 2 != 0:
            spacing += 30
        elif j % 2 == 0:
            spacing += 45.7
        for k in zlevels:
            xcords.append(spacing)
            ycords.append(rowys[i])
            zcords.append(k)


#WB1_Sheet_A

# stringer holes
nstringers = 2
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[0]
side_spacing = 50
rowspacing = 128.4

rivetsperrow1 = [29, 29]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*rowspacing)
            zcords.append(k)

for j in range(rivetsperrow1[i]):
    for k in zlevels:
        if j == 5 or j == 12:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(74.2)
            zcords.append(k)


# rib holes
rivetsperrow2 = 3
top_spacing = 36 + CornerCords[0]
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



#WB1_Sheet_B


# stringer holes
nstringers = 2
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[1]
side_spacing = 50
rowspacing = 128.4

rivetsperrow1 = [25, 25]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*rowspacing)
            zcords.append(k)


for j in range(rivetsperrow1[i]):
    for k in zlevels:
        if j == 5 or j == 12:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(74.2)
            zcords.append(k)


# rib holes
rivetsperrow2 = 3
top_spacing = 36 + CornerCords[1]
rowys = [230.0, 420.0, 1020.0]
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

#Stringer C1

nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[2]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [29]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)

#Stringer C2

nstringers = 1
rivet_spacing1 = 50 
top_spacing = 10 + CornerCords[3]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [29]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#Stringer C3
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[4]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [28]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#Stringer C4
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[5]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [27]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#Stringer C5
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[6]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [27]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)

#Stringer C6
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[7]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [29]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)
#Stringer B1
# stringer holes
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
#Stringer B2
# stringer holes
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

#Stringer B3
# stringer holes
nstringers = 1
rivet_spacing1 = 50
top_spacing = 10 + CornerCords[10]
side_spacing = 50
rowspacing = 75.68

rivetsperrow1 = [24]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)

#Vertical Stiffener D1
# stringer holes
nstringers = 1
rivet_spacing1 = 64.2
top_spacing = 10 + CornerCords[11]
side_spacing = 11.8
rowspacing = 64.2

rivetsperrow1 = [3]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)

#Vertical Stiffener D1 (Symmetry)
# stringer holes
nstringers = 1
rivet_spacing1 = 64.2
top_spacing = 10 + CornerCords[12]
side_spacing = 11.8
rowspacing = 64.2

rivetsperrow1 = [3]


for i in range(nstringers):
    for j in range(rivetsperrow1[i]):
        for k in zlevels:
            ycords.append(float(side_spacing+j*rivet_spacing1))
            xcords.append(top_spacing+i*75.68)
            zcords.append(k)

#Rib 1.1 Wb1
# top row
rivetsperrow = 10
top_spacing = 10 + CornerCords[13]
side_spacing = 53.8
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
top_spacing = 180.15 + CornerCords[13]
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
top_spacing = 56.88 + CornerCords[13]
side_spacing = 10
ys = [10, 430]
for i in ys:
    for j in range(rivetsperrow):
        for k in zlevels:
            xcords.append(top_spacing+j*rivet_spacing)
            ycords.append(i)
            zcords.append(k)

#Rib 1.2 Wb1
# top row
rivetsperrow = 10
top_spacing = 10 + CornerCords[13]
side_spacing = 53.8 + 753
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
top_spacing = 180.15 + CornerCords[13]
side_spacing = 8.13
ys = [68.53, 118.53, 168.53, 271.33, 321.33, 371.33]
for j in range(rivetsperrow):
    for k in zlevels:
        xcords.append(top_spacing)
        ycords.append(ys[j]+753)
        zcords.append(k)

# side rows
rivetsperrow = 3
rivet_spacing = 38.2
top_spacing = 56.88 + CornerCords[13]
side_spacing = 10
ys = [10, 430]
for i in ys:
    for j in range(rivetsperrow):
        for k in zlevels:
            xcords.append(top_spacing+j*rivet_spacing)
            ycords.append(i + 753)
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
frame.to_csv("Config_1.csv", header=False, index=False)

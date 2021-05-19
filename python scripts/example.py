import pandas as pd

nstringers = 6
rivet_spacing1 = 50
top_spacing = 10.8
side_spacing = 50
rowspacing = 75.68

rivetsperrow = [29, 29, 28, 27, 26, 24]

xcords, ycords = [], []

# stringer holes
for i in range(nstringers):
    for j in range(rivetsperrow[i]):
        ycords.append(side_spacing+j*rivet_spacing1)
        xcords.append(round(top_spacing+i*75.68, 4))

# rib holes
rivetsperrow = 10
top_spacing = 33.64
rowys = [230, 420, 730, 1020]
spacing = 0
for i in range(3):
    for j in range(rivetsperrow):
        ycords.append(round(230+rowys[i], 4))
        if j % 2 == 0:
            spacing += top_spacing+j*30
        else:
            spacing += top_spacing+j*45.7
        xcords.append(spacing)


data = {"xcords": xcords, "ycords": ycords}
frame = pd.DataFrame(data)
frame.to_csv("C1.csv", header=False, index=False)
print(frame)

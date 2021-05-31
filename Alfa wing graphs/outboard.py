import pandas as pd
import matplotlib.pyplot as plt

outboard = pd.read_excel(r'dataset.xlsx', sheet_name='OUTBOARD')
loaddis = pd.read_excel(r'dataset.xlsx', sheet_name='LOAD & DISPLACEMENT')
outboard = outboard[outboard.columns[:11]]
outboard = outboard[:50]
# print(outboard)

load = -loaddis["LOADCELL"]
print(load)

topgauges = outboard[outboard.columns[1::2]]
bottomgauges = outboard[outboard.columns[::2]]
print(topgauges)
# print(bottomgauges)

fig, ax = plt.subplots(2, 2)
a = 0
for i in range(2, 9, 2):
    # print(i)
    ax[0, 0].plot(load, topgauges[f"SG {i}"], label=f"Sensor {i}")
ax[0, 0].set_title("Top sheet of outboard wingbox")
ax[0, 0].set_ylabel("Strain")
ax[0, 0].set_xlabel("Load [N]")
ax[0, 0].legend()

for i in range(1, 9, 2):
    # print(i)
    ax[1, 0].plot(load, bottomgauges[f"SG {i}"], label=f"Sensor {i}")
ax[1, 0].set_title("Bottom sheet of outboard wingbox")
ax[1, 0].set_ylabel("Strain")
ax[1, 0].set_xlabel("Load [N]")
ax[1, 0].legend()


ax[0, 1].plot(load, outboard["SG 9"], label="Sensor 9")
ax[0, 1].set_title("Left sheet of outboard wingbox")
ax[0, 1].set_ylabel("Strain")
ax[0, 1].set_xlabel("Load [N]")
ax[0, 1].legend()


ax[1, 1].plot(load, outboard["SG 10"], label="Sensor 10")
ax[1, 1].set_title("Right sheet of outboard wingbox")
ax[1, 1].set_ylabel("Strain")
ax[1, 1].set_xlabel("Load [N]")
ax[1, 1].legend()

ax[0, 0].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
ax[0, 1].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
ax[1, 1].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
ax[1, 0].ticklabel_format(axis="y", style="sci", scilimits=(0, 0))

fig.suptitle("Outboard wingbox Load-Strain graphs\n")
fig.set_figheight(12)
fig.set_figwidth(9)
fig.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

inboard = pd.read_excel(r'dataset.xlsx', sheet_name='INBOARD')
loaddis = pd.read_excel(r'dataset.xlsx', sheet_name='LOAD & DISPLACEMENT')
inboard = inboard[inboard.columns[:11]]
inboard = inboard[:81]
# print(inboard)

load = -loaddis["LOADCELL"]

topgauges = inboard[inboard.columns[1::2]]
bottomgauges = inboard[inboard.columns[::2]]
print(topgauges)
# print(bottomgauges)

fig, ax = plt.subplots(2, 2)
a = 0
for i in range(2, 9, 2):
    print(i)
    ax[0, 0].plot(topgauges[f"SG {i}"], load, label=f"Sensor {i}")
ax[0, 0].set_title("Top sheet of inboard wingbox")
ax[0, 0].set_xlabel("Strain")
ax[0, 0].set_ylabel("Load [N]")
ax[0, 0].legend()

for i in range(1, 9, 2):
    print(i)
    ax[1, 0].plot(bottomgauges[f"SG {i}"], load, label=f"Sensor {i}")
ax[1, 0].set_title("Bottom sheet of inboard wingbox")
ax[1, 0].set_xlabel("Strain")
ax[1, 0].set_ylabel("Load [N]")
ax[1, 0].legend()


ax[0, 1].plot(inboard["SG 9"], load, label="Sensor 9")
ax[0, 1].set_title("Left sheet of inboard wingbox")
ax[0, 1].set_xlabel("Strain")
ax[0, 1].set_ylabel("Load [N]")
ax[0, 1].legend()


ax[1, 1].plot(inboard["SG 10"], load, label="Sensor 10")
ax[1, 1].set_title("Right sheet of inboard wingbox")
ax[1, 1].set_xlabel("Strain")
ax[1, 1].set_ylabel("Load [N]")
ax[1, 1].legend()


fig.set_figheight(12)
fig.set_figwidth(9)
fig.tight_layout()
plt.show()

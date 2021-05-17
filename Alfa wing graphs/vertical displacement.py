import pandas as pd
import matplotlib.pyplot as plt

loaddis = pd.read_excel(r'dataset.xlsx', sheet_name='LOAD & DISPLACEMENT')
data = loaddis[["LOADCELL", "displacement 1", "displacement 2"]]
print(data)

xdata1 = data["displacement 1"]
xdata2 = data["displacement 2"]
ydata = -data["LOADCELL"]

fig = plt.figure()
ax = plt.axes()

ax.plot(xdata1, ydata, label="Sensor 1")
ax.plot(xdata2, ydata, label="Sensor 2")
plt.legend()
# axs[0].set_title("Displacement 1 vs loadcell")
ax.set_xlabel("Displacement [mm]")
ax.set_ylabel("Load [N]")

"""
axs[1].plot(xdata2, ydata)
# axs[1].set_title("Displacement 2 vs loadcell")
axs[1].set_xlabel("Displacement 2 [mm]")
axs[1].set_ylabel("Load [N]")
"""
fig.tight_layout()
plt.show()

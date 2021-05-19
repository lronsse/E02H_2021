import pandas as pd
import matplotlib.pyplot as plt

loaddis = pd.read_excel(r'dataset.xlsx', sheet_name='LOAD & DISPLACEMENT')
outboard = pd.read_excel(r'dataset.xlsx', sheet_name='OUTBOARD')
data = loaddis["LOADCELL"]
print(data)

outboard = outboard[outboard.columns[10:12]]
print(outboard)

xdata1 = outboard["SLEEVE TOP"]
xdata2 = outboard["SLEEVE BOTTOM"]
ydata = -data

fig = plt.figure()
ax = plt.axes()

ax.plot(ydata, xdata1, label="Sleeve top (B)")
ax.plot(ydata, xdata2, label="Sleeve bottom (A)")
plt.legend()
# axs[0].set_title("Displacement 1 vs loadcell")
ax.set_ylabel("Strain")
ax.set_xlabel("Load [N]")


fig.suptitle("Sleeve sensors A&B Load-Strain graphs")
fig.tight_layout()
plt.show()

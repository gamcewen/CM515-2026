import pandas as pd
import matplotlib.pyplot as plt
import os

new_directory_path = "/Users/gavinmcewen/Documents/GitHub/CM515-2026/modules/wk_10_image_analysis"
os.chdir(new_directory_path)
current_dir = os.getcwd()

#print(current_dir)

file_path = "Results.csv"
df = pd.read_csv(file_path)

x_axis = df.columns[0]
y_axis_raw = df.columns[1]
y_axis_normal = df.columns[3]

plt.figure()

plt.bar(df[x_axis], df[y_axis_raw])

plt.xlabel(x_axis)
plt.ylabel("Non-normalized Band Intensities")
plt.title("Non-normalized Western Blot Band Quantification")
plt.legend()
plt.grid(True)

plt.savefig("Non-normalized.png", dpi = 600)
plt.close()

plt.figure()

plt.bar(df[x_axis], df[y_axis_normal])

plt.xlabel(x_axis)
plt.ylabel("Normalized Band Intensities")
plt.title("Normalized Western Blot Band Quantification")
plt.legend()
plt.grid(True)

plt.savefig("Normalized.png", dpi = 600)
plt.close()

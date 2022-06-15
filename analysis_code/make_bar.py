import matplotlib.pyplot as plt
import matplotlib.colors

cm = plt.cm.get_cmap("hsv")
norm = matplotlib.colors.Normalize(vmin=0, vmax=255)
fig = plt.figure()
cax = fig.add_axes([0.1,0.1,0.8,0.4])
fig.colorbar(plt.cm.ScalarMappable(norm, cm), cax=cax, orientation="horizontal")
plt.xticks([0, 42.5, 85, 127.5, 170, 212.5, 255])
plt.show()

file_name = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/color_bar.png"
fig.savefig(file_name)
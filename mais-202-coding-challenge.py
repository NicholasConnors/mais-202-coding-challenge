import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from matplotlib.font_manager import FontProperties

#Load data from csv
data = np.loadtxt('data.csv', str, delimiter=',') 

#Get array of purpose and int_rate
purpose_index = data[0].tolist().index('purpose')
int_rate_index = data[0].tolist().index('int_rate')
#Cut off first row, keep 2 columns
data = data[1:,[purpose_index, int_rate_index]] 

#Create dictionary of purpose and list of int_rates
data_dict = {p:[] for p in sorted([p for p,_ in data])}
for purpose,int_rate in data:
    data_dict[purpose].append(float(int_rate))

#Calculate avgerage int_rate
avg_int_rate = [(key,np.average(value)) for key,value in data_dict.items()]

#Plot
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10,5), gridspec_kw={'width_ratios':[1, 2]})

#Bar graph colours
colours=cycle(['green', 'orange', 'blue', 'pink', 'lime', 'yellow', 'beige', 'grey'])

#Plot bar graph
ax2.bar(range(0, len(avg_int_rate)), [r for _,r in avg_int_rate], color=[next(colours) for i in range(len(avg_int_rate))])
ax2.yaxis.grid()
ax2.set_axisbelow(True)
ax2.set_aspect(0.5)

#Labels
ax2.set_xticks(range(0, len(avg_int_rate)))
ax2.set_xticklabels([p for p,_ in avg_int_rate], fontsize=7, rotation=25, ha='right')
ax2.set_xlabel('purpose')
ax2.set_ylabel('int_rate')

#Table
columns = ('purpose', 'avg_int_rate')
rows = range(0, len(avg_int_rate))
cell_text = [(purpose, '{:.6f}'.format(int_rate)) for purpose,int_rate in avg_int_rate]
table = ax1.table(cellText=cell_text,
          rowLabels=rows,
          colLabels=columns,
          loc='center',
          cellLoc='left',
          colWidths=[0.65,0.35])
table.auto_set_font_size(False)
table.set_fontsize(8)
ax1.axis('off') #Gets rid of unused plot

plt.show();
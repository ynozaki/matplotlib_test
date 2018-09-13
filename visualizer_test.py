# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter

n_groups=2
conditions=['with GPU','witout GPU']
y1=np.array([207, 1147])
y2=np.array([65, 245])
index=np.arange(n_groups)
x=np.array([0,1])
bar_width=0.35

fig, ax=plt.subplots()

rects1=ax.bar(index,y1,bar_width,color='b',label=conditions[0])
rects2=ax.bar(index+bar_width,y2,bar_width,color='r',label=conditions[1])

ax.set_xlabel('condition')
ax.set_ylabel('calculation time[s]')
ax.set_title('Performance comparison　w/o GPU')
ax.set_xticks(x + bar_width/2)
ax.set_xticklabels((conditions))
ax.set_xlim(0-2*bar_width,2+bar_width)
ax.legend()

fig.tight_layout()
plt.show()



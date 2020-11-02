import numpy as np
import random
import math
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import Bar

# Starting with a simple bar object
trace1 = Bar(
    x=[1, 2, 3],
    y=[2, 1, 1]
)

# (1) Two lists of numbers
#x1 = [1, 2, 3, 5, 6]
#y1 = [1, 4.5, 7, 24, 38]

# (2) Make dictionary linking x and y coordinate lists to 'x' and 'y' keys
#trace1 = dict(x=x1, y=y1)

# (3) Make list of 1 trace, to be sent to Plotly
data = [trace1]
# (@) Call the plot() function of the plotly.plotly submodule,
#     save figure as 's0_first_plot'
py.plot(data, filename='s0_first_plot')


stdList = [2, 4, 6, 100]

date = "Tue Nov 10 21:25:11 +0000 2015"

print "2015-10-"+date[8:10]+" "+date[11:19]

i=0
while i<10:
	i+=1
	print random.randint(0,3)


print '%.4f' % math.log(np.std(stdList), 10)

l1 = [1, 2, 3]
del l1[:]

l1.append(5)
print(l1)





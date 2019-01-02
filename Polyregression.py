__author__ = 'Márcio Ciolfi'
__copyright__ = 'Copyright 2019'
__license__ = 'Ciolfi'
__version__ = '1.0'
__maintainer__ = 'Márcio Ciolfi'
__email__ = 'ciolfi@gmail.com'
__course__ = 'SAE2019'
__date__ = '2019/01/02'
__username__ = 'mciolfi'
__description__ = 'Polynomial Regression using Pression dataset'
__status__ = 'Development'

# Open dataset
def arq(name, ndata, types):
    import csv

    listt = []  # Define listt as matrix
    with open(name, newline='') as csvfile:  # csv module will detect new lines
        if types == ' ':  text = csv.reader(csvfile, delimiter=' ')  # classify by space
        if types == ',':  text = csv.reader(csvfile, delimiter=',')  # classify by comma
        if types == '\t': text = csv.reader(csvfile, delimiter='\t') # classify by tab
        for line in text:
            for t in range(len(line) - ndata): line.remove('')  # Removes zeros inside data
            listt.append(line)  # Define listt as the data inside file
    return (listt)


# Main program
from numpy import exp, array, random, dot, square
from numpy.linalg import inv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

listt = array(arq('pressures.dat', 3, '\t'))  # Define listt as the data inside the file
x1 = [] # Set variables x1, x2 and y as matrix
x2 = []
y = []
one = []
#plt.xlabel('pressure')
#plt.ylabel('length')
#plt.semilogy()
for count in range(len(listt)): # Convert the data string in values
    x1.append(float(listt[count][0]))
    x2.append(float(listt[count][1]))
    y.append([int(listt[count][2])])
    one.append(1)
    #plt.subplot(221)
    #plt.plot(x1, y, 'go', label = 'lenght')
    #plt.subplot(222)
    #plt.plot(x2, y, 'r^', label = 'deep')
y = array(y)
x = [one, x1, square(x1), x2, square(x2)]
x = array(x).T # Adaptating the matrix direction
beta = dot(inv(dot(x.T,x)),dot(x.T,y))
# Testing the results of beta
# For lenght = 19 mm and diameter of 4.34 mm 
test1 = [1, 19, 19**2, 4.34, 4.34**2]
result1 = dot(test1,beta)
print (result1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#Axes3D.plot_wireframe(x1, x2, y)
#Axes3D.plot(x1, x2, y)

ax.set_xlabel('diameter [mm]',color='b')
ax.set_ylabel('lenght [mm]',color='r')
ax.set_zlabel('Pressure [bar]')
ax.scatter(x2, x1, y, c='g', marker='^')
ax.plot(x1, x2, y)
plt.show()

#"""fig, ax1 = plt.subplots()
#plt.grid(True)
#ax1.plot(x2, y, 'b.')
#ax1.set_ylabel('pressure [bar]')
# Make the y-axis label, ticks and tick labels match the line color.
#ax1.set_xlabel('diameter [mm]', color='b')
#ax1.tick_params('x', colors='b')

#ax2 = ax1.twiny()
#ax2.plot(x1, x2, y, 'r.')
#ax2.set_xlabel('lenght [mm]', color='r')
#ax2.tick_params('x', colors='r')
#plt.legend(('lenght', 'deep'),
#           shadow=True, loc=(0.01, 0.48), handlelength=1.5, fontsize=16)

#fig.tight_layout()
#plt.show()


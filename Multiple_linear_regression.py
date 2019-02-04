__author__ = 'Márcio Ciolfi'
__copyright__ = 'Copyright 2019'
__license__ = 'Free'
__version__ = '1.0'
__maintainer__ = 'Márcio Ciolfi'
__email__ = 'ciolfi@gmail.com'
__course__ = 'SAE2019'
__date__ = '2019/01/02'
__username__ = 'mciolfi'
__description__ = 'Multiple linear regression using Pression non zeros dataset'
__status__ = 'Production'


# Open dataset
def arq(name, ndata, types):
    import csv

    listt = []  # Define listt as matrix
    with open(name, newline='') as csvfile:  # csv module will detect new lines
        if types == ' ':  text = csv.reader(csvfile, delimiter=' ')  # classify by space
        if types == ',':  text = csv.reader(csvfile, delimiter=',')  # classify by comma
        if types == '\t': text = csv.reader(csvfile, delimiter='\t')  # classify by tab
        for line in text:
            for t in range(len(line) - ndata): line.remove('')  # Removes zeros inside data
            listt.append(line)  # Define listt as the data inside file
    return (listt)


# Main program
from numpy import exp, array, random, dot, square, log
from numpy.linalg import inv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

listt = array(arq('pressures_nonzeros.dat', 3, '\t'))  # Define listt as the data inside the file
# Set input variables one, x1, x2, and output y as matrix and vector
one = []
x1 = []
x2 = []
y = []
# plt.xlabel('pressure')
# plt.ylabel('length')
# plt.semilogy()
for count in range(len(listt)):  # Convert the data string in values
    x1.append(float(listt[count][0]))
    x2.append(float(listt[count][1]))
    y.append([int(listt[count][2])])
    one.append(1)
    # add values on plot
    plt.subplot(121)
    plt.grid(True)
    plt.plot(x1, y, 'g.', label = 'length')
    plt.xlabel ('Length [mm]')
    plt.ylabel ('Burst Pressure [bar]')
    plt.subplot(122)
    plt.grid(True)
    plt.xlabel ('External Diameter [mm]')
    plt.plot(x2, y, 'r.', label = 'External diameter')
# Define x value and beta and turn variables as array
y = array(y)
x = [one, x1, log(x1), x2, square(x2)]  # Main function
x = array(x).T  # Adaptating the matrix direction
beta = dot(inv(dot(x.T, x)), dot(x.T, y))  # Finding beta coefficients
# Print program data
print('# ' + '=' * 78)
print('Author: ' + __author__)
print('Copyright: ' + __copyright__)
print('License: ' + __license__)
print('Version: ' + __version__)
print('Maintainer: ' + __maintainer__)
print('Email: ' + __email__)
print('Status: ' + __status__)
print('Course: ' + __course__)
print('Date: ' + __date__)
print('Username: ' + __username__)
print('Description: ' + __description__)
print('# ' + '=' * 78)

# Print main function
print('beta = ',beta.T)
print('f(pipe) =', int(beta[0]), '+', int(beta[1]), '* length +', int(beta[2]), '* ln(length) +', int(beta[3]), '* diameter +', int(beta[4]), '* diameter^2')
# Testing the results of beta with sample
for length in [1.5, 3, 19]:
    for dia in [4.5, 4.36, 4.15]:
        test1 = [1, length, log(length), dia, square(dia)]
        result1 = dot(test1, beta)
        print('Length =', length, 'mm\t+ Diameter =', dia, 'mm\t => Burst Pressure =', int(result1[0]), 'bar')
        # Plot results
        plt.subplot(121)
        plt.grid(True)
        plt.plot(length, result1, 'bo')
        g_patch = mpatches.Patch(color='green', label='Input values')
        b_patch = mpatches.Patch(color='blue', label='Equation output')
        plt.legend(handles=[g_patch]+[b_patch])
        plt.subplot(122)
        plt.grid(True)
        plt.plot(dia, result1, 'bo')
        g_patch = mpatches.Patch(color='red', label='Input values')
        b_patch = mpatches.Patch(color='blue', label='Equation output')
        plt.legend(handles=[g_patch]+[b_patch])
plt.show ()

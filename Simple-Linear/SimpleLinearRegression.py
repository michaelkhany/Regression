###
#       "KNOWLEDGE NOT SHARED, IS WASTED." -Clan Jacobs.
###

import os.path
from csv_loader import get_CSVrowsCount_int, loadCSV_array, loadCSV_text
import os
def clear(): return os.system('cls')  # On Windows System to clear screen

# To check if file or directory exists


clear()
print("Let's see first 8 rows of data in the default csv file:")
csv_file_path = (r'income_happiness_498p.csv')
print(loadCSV_text(csv_file_path, 8))

# Let's go for the simple linear regression equation compution
# Loading CSV into array
csv_array_2cols = loadCSV_array(csv_file_path)
# Equation is: y =ax +b
# a = ((sum_y × sum_xp2) – ((sum_x × sum_xy)) / n (sum_xp2) – sum_xp2)
# b = (n (sum_xy) – ((sum_x × sum_y)) / n (sum_xp2) – sum_xp2)
n = get_CSVrowsCount_int(csv_file_path)

# print("Items count (n): " + str(n))

#Initiating the variables
sum_x =float(0)
sum_y =float(0)
sum_xy =float(0)
sum_xp2 =float(0)
sum_yp2 = float(0)
xys = []
xp2s = []
yp2s = []

# Check if variable is float not string or empty values
def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


i = 0  # to clean the garbage in the lists
# Computations start here:
for i in range(0, n):
    if (is_float(csv_array_2cols[i][1]) and is_float(csv_array_2cols[i][2])):
        x_row_ic0 = float(csv_array_2cols[i][1])
        sum_x += x_row_ic0
        t = x_row_ic0**2
        xp2s.append(t)

        y_row_ic1 = float(csv_array_2cols[i][2])
        sum_y += y_row_ic1
        t = (y_row_ic1**2)
        yp2s.append(t)

        t = (x_row_ic0*y_row_ic1)
        xys.append(t)
        # print("xys value(%f) and x*y value(%f)" %
        #       (xys[i], x_row_ic0*y_row_ic1))
# print("Last index: %d" % i)

# print("xys: "+str(len(xys)))
for j in range(0, len(xys)):
    sum_xy += xys[j]
    sum_xp2 += xp2s[j]
    sum_yp2 += yp2s[j]

print("SumX %f \n SumY %f \n SumXY %f \n SumX2 %f \n SumY2 %f " %
      (sum_x, sum_y, sum_xy, sum_xp2, sum_yp2))

#Slope
n =len(xys)
a = ((((sum_y * sum_xp2) - ((sum_x * sum_xy))) / (n * (sum_xp2) - sum_xp2)))
#Intercept
b = (((n * (sum_xy) - ((sum_x * sum_y))) / (n * (sum_xp2) - sum_xp2)))

print("y =(%f)x+(%f)" % (a, b))

i = input("Please enter your x value: ")
i = float(i)

if (i >= 0 or i < 0):
    print("y =(%f) *(%f) +(%f)" % (a, i, b))
    print("\t=%f" % (a*i+b))
else:
    print(">> Error: Please enter a valid number and try again.")

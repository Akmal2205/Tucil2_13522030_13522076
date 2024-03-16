from point import Point
import matplotlib.pyplot as plt
import numpy as np


#Helping Functions
def Insert_Point(pn):
    point = [float(x) for x in input(f"Masukkan titik {pn} (x,y): ").split(",")]
    return Point(point[0], point[1])

def mid_point(p0: Point, p2: Point):
    return Point((p0.getAbsis()+p2.getAbsis())/float(2), (p0.getOrdinat()+p2.getOrdinat())/float(2))

def mid_section(p0: Point, cp: Point, p2: Point):
    return mid_point(mid_point(p0, cp), mid_point(cp, p2))

#Inputs
n = int(input("Masukkan jumlah iterasi: "))
p0 = Insert_Point("p0")
p1 = Insert_Point("p1")
p2 = Insert_Point("p2")
ip=[p0,p1,p2]

#Main Function
def Divide_n_Conquer(n, p0, cp, p2, res):
    if (n==1):
        res.append(p0)
        res.append(mid_section(p0, cp, p2))
    else:
        Divide_n_Conquer(n-1, p0, mid_point(p0, cp), mid_section(p0, cp, p2), res) #left
        Divide_n_Conquer(n-1, mid_section(p0, cp, p2), mid_point(p2, cp), p2, res) #right

#Displaying, with a bit animation
x_input_points = np.array([x.getAbsis() for x in ip])
y_input_points = np.array([y.getOrdinat() for y in ip])
lines = []
fig, ax= plt.subplots()
ax.plot(x_input_points, y_input_points, marker = "p", c = "r")
for i in range(n):
    res = []
    Divide_n_Conquer(i+1, p0, p1, p2, res)
    res.append(p2)
    x_res = [x.getAbsis() for x in res]
    y_res = [y.getOrdinat() for y in res]
    ax.clear()
    ax.plot(x_input_points, y_input_points, marker="p", c="r")
    ax.plot(x_res, y_res, marker="o", label=f"Iterasi ke-{i+1}")
    ax.set_title("Bezier Curve with Divide n' Conquer")
    ax.legend()
    plt.pause(1.25)

plt.show()
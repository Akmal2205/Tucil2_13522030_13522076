from point import Point
import matplotlib.pyplot as plt
import numpy as np
import time

def Insert_Point(pn):
    point = [float(x) for x in input(f"Masukkan titik {pn} (x,y): ").split(",")]
    return Point(point[0], point[1])

def rumusbezier(p0:Point, p1:Point, p2:Point, t) :
    return [(1-t)*(1-t)*p0.getAbsis() + 2*(1-t)*t*p1.getAbsis() + t*t*p2.getAbsis(), (1-t)*(1-t)*p0.getOrdinat() + 2*(1-t)*t*p1.getOrdinat() + t*t*p2.getOrdinat()]

def bezierBF(p0,p1,p2,iterasi) :
    t = 2**iterasi
    arraybezier = []
    for i in range(0,t+1) :
        b = rumusbezier(p0,p1,p2,(i/t))
        arraybezier.append(Point(b[0],b[1]))
    return arraybezier

# def plot_bezier_curve(control_points, curve_points):
#     plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
#     plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Bezier Curve')
#     plt.title('Bezier Curve with Brute Force')
#     plt.legend()
#     plt.show()

def mainbf() :
    #Inputs
    n = int(input("Masukkan jumlah iterasi: "))
    while(n<=0):
        print("Input salah!, Masukkan ulang input >:(")
        n = int(input("Masukkan jumlah iterasi: "))
    p0 = Insert_Point("p0")
    p1 = Insert_Point("p1")
    p2 = Insert_Point("p2")
    ip=[p0,p1,p2]

    #Displaying, with a bit animation
    x_input_points = np.array([x.getAbsis() for x in ip])
    y_input_points = np.array([y.getOrdinat() for y in ip])
    fig, ax= plt.subplots()
    ax.plot(x_input_points, y_input_points, marker = "p", c = "r")
    for i in range(n):
        start = time.time()
        res = bezierBF(p0, p1, p2, i+1)
        end = time.time()
        print(f"Time taken: {(end-start)*10**3:.03f}ms")
        x_res = [x.getAbsis() for x in res]
        y_res = [y.getOrdinat() for y in res]
        ax.clear()
        ax.plot(x_input_points, y_input_points, marker="p", c="r")
        ax.plot(x_res, y_res, marker="o", label=f"Iterasi ke-{i+1}")
        ax.set_title("Bezier Curve with Divide n' Conquer")
        ax.legend()
        plt.pause(1.25)

    plt.show()

if __name__ == "__main__" :
    mainbf()
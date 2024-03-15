import matplotlib.pyplot as plt
import numpy as np

def rumusbezier(p0, p1, p2, t) :
    return [(1-t)*(1-t)*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0], (1-t)*(1-t)*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]]

def bezierBF(p0,p1,p2,iterasi) :
    t = 2**iterasi
    arraybezier = []
    for i in range(0,t+1) :
        b = rumusbezier(p0,p1,p2,(i/t))
        arraybezier.append(b)
    return arraybezier

def plot_bezier_curve(control_points, curve_points):
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
    plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Bezier Curve')
    plt.title('Bezier Curve with Brute Force')
    plt.legend()
    plt.show()

def mainbf() :
    print("Titik 1")
    x = float(input("x = "))
    y = float(input("y = "))
    p1 = [x,y]
    print("Titik 2")
    x = float(input("x = "))
    y = float(input("y = "))
    p2 = [x,y]
    print("Titik 3")
    x = float(input("x = "))
    y = float(input("y = "))
    p3 = [x,y]
    iterasi = int(input("jumlah iterasi = "))
    arraypoint = np.array([p1,p2,p3])
    arbf = np.array(bezierBF(p1,p2,p3,iterasi))
    plot_bezier_curve(arraypoint,arbf)

if __name__ == "__main__" :
    mainbf()
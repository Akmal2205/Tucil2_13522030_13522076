from point import Point
import matplotlib.pyplot as plt
import numpy as np

def Insert_Point(pn):
    point = [float(x) for x in input(f"Masukkan titik {pn} (x,y): ").split(",")]
    return Point(point[0], point[1])

def mid_point(p0: Point, p2: Point):
    return Point((p0.getAbsis()+p2.getAbsis())/float(2), (p0.getOrdinat()+p2.getOrdinat())/float(2))

def titikAproksimasi(control_point, pinggiran) :
    if len(control_point) <= 1 :
        return control_point, control_point
    else :
        titik_aproksimasi = []
        for i in range(len(control_point)-1) :
            titik_aproksimasi.append(mid_point(control_point[i],control_point[i+1]))
        titik, pinggir = titikAproksimasi(titik_aproksimasi,pinggiran)
        pinggir = np.concatenate(([control_point[0]], pinggir, [control_point[-1]]))
        return titik, pinggir
    
def nAryDNC(control_point, iterasi) :
    new_control_point, old_control_point = titikAproksimasi(control_point,[])
    if iterasi == 1 :
        return new_control_point
    else :
        mid = len(old_control_point)//2
        awal = old_control_point[:mid+1]
        akhir = old_control_point[mid:]
        res = np.array(nAryDNC(awal,iterasi-1))
        res = np.concatenate((res, new_control_point))
        res = np.concatenate((res,nAryDNC(akhir, iterasi-1)))
        return res
    
def mainNTitikDNC() :
    nTitik = int(input("Masukkan jumlah titik yang diinginkan = "))
    arr_point = []
    for i in range(nTitik) :
        p = Insert_Point("p")
        arr_point.append(p) 
    iterasi = int(input("Masukkan jumlah iterasi: "))
    while(iterasi<=0):
        print("Input salah!, Masukkan ulang input >:(")
        iterasi = int(input("Masukkan jumlah iterasi: "))
    #Displaying, with a bit animation
    x_input_points = np.array([x.getAbsis() for x in arr_point])
    y_input_points = np.array([y.getOrdinat() for y in arr_point])
    lines = []
    fig, ax= plt.subplots()
    ax.plot(x_input_points, y_input_points, marker = "p", c = "r")
    for i in range(iterasi):
        res = nAryDNC(arr_point, iterasi)
        res = np.concatenate((arr_point[0], res, arr_point[-1]))
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
    mainNTitikDNC()

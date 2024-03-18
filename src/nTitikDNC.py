from point import Point
import time
import matplotlib.pyplot as plt
import numpy as np

#Helping Functions
def Insert_Point(pn):
    point = [float(x) for x in input(f"Masukkan titik {pn} (x,y): ").split(",")]
    return Point(point[0], point[1])

def mid_point(p0: Point, p2: Point):
    return Point((p0.getAbsis()+p2.getAbsis())/float(2), (p0.getOrdinat()+p2.getOrdinat())/float(2))

def isSamePoint(p1: Point, p2: Point):
    return (p1.x == p2.x and p1.y == p2.y)

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
    
def uniqueArray(array):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]!="null" and array[j]!="null" and isSamePoint(array[i], array[j]):
                array[i] = "null"
    res=[]
    for el in array:
        if el!="null":
            res.append(el)
    return res
    
#Main Function
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

#Visual Bonus Function
def plotAnimation(ip, n):
    x_input_points = np.array([x.getAbsis() for x in ip])
    y_input_points = np.array([y.getOrdinat() for y in ip])
    for i in range(n):
        res = []
        res = nAryDNC(ip, i+1)
        res = np.concatenate(([ip[0]], res, [ip[-1]]))
        x_res = [x.getAbsis() for x in res]
        y_res = [y.getOrdinat() for y in res]
        x_input_points = [x.getAbsis() for x in ip]
        y_input_points = [y.getOrdinat() for y in ip]
        plt.clf()
        plt.plot(x_input_points, y_input_points, marker="p", c="r")
        plt.plot(x_res, y_res, marker="o", label=f"Iterasi ke-{i+1}")
        plt.title("Bezier Curve with Divide n' Conquer")
        plt.legend()
        plt.pause(1.25)

def bezier_time_taken(arr_point, iterasi):
    start = time.time()
    res = nAryDNC(arr_point, iterasi)
    res = np.concatenate(([arr_point[0]], res, [arr_point[-1]]))
    end = time.time()
    print(f"Time taken: {(end-start)*10**3:.03f}ms")


def mainNTitikDNC() :
    #Inputs
    iterasi = int(input("Masukkan jumlah iterasi : "))
    while(iterasi<=0):
        print("Input salah!, Masukkan ulang input >:(")
        iterasi = int(input("Masukkan jumlah iterasi : "))
    nTitik = int(input("Masukkan jumlah titik yang diinginkan : "))
    arr_point = []
    for i in range(nTitik) :
        p = Insert_Point(f"p{i+1}")
        arr_point.append(p) 
    arr_point = uniqueArray(arr_point)
    while len(arr_point) < 3:
        print("Masukkan minimal lebih dari 3 titik berbeda!")
        arr_point = []
        for i in range(nTitik) :
            p = Insert_Point(f"p{i+1}")
            arr_point.append(p) 
        arr_point = uniqueArray(arr_point)

    #Show time taken
    bezier_time_taken(arr_point, iterasi)

    #Displaying
    plotAnimation(arr_point, iterasi)
    plt.show()

if __name__ == "__main__" :
    mainNTitikDNC()

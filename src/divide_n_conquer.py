from point import Point

def Insert_Point(pn):
    point = [float(x) for x in input(f"Masukkan titik {pn} (x,y): ").split(",")]
    return Point(point[0], point[1])

def mid_point(p0: Point, p2: Point):
    return Point((p0.getAbsis()+p2.getAbsis())/float(2), (p0.getOrdinat()+p2.getOrdinat())/float(2))

def mid_section(p0: Point, cp: Point, p2: Point):
    return mid_point(mid_point(p0, cp), mid_point(cp, p2))

p0 = Insert_Point("p0")
p1 = Insert_Point("p1")
p2 = Insert_Point("p2")

res = []

def Divide_n_Conquer(n, p0, cp, p2, res):
    if (n==1):
        res.append(p0)
        res.append(mid_section(p0, cp, p2))
    else:
        Divide_n_Conquer(n-1, p0, mid_point(p0, cp), mid_section(p0, cp, p2), res) #left
        Divide_n_Conquer(n-1, mid_section(p0, cp, p2), mid_point(p2, cp), p2, res) #right

Divide_n_Conquer(3, p0, p1, p2, res)
res.append(p2)
# for i in range(len(res)):
#     res[i].printPoint()

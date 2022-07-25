from math import sin,cos
class points:
    def __init__(self,arr):
        self.x = arr[0]
        self.y = arr[1]
def swap(item1,item2):
    item1,item2 = item2,item1
    answer = item1,item2
    return
def rotatesue(center:points,points:points,rotationdegree,mirrorx = 0,mirrory = 0):
    #cases are R0,R90,RXY,R270 and all of items with X,Y and XY
    a,b,c,d = points[0], points[1], points[2], points[3]

    ap, bp, cp, dp = a, b, c, d
    ap.x = a.x * cos(rotationdegree) + a.y*sin(rotationdegree)
    bp.x = b.x * cos(rotationdegree) + b.y*sin(rotationdegree)
    cp.x = c.x * cos(rotationdegree) + c.y*sin(rotationdegree)
    dp.x = d.x * cos(rotationdegree) + d.y*sin(rotationdegree)

    ap.y = a.y * cos(rotationdegree) + a.y*sin(rotationdegree)
    bp.y = b.y * cos(rotationdegree) + b.y*sin(rotationdegree)
    cp.y = c.y * cos(rotationdegree) + c.y*sin(rotationdegree)
    dp.y = d.y * cos(rotationdegree) + d.y*sin(rotationdegree)    
    if mirrorx :
        ap.x = 2*center.x -a.x
        bp.x = 2*center.x -b.x
        cp.x = 2*center.x -c.x
        dp.x = 2*center.x -d.x
    elif mirrory:
        ap.y = 2*center.y -a.y
        bp.y = 2*center.y -b.y
        cp.y = 2*center.y -c.y
        dp.y = 2*center.y -d.y
    elif mirrorx and mirrory:
        swap(ap.x,ap.y)
        swap(bp.x,bp.y)
        swap(cp.x,cp.y)
        swap(dp.x,dp.y)

    pointsprime = ap,bp,cp,dp
    return pointsprime


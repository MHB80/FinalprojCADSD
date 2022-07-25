
def flipx(p,center = [0,0]):
    p[0]=2*center[0] -p[0]
    return p
def flipy(p,center =[0,0]):
    p[1]=2*center[1]-p[1]
    return p
def rotate_90_anchor_0(p):
    p[0],p[1] = p[1],p[0]
    p[0] = - p[0]
    return p
print(flipx([10,10])==[-10,10])
print(flipx([40,10],[10,0])==[-20,10])
print(flipy([10,10])==[10,-10])
print(flipy([10,60],[10,40])==[10,20])
print(rotate_90_anchor_0([10,-10])==[10,10])
print(rotate_90_anchor_0([40,-50])==[50,40])
print(rotate_90_anchor_0([-40,-50])==[50,-40])

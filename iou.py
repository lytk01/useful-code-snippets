#usr/bin/python

# Intersection over Union func
def IoU(x1,y1,w1,h1,x2,y2,w2,h2):
    interw=min(x1+w1,x2+w2)-max(x1,x2)
    interh=min(y1+h1,y2+h2)-max(y1,y2)
    if interw <=0 or interh <=0:
        return 0.0
    else:
        inters=interw*interh
        return inters/(w1*h1+w2*h2-inters)

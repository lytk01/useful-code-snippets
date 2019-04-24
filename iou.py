#usr/bin/python

# Intersection over Union func
def IoU(r1,r2):
    """calculate iou between 2 rectangles
    
    Arguments:
        r1 {tuple or list} -- first rectangle containing topleft point (x1,y1), width(w1) and height(h1)
        r2 {tuple or list} -- second rectangle containing topleft point (x2,y2), width(w2) and height(h2)
    
    Returns:
        {float} -- iou result
    """
    x1,y1,w1,h1=r1
    x2,y2,w2,h2=r2
    assert x1>0 and y1>0 and w1>0 and h1>0 and x2>0 and y2>0 and w2>0 and h2>0

    interw=min(x1+w1,x2+w2)-max(x1,x2)
    interh=min(y1+h1,y2+h2)-max(y1,y2)
    if interw <=0 or interh <=0:
        return 0.0
    else:
        inters=interw*interh
        return inters/(w1*h1+w2*h2-inters)

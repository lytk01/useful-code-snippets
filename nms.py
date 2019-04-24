#usr/bin/python
#coding=utf-8
from iou import IoU
from math import exp,pow

# TODO : update comments and usage.
def NMS(boxes:list,scores:list,threshold:float):
    """Implement NMS algorithm using given boxes and scores 

    Arguments:
        boxes {list} -- the list of initial detection boxes
        scores {list} -- the list of scores that contains corresponding detection scores
        threshold {float} -- the NMS threshold

    Returns:
        D {list} -- the list of boxes after implement NMS
        S {list} -- the list of scores corresponding boxes in D
    """

    D=[]
    S=[]
    while len(boxes) != 0:
        # index of max score
        m=max(range(len(scores)),key=lambda i:scores[i])
        # box of max score
        M=boxes[m]
        D.append(M)
        boxes.remove(M)
        S.append(scores[m])
        scores.remove(scores[m])
        for bi in boxes:
            if IoU(M,bi) > threshold:
                scores.remove(scores[boxes.index(bi)])
                boxes.remove(bi)

    return D,S


def SoftNMS(boxes:list,scores:list,threshold:float,method:str='linear'):
    """Improvement for NMS:SoftNMS
    
    Arguments:
        boxes {list} -- the list of initial detection boxes
        scores {list} -- the list of scores that contains corresponding detection scores
        threshold {float} -- the NMS threshold
    
    Keyword Arguments:
        method {str} -- improve method,optional:'linear' or 'gaussian' (default: {'linear'})
    
    Returns:
        D {list} -- the list of boxes after implement NMS
        S {list} -- the list of scores corresponding boxes in D
    """

    D=[]
    S=[]
    while len(boxes) != 0:
        # index of max score
        m=max(range(len(scores)),key=lambda i:scores[i])
        # box of max score
        M=boxes[m]
        D.append(M)
        boxes.remove(M)
        S.append(scores[m])
        scores.remove(scores[m])
        for bi in boxes:
            if method == 'linear':
                scores[boxes.index(bi)]*=1-IoU(M,bi)
            elif method == 'gaussian':
                scores[boxes.index(bi)]*=exp(-pow(IoU(M,bi),2)/1.0)# TODO : value '1.0' is param sigma and should be determined.
            else:
                raise AttributeError(f"unknown method:{method}")

    for di in D:
        index=D.index(di)
        if S[index] <= threshold:
            D.remove(D[index])
            S.remove(S[index])

    return D,S

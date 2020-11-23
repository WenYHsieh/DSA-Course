from typing import List
import math
from math import atan2
from random import randint

# def create_points(ct,min,max):
# 	return [[randint(min,max),randint(min,max)] \
# 			for _ in range(ct)]

class Airport:
    '''
    1. find convex hull of all given points
    2. calcuate the average distance of each edges of convext hull to all points
    3. return the smallest averge distance to airplane 
    '''
    '''
    to find convex hull:
    - find reference point
    - ccw (pointA, pointB, pointC)
    - polar angel order comparator :
        polarOrder(pointA, pointB)
    '''

    @staticmethod
    def polarAngle(p0,p1=None):
        if p1==None: 
            p1=anchor
        ySpan=p0[1]-p1[1]
        xSpan=p0[0]-p1[0]
        return atan2(ySpan,xSpan)

    @staticmethod
    def distance(p0,p1=None):
        if p1==None: 
            p1=anchor
        ySpan=p0[1]-p1[1]
        xSpan=p0[0]-p1[0]
        return ySpan**2 + xSpan**2

    @staticmethod
    def det(p1,p2,p3):
        return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

    @staticmethod
    def quickSort(a):
        if len(a)<=1: 
            return a

        smaller,equal,larger=[],[],[]
        pivAng=Airport.polarAngle(a[randint(0,len(a)-1)]) # select random pivot

        for pt in a:
            ptAng=Airport.polarAngle(pt) # calculate current point angle
            if ptAng<pivAng:  
                smaller.append(pt)
            elif ptAng==pivAng: 
                equal.append(pt)
            else: 				  
                larger.append(pt)

        return Airport.quickSort(smaller) + sorted(equal,key=Airport.distance) + Airport.quickSort(larger)

    @staticmethod
    def grahamScan(points):
        if len(points) <=2:
            return points
        else: 
            global anchor
            minIdx=None
            for i,(x,y) in enumerate(points):
                if minIdx==None or y<points[minIdx][1]:
                    minIdx=i
                if y==points[minIdx][1] and x<points[minIdx][0]:
                    minIdx=i

            anchor=points[minIdx]

            sortedPts=Airport.quickSort(points)
            del sortedPts[sortedPts.index(anchor)]

            hull=[anchor,sortedPts[0]]
            for s in sortedPts[1:]:
                while Airport.det(hull[-2],hull[-1],s)<=0:
                    del hull[-1] # backtrack
                    if len(hull)<2: break
                hull.append(s)

        return hull


    @staticmethod
    def distanceToline(p1, p2, Ps):
        # lineParas: output from linearEquationParas
        # Ps: [houses] for all point except p1,p2 (that form edge)
        A = p2[1]-p1[1] # y2-y1
        B = p1[0]-p2[0] # x1-x2
        C = (p1[1]*p2[0]) - (p2[1]*p1[0]) # (y1x2-y2x1)

        sumX = sum([p[0] for p in Ps])
        sumY = sum([p[1] for p in Ps])
        Psum = [sumX, sumY]
        n = len(Ps)
        distance=abs((Psum[0]*A)+(Psum[1]*B)+(n*C))/math.sqrt((A**2)+(B**2))
        averageDistance = distance/n

        return averageDistance

    def airport(self, houses: List[List[int]]) -> float:

        if len(houses)<=2: 
            return 0
        else:
        
            convextHull = Airport.grahamScan(houses)
            cyCH = convextHull+[convextHull[0]]
            meanDisToEdges = []

            for i in range(len(cyCH)-1):
                edgeP1 = cyCH[i]
                edgeP2 = cyCH[i+1]
                meanDisToEdges.append(Airport.distanceToline(edgeP1, edgeP2, houses))

            ans = min(meanDisToEdges)

        return ans


# pts=create_points(60000,0,1000000)
if __name__ == "__main__":
    # print(Airport().airport(pts))
    print(Airport().airport([[0,0],[1,0]]))
    print(Airport().airport([[0,0],[1,0],[0,1]]))
    print(Airport().airport([[0,0],[2,0],[0,2],[1,1],[2,2]]))
    print(Airport().airport([[1,1],[2,2],[0,2],[2,0],[2,4],[3,3],[4,2],[4,1],[4,0]]))
    print(Airport().airport([[0,0],[1,1],[2,2]]))
    """
    # house: [[0, 0], [1, 0]]
    ..
    **
    0.0
    # house: [[0, 0], [1, 0], [0, 1]]
    *.
    **
    # Convex: [[0, 0], [1, 0], [0, 1]]
    0.2357022603955159
    # house: [[0, 0], [2, 0], [0, 2], [1, 1], [2, 2]]
    *.*
    .*.
    *.*
    # Convex: [[0, 0], [2, 0], [2, 2], [0, 2]]
    1.0
    # house: [[1, 1], [2, 2], [0, 2], [2, 0], [2, 4], [3, 3], [4, 2], [4, 1], [4, 0]]
    ..*..
    ...*.
    *.*.*
    .*..*
    ..*.*
    # Convex: [[0, 2], [2, 0], [4, 0], [4, 2], [2, 4]]
    1.3356461422412562
    """

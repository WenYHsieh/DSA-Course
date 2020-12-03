from typing import List
import heapq


class Cluster:
    def cluster(self, points: List[List[int]], cluster_num: int) -> List[List[float]]:
        """ 
        Cluster the points to cluster_num clusters.
        Output the sorted center coordination of those clusters.
        """ 
        return sorted([[0,0]])


if __name__ == "__main__":
    print(Cluster().cluster([[0,0], [1,0], [3,0], [0,1]], 2)) 
    # [[0.3333333333333333, 0.3333333333333333], [3, 0]] 
    # [0,0], [1,0], [0,1] are in same cluster
    # [3,0] are in another cluster

    print(Cluster().cluster([[0,3], [3,3], [4,7], [9,0], [9,4]], 3)) 
    # [[1.5, 3.0], [4, 7], [9.0, 2.0]]

    print(Cluster().cluster([[0,1], [0,2], [3,1], [3,2]], 2)) 
    # [[0.0, 1.5], [3.0, 1.5]]
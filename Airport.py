from typing import List
import math


class Airport:
    def airport(self, houses: List[List[int]]) -> float:
        """
        Find the best place to build airport and
        calculate the average distance from all the house to airport

        Parameters:
            houses(list[list[int]]): List of houses.
                Each house contains [x,y] coordination.

        Returns:
            distance(float)
        """
        return 0.


if __name__ == "__main__":
    print(Airport().airport([[0,0],[1,0]]))
    """
    0.0
    """
    print(Airport().airport([[0,0],[1,0],[0,1]]))
    """
    *.
    **
    # Convex: [[0, 0], [1, 0], [0, 1]]
    0.2357022603955159
    """
    print(Airport().airport([[0,0],[2,0],[0,2],[1,1],[2,2]]))
    """
    *.*
    .*.
    *.*
    # Convex: [[0, 0], [2, 0], [2, 2], [0, 2]]
    1.0
    """
    print(Airport().airport([[1,1],[2,2],[0,2],[2,0],[2,4],[3,3],[4,2],[4,1],[4,0]]))
    """
    ..*..
    ...*.
    *.*.*
    .*..*
    ..*.*
    # Convex: [[0, 2], [2, 0], [4, 0], [4, 2], [2, 4]]
    1.3356461422412562
    """
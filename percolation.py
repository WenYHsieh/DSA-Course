class Percolation:
    def __init__(self, N :int):
        """ Create N-by-N grid, with all sites blocked """
        pass

    def open(self, i :int, j :int):
        """ Open site (row i, column j) if it is not open already """
        pass

    def isOpen(self, i :int, j :int) -> bool:
        """ Is site (row i, column j) open? """
        return True

    def isFull(self, i :int, j :int) -> bool:
        """ Is site (row i, column j) full? """
        return True
            
    def precolates(self) -> bool:
        """ Does the system percolate? """
        return True
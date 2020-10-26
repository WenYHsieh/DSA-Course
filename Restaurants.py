import functools
from typing import List


class Restaurant(object): # construct restaurant object
    def __init__(self, id :int, rate :int, price :int, distance :int):
        self.Id = id
        self.Rate = rate
        self.Price = price
        self.Distance = distance

    def getID(self) -> int:
        return self.Id
    
    def getDistance(self):
        return self.Distance

    def __lt__(self, b) -> bool: # Comparable in Object -> define behaviour of '<', less than operator
        """
        The natural comparator of Restaurant
        
        The comparator should compare the restaurants by the value calculated from the formula
        `distance * price / rate`
        and return True if the value of `self` is lower than `b`
        If the value is the same, keep the same order as input.
        """
        # b is a restaurant Object
        int1 = (self.Distance*self.Price)/self.Rate
        int2 = (b.Distance/b.Price)/b.Rate
        if int1 < int2: 
            return True

    @staticmethod
    def comparator1(a, b) -> int: 
        """
        Compare two restaurants by restaurant object    
        ->對兩個 restaurant 進行指定的比較
        Order the restaurants by the rate in increasing order,
        distance in increasing order (if tied),and 
        id in decreasing order (if tied again).
        -> 基本上是針對 rate (評分)由低分在前高分在後，如果相同就比 distance (距離)，距離近在前遠的在後, 再相同比 id ，大的在前小的在後
        
        Parameters:
            a(Restaurant): The restaurant object
            b(Restaurant): The restaurant object
            -> 傳入 a, b 兩個餐廳物件

        Returns:
            result(int): -1 for restaurant a has smaller order, 1 for restaurant b has smaller order, 0 for equal.
            -> a 在前 回傳-1, b 在前回傳1, 都相同回傳0
        """
        if a.Rate < b.Rate: return -1
        if a.Rate > b.Rate: return 1
        if a.Rate == b.Rate:
            if a.Distance < b.Distance: return -1
            if a.Distance > b.Distance: return 1
        if a.Distance == b.Distance:
            if a.Id < b.Id: return -1
            if a.Id > b.Id: return 1

        return 0

class Restaurants(object):
    def __init__(self, restaurants :List[Restaurant]):
        
        self.rests = dict(zip(list(range(len(restaurants))),[rest for rest in restaurants]))
        

    def filter(self, min_price: int, max_price :int, min_rate: int) -> List[int]:
        """
        Filter the restaurants, output the list of restaurant id that meet the condition.

        Output the list in in the increasing order of distance;
        If the distance is the same, order the restaurant ids from the highest to the lowest.

        Returns:
            restaurants (List[int]): The list of restaurant id.
        """
        
        return 0


if __name__ == "__main__":
    rests = [
        # id, rate, price, distance
        Restaurant(20, 1, 20, 12),
        Restaurant(15, 3, 19, 11),
        Restaurant(19, 4, 19, 12),
        Restaurant(18, 5, 20, 11),
    ]
    r = Restaurants(rests)
    print(r.filter(0, 25, 3)) 
    print(r.filter(0, 25, 4)) 
    print(r.filter(0, 20, 1)) 
    print(r.filter(0, 10, 1))
    print(r.filter(0, 19, 1))
    print(r.filter(19, 19, 3))

    # case6 測是物件實作的comparator
    # rests = [
    #     # id, rate, price, distance
    #     Restaurant(3, 2, 3, 8),
    #     Restaurant(0, 2, 4, 6),
    #     Restaurant(2, 4, 5, 12),
    #     Restaurant(1, 5, 6, 11),
    # ]
    # print([i.getID() for i in sorted(rests)])
    # print([i.getID() for i in sorted(rests, key=functools.cmp_to_key(Restaurant.comparator1))])


#Output:
# [18, 15, 19]
# [18, 19]
# [18, 15, 20, 19]
# []
# [15, 19]
# [15, 19]
# [3, 0, 1, 2]
# [0, 3, 2, 1]

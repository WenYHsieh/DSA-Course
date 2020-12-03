class Calendar:
    def __init__(self):
        ...

    def book(self, start: int, end: int) -> bool:
        """
        Book the event where interval started from start(included) to end(excluded)

        If availble: book it and return True
        else: return False
        """
        return True


if __name__ == "__main__":
    a = Calendar()
    print(a.book(10, 20))
    print(a.book(15, 25))
    print(a.book(20, 25))
    print(a.book(17, 21))
    print(a.book(0, 3)) 
    print(a.book(2, 6)) 
    print(a.book(3, 6)) 
    """ 
    True
    False  #[15, 20) is unavailable
    True
    False  #[17, 21] is unavailable
    True
    False  #[2, 3) is unavailable
    True
    """

    a = Calendar()
    print(a.book(5, 15))
    print(a.book(0, 18))
    print(a.book(24, 29))
    print(a.book(13, 25))
    print(a.book(18, 22))
    print(a.book(15, 18))
    """ 
    True
    False  #[5, 15) is unavailable
    True
    False  #[24, 25] is unavailable
    True
    True
    """
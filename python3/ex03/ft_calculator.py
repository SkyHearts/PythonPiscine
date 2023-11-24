class calculator:
    """Calculator class"""
    def __init__(self, num: list) -> None:
        """Init the list"""
        self.num_list = num

    def __add__(self, object) -> None:
        """add number operator overload"""
        new_list = []
        for item in self.num_list:
            item = item + object
            new_list.append(item)
        self.num_list = new_list
        print(new_list)

    def __mul__(self, object) -> None:
        """mul number operator overload"""
        new_list = []
        for item in self.num_list:
            item *= object
            new_list.append(item)
        self.num_list = new_list
        print(new_list)

    def __sub__(self, object) -> None:
        """sub number operator overload"""
        new_list = []
        for item in self.num_list:
            item -= object
            new_list.append(item)
        self.num_list = new_list
        print(new_list)

    def __truediv__(self, object) -> None:
        """div number operator overload"""
        try:
            assert object != 0, "Unable to divide 0"
            new_list = []
            for item in self.num_list:
                item /= object
                new_list.append(item)
            self.num_list = new_list
            print(new_list)
        except AssertionError as msg:
            print(msg)

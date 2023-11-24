class calculator:
    """Calculator class"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product"""
        listA = [A * B for A, B in zip(V1, V2)]
        dot = sum(listA)
        print("Dot product is:", dot)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add vector"""
        listA = [float(A) + float(B) for A, B in zip(V1, V2)]
        print("Add Vector is:", listA)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Sub vector"""
        listA = [float(A) - float(B) for A, B in zip(V1, V2)]
        print("Sous Vector is:", listA)

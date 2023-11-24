import numpy as np


def isnumeric(s):
    """Check if is numeric"""
    try:
        float(s)
        return True
    except ValueError:
        return False


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Return bmi list if list is correct with correct type"""
    try:
        np_height = np.array(height)
        np_weight = np.array(weight)
        assert isinstance(np_height, list), "Wrong type given"
        assert isinstance(np_weight, list), "Wrong type given"
        assert len(np_height) > 0, "empty list given"
        assert len(np_weight) > 0, "empty list given"
        assert np_height.size == np_weight.size, "incorrect list size"
        flag = False
        height_num = np.frompyfunc(isnumeric, 1, 1)(np_height)
        weight_num = np.frompyfunc(isnumeric, 1, 1)(np_weight)
        if all(height_num) and all(weight_num):
            flag = True
        assert flag is True, "incorrect type"
        np_height = np.asarray(np_height, dtype=float)
        np_weight = np.asarray(np_weight, dtype=float)
        np_bmi = np_weight / (np_height * np_height)
        return list(np_bmi)
    except AssertionError as msg:
        print("AssertionError:", msg)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check list against a limit and return a bool list"""
    try:
        assert isinstance(bmi, list), "Wrong type given"
        assert len(bmi) > 0, "empty list given"
        np_bmi = np.array(bmi)
        np_bool = (np_bmi > limit)
        return list(np_bool)
    except AssertionError as msg:
        print("AssertionError:", msg)


# def main():
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))


# if __name__ == "__main__":
#     """Testing"""
#     main()

def NULL_not_found(object: any) -> int:
    # your code here
    if (object is None):
        print("Nothing : None", type(object))
    elif (isinstance(object, float) and object != object):
        print("Cheese : nan", type(object))
    elif (isinstance(object, bool) and object is False):
        print("Fake: : False", type(object))
    elif (isinstance(object, int) and object == 0):
        print("Zero : 0", type(object))
    elif (isinstance(object, str) and len(object.strip()) == 0):
        print("Empty :", type(object))
    else:
        print("Type not Found")
        return (1)
    return 0
    # your code here

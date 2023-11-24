import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load and return CSV data using pandas lib"""
    try:
        ret = pd.read_csv(path)
        assert path.endswith('.csv') is True, "Wrong Extension"
        return ret
    except FileNotFoundError:
        print("Path is bad")
        return None
    except Exception as msg:
        print("Parse error: ", msg)
        return None
    # except AssertionError as msg:
    #     print(msg)
    #     return None

import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load and return CSV data using pandas lib"""
    try:
        # # Read and set index to country
        # ret = pd.read_csv(path, index_col='country')
        # Read only
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

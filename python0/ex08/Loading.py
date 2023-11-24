def ft_tqdm(lst: range) -> None:
    """Mimics a loading bar in TQDM package"""
    iteration = 0
    length = 50
    total = len(lst)
    while iteration <= total:
        percent = ("{:.0f}").format(100 * iteration / total)
        filledLength = int(length * iteration / total)
        bar = '█' * filledLength + ' ' * (length - filledLength)
        print(f'{percent}%|{bar}|{iteration}/{total}', end="\r")
        if (iteration == total):
            print()
        yield iteration
        iteration += 1

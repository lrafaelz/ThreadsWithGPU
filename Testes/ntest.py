from multiprocessing import Pool

def add(x, y):
    """Return the sum of the tuple of two arguments"""
    return x + y

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

if __name__ == "__main__":
    with Pool() as pool:
        result = pool.starmap(add, zip(a, b))

    print(result)
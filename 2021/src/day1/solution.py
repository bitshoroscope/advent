import csv

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.readline(chunk_size).splitlines()
        if not data:
            break
        yield data[0]

def get_depth_counter():
    with open('input.txt') as f:
        counter = -1
        currentValue = 0
        for value in read_in_chunks(f):
            if int(value) > currentValue:
                counter += 1
            currentValue = int(value)
        return counter

print(get_depth_counter())



import re
import os

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def file_sort(fname):
    f = os.listdir(fname)
    return sorted(f, key=numericalSort)

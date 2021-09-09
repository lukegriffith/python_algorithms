'''
Quicksort, runs at worst O(n), at best O(n log n)
'''
import time
import subprocess
import select
import os
import threading

LOG_FILE = 'apache_logs.txt'

'''modified quicksort to accept the tuple of url to count'''
def quicksort(xs):
    """Given indexable and slicable iterable, return a sorted list"""
    if xs: # if given list (or tuple) with one ordered item or more: 
        pivot = xs[0]
        # below will be less than:
        below = [i for i in xs[1:] if i[0] < pivot[0]] 
        # above will be greater than or equal to:
        above = [i for i in xs[1:] if i[0] >= pivot[0]]
        return quicksort(below) + [pivot] + quicksort(above)
    else: 
        return xs # empty list

def process_line(line, url_dict, tick):
    split_line = str(line).split(' ')
    url = split_line[6]
    if url in url_dict:
        url_dict[url] = url_dict[url] + 1
    else:
        url_dict[url] = 1

    tick['tick'] = tick['tick'] + 1


def tail_file():
    f = subprocess.Popen(['tail','-F',LOG_FILE],\
            stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p = select.poll()
    p.register(f.stdout)
    url_dict = {}
    tick = {} 
    tick['tick'] = 0

    def thread_function(url_dict, f, tick):
        while True:
            if p.poll(1):
                line = f.stdout.readline()
                if line == '':
                    continue
                process_line(line, url_dict, tick)


        time.sleep(1/100.0)
    x = threading.Thread(target=thread_function, args=(url_dict, f, tick))
    x.start()

    while True:
        url_array = [(url_dict[key], key) for key in url_dict.keys()]
        sorted_urls = quicksort(url_array)
        for u in sorted_urls[::-1][0:5]:
            print(u[0], u[1])
        print(tick['tick'])
        print("==="*10)
        time.sleep(5)


tail_file()
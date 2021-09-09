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

'''
def linearsort(url_dict,url_array):
    url_dict_copy = url_dict.copy()
    top_five = []
    for i in range(0,5):
        highest_value = 0
        highest_value_key = None
        for url in url_array:
            value = url[0]
            key = url[1]
            if value > highest_value:
                highest_value = value
                highest_value_key = key
        if highest_value_key == None:
            continue
        top_five.append((highest_value, highest_value_key))
        print(top_five)
        del(url_dict_copy[highest_value_key])
    return top_five
'''

def process_line(line, url_dict, tick):
    split_line = str(line).split(' ')
    url = split_line[6]
    if url in url_dict:
        url_dict[url] = url_dict[url] + 1
    else:
        url_dict[url] = 1

    tick['tick'] = tick['tick'] + 1

def display_results(url_dict, tick):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        ''' quick sort '''
        start = time.time()
        url_array = [(url_dict[key], key) for key in url_dict.keys()]
        sorted_urls = quicksort(url_array)
        end = time.time()
        quick_sort_time = end - start
        ''' linear sort '''
        #start = time.time()
        #url_array = [(url_dict[key], key) for key in url_dict.keys()]
        #sorted_urls = linearsort(url_dict,url_array)
        #end = time.time()
        #linear_sort_time = end - start
        for u in sorted_urls[::-1][0:5]:
            print(u[0], u[1])
        print(tick['tick'])
        print("==="*10)
        print("Quicksort Runtime:", quick_sort_time)
        #print("Linear sort Runtime:", linear_sort_time)
        time.sleep(1)


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

    display_results(url_dict, tick)

tail_file()

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

def main():
    f = open('apache_logs.txt','r')
    file = f.read()
    lines = file.split('\n')
    url_dict = {}
    for line in lines:
        if line == '':
            continue
        split_line = line.split(' ')
        url = split_line[6]
        if url in url_dict:
            url_dict[url] = url_dict[url] + 1
        else:
            url_dict[url] = 1
    url_array = [(url_dict[key], key) for key in url_dict.keys()]
    sorted_urls = quicksort(url_array)
    for u in sorted_urls[::-1][0:5]:
        print(u[0], u[1])
main()

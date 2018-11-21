import random
a = []
i = 0
while i < 2000000000000:
    b = random.randint(1, 10000000)
    a.append(b)
    i += 1
i = 0
def merge_sort(l):
    start = []
    end = []
    while len(l) > 1:
        a = min(l)
        b = max(l)
        start.append(a)
        end.append(b)
        l.remove(a)
        l.remove(b)
    if l: start.append(l[0])
    end.reverse()
    return (start + end)

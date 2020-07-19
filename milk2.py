"""
ID: kanghee2
LANG: PYTHON3
PROG: milk2
"""
fin = open('milk2.in')
fout = open('milk2.out','w')
time_list = []
for line in fin.readlines():
    if ' 'in line:
        time_list.append(tuple(int(x) for x in line.strip().split()))

def FindTimeOverlap(time1tuple, time2tuple):
    time1_start, time1_end = time1tuple
    time2_start, time2_end = time2tuple
    if time1_start <= time2_start <= time1_end or time2_start <= time1_start <= time2_end:
        return (min(time1_start, time2_start), max(time1_end, time2_end))
    else:
        return [(time1tuple, time2tuple)]
time_list.sort()
overlap_list = [time_list[0]]
idle_list = []
overlap = time_list[0]
for item in time_list:
    current_overlap = FindTimeOverlap(overlap, item)
    if type(current_overlap) == tuple:
        overlap = current_overlap
    else:
        overlap_list.append(overlap)
        idle_list += current_overlap
        overlap = item
if overlap != item:
    overlap_list.append(overlap)

largest_overlap = 0
for overlaps in overlap_list:
    start, end = overlaps
    if end-start > largest_overlap:
        largest_overlap = end-start
largest_idle = 0
for idling in idle_list:
    tuple1, tuple2= idling
    start1, end1 = tuple1
    start2, end2 = tuple2
    if start2-end1 > largest_idle:
        largest_idle = start2-end1

fout.write(f"{largest_overlap} {largest_idle}\n")


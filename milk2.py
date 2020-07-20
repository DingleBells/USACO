"""
ID: kanghee2
LANG: PYTHON3
PROG: milk2
"""
fin = open('milk2.in')
fout = open('milk2.out','w')
lines_number = int(fin.readline())
time_list = []
for line in range(lines_number):
    line = fin.readline()
    time_list.append(tuple(int(x) for x in line.strip().split()))
def FindTimeOverlap(time1tuple, time2tuple):
    time1_start, time1_end = time1tuple
    time2_start, time2_end = time2tuple
    if time1_start <= time2_start <= time1_end or time2_start <= time1_start <= time2_end:
        return True, [(min(time1_start, time2_start), max(time1_end, time2_end))]
    else:
        return False, [time2_start-time1_end]
time_list.sort()
overlap_list = []
idle_list = []
overlap = time_list[0]
for item in time_list[1:]:
    condition, [current_overlap] = FindTimeOverlap(overlap, item)
    if condition:
        overlap = current_overlap
    else:
        overlap_list.append(overlap)
        idle_list.append(current_overlap)
        overlap = item
overlap_list.append(overlap)

largest_overlap = 0
for overlaps in overlap_list:
    start, end = overlaps
    if end-start > largest_overlap:
        largest_overlap = end-start
largest_idle = max(idle_list)

fout.write(f"{largest_overlap} {largest_idle}\n")


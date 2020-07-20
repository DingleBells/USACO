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
def IsOverlap(time1tuple, time2tuple):
    time1_start, time1_end = time1tuple
    time2_start, time2_end = time2tuple
    if time1_start <= time2_start <= time1_end or time2_start <= time1_start <= time2_end:
        return True
    return False
time_list.sort()
largest_overlap = 0
largest_idle = 0
overlap = time_list[0]
for item in time_list[1:]:
    item_start, item_end = item
    overlap_start, overlap_end = overlap
    if IsOverlap(item, overlap):
        overlap = min(item_start, overlap_start), max(overlap_end, item_end)
    else:
        if overlap_end-overlap_start > largest_overlap:
            largest_overlap = overlap_end-overlap_start
        if item_start-overlap_end > largest_idle:
            largest_idle = item_start-overlap_end
        overlap = item

fout.write(f"{largest_overlap} {largest_idle}\n")


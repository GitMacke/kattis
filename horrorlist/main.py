import sys
from collections import defaultdict
line_number = 0
neighbor_dict = defaultdict(list)
for i in sys.stdin:
    if line_number == 0:
        n,h,l = [int(x) for x in i.split(' ')]
        continue
    if line_number == 1:
        horror_ids = [int(x) for x in i.split(' ')]
        continue
    a,b = [int(x) for x in i.split(' ')]
    neighbor_dict[a].append(b)
    neighbor_dict[b].append(a)
    line_number+=1
horror_score_dict = dict()
for id in range(n):
    
    

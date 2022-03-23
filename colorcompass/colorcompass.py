from collections import defaultdict

import sys

import random
import time
def genInput(n=1000):
    line_list = []
    prev_ids = set()
    for _ in range(n):
        r = str(random.randint(0,359))
        g = str(random.randint(0,359))
        b = str(random.randint(0,359))
        identity = random.randint(0,2e31)
        if identity not in prev_ids:
            line_list.append(r+" "+g+" "+b+" "+str(identity))
        prev_ids.add(identity)
    return line_list

def find_uniqueness(color_dict,color_angle,id_ignore = None):
    #color_dict[color_angle] = set(x for x in color_dict[color_angle] if x in card_dict.keys())
    if len(color_dict[color_angle]) > 1:
        affected = []
        if len(color_dict[color_angle]) == 2:
            affected = [x for x in color_dict[color_angle] if x != id_ignore]
        return 0, affected

    right_neighbor = 0
    left_neighbor = 0
    left_found = False
    right_found = False
    affected = []

    for i in range(360):
        if not left_found:
            try_left_angle = (color_angle+1+i) % 360
            try_left = color_dict[try_left_angle]
            if try_left:
                left_neighbor = try_left_angle
                left_found = True
                if len(try_left) == 1:
                    affected += list(try_left)
        if not right_found:
            try_right_angle = (color_angle-1-i) % 360
            try_right = color_dict[try_right_angle]
            if try_right:
                right_neighbor = try_right_angle
                right_found = True
                if len(try_right) == 1:
                    affected += list(try_right)

        if left_found and right_found:
            return (left_neighbor-right_neighbor) % 360, affected

    return 0, []


def check_if_full(color_dict):
    for k in range(360):
        if len(color_dict[k]) < 2:
            return False
    return True


first = True
counter = 0

card_dict = dict()
red_dict = defaultdict(set)
green_dict = defaultdict(set)
blue_dict = defaultdict(set)
neighbor_dict = defaultdict(set)
uniqueness_dict = dict()
zero_dict = dict()

line = sys.stdin.readline()
while line:
    if first:
        n_cards = int(line)
        first = False
    else:
        red, green, blue, card_id = [int(x) for x in line.split(' ')]
        red_dict[red].add(card_id)
        green_dict[green].add(card_id)
        blue_dict[blue].add(card_id)
        card_dict[card_id] = (red, green, blue)
        counter += 1
    if counter == n_cards:
        break
    line = sys.stdin.readline()


# lines = genInput(1000)
# t0 = time.time()
#
# for line in lines:
#     red, green, blue, card_id = [int(x) for x in line.split(' ')]
#     red_dict[red].add(card_id)
#     green_dict[green].add(card_id)
#     blue_dict[blue].add(card_id)
#     card_dict[card_id] = (red, green, blue)

zero_ids = []
for k,v in card_dict.items():
    r_uniqueness, r_neighbors = find_uniqueness(red_dict, v[0],id_ignore = k)
    g_uniqueness, g_neighbors = find_uniqueness(green_dict, v[1],id_ignore = k)
    b_uniqueness, b_neighbors = find_uniqueness(blue_dict, v[2],id_ignore = k)
    uniqueness = r_uniqueness + g_uniqueness + b_uniqueness
    neighbors = r_neighbors + g_neighbors + b_neighbors
    uniqueness_dict[k] = (uniqueness,-k, set(neighbors))
    if uniqueness==0:
        zero_ids.append(k)

zero_ids.sort()

while uniqueness_dict.keys():
    if zero_ids:
        least_unique_id = zero_ids.pop()
    else:
        least_unique_id = min(uniqueness_dict,key=uniqueness_dict.get)

    neighbors = uniqueness_dict.pop(least_unique_id)[2]
    sys.stdout.write(str(least_unique_id))
    sys.stdout.write("\n")
    r, g, b = card_dict.pop(least_unique_id)
    red_dict[r].remove(least_unique_id)
    green_dict[g].remove(least_unique_id)
    blue_dict[b].remove(least_unique_id)

    neighbors_neighbors = set()
    if len(red_dict[r]) == 1:
        neighbors_neighbors.add(list(red_dict[r])[0])
    if len(green_dict[g]) == 1:
        neighbors_neighbors.add(list(green_dict[g])[0])
    if len(blue_dict[b]) == 1:
        neighbors_neighbors.add(list(blue_dict[b])[0])

    if not uniqueness_dict.keys():
        break
    for neighbor in neighbors: ##update affected cards
        #if neighbor in card_dict.keys():
        r, g, b = card_dict[neighbor]
        r_uniqueness, r_neighbors = find_uniqueness(red_dict, r, id_ignore=neighbor) ## potential optimization: only update affected color of uniqueness
        g_uniqueness, g_neighbors = find_uniqueness(green_dict, g, id_ignore=neighbor)
        b_uniqueness, b_neighbors = find_uniqueness(blue_dict, b, id_ignore=neighbor)
        uniqueness = r_uniqueness + g_uniqueness + b_uniqueness
        new_neighbors = r_neighbors + g_neighbors + b_neighbors
        uniqueness_dict[neighbor] = (uniqueness, -neighbor, set(new_neighbors))
        if uniqueness>0 and zero_ids and neighbor in zero_ids:
            zero_ids.remove(neighbor)
    for neighbor in neighbors_neighbors: ##update affected cards
        #if neighbor in card_dict.keys():
        r, g, b = card_dict[neighbor]
        r_uniqueness, r_neighbors = find_uniqueness(red_dict, r, id_ignore=neighbor) ## potential optimization: only update affected color of uniqueness
        g_uniqueness, g_neighbors = find_uniqueness(green_dict, g, id_ignore=neighbor)
        b_uniqueness, b_neighbors = find_uniqueness(blue_dict, b, id_ignore=neighbor)
        uniqueness = r_uniqueness + g_uniqueness + b_uniqueness
        new_neighbors = r_neighbors + g_neighbors + b_neighbors
        uniqueness_dict[neighbor] = (uniqueness, -neighbor, set(new_neighbors))
        if uniqueness>0 and zero_ids and neighbor in zero_ids:
            zero_ids.remove(neighbor)
        for neighbor_neighbor in new_neighbors: ##update affected cards
        #if neighbor in card_dict.keys():
            r, g, b = card_dict[neighbor_neighbor]
            r_uniqueness, r_neighbors = find_uniqueness(red_dict, r, id_ignore=neighbor_neighbor) ## potential optimization: only update affected color of uniqueness
            g_uniqueness, g_neighbors = find_uniqueness(green_dict, g, id_ignore=neighbor_neighbor)
            b_uniqueness, b_neighbors = find_uniqueness(blue_dict, b, id_ignore=neighbor_neighbor)
            uniqueness = r_uniqueness + g_uniqueness + b_uniqueness
            new_neighbors = r_neighbors + g_neighbors + b_neighbors
            uniqueness_dict[neighbor_neighbor] = (uniqueness, -neighbor_neighbor, set(new_neighbors))
            if uniqueness>0 and zero_ids and neighbor in zero_ids:
                zero_ids.remove(neighbor)

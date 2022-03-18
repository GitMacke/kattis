from collections import defaultdict

import sys


def find_uniqueness(color_dict,color_angle):

    if len(color_dict[color_angle]) > 1:
        affected = []
        if len(color_dict[color_angle]) == 2:
            affected = list(color_dict[color_angle])
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
for k,v in card_dict.items():

    r_uniqueness, r_neighbors = find_uniqueness(red_dict, v[0])
    g_uniqueness, g_neighbors = find_uniqueness(green_dict, v[1])
    b_uniqueness, b_neighbors = find_uniqueness(blue_dict, v[2])
    uniqueness = r_uniqueness + g_uniqueness + b_uniqueness
    neighbors = r_neighbors + g_neighbors + b_neighbors
    uniqueness_dict[k] = (uniqueness,-k, set(neighbors))

full = False

if all([check_if_full(red_dict),check_if_full(green_dict),check_if_full(blue_dict)]): #if all angles have more than 2 cards all uniquenesses = 0 and highest id gets removed
    full = True
    all_ids = list(card_dict.keys())
    all_ids.sort()

while uniqueness_dict.keys():
    if full:
        least_unique_id = all_ids.pop()
    else:
        least_unique_id = min(uniqueness_dict, key=uniqueness_dict.get)
        #least_unique_id = max([k for k, v in uniqueness_dict.items() if v[0] == min_val])

    sys.stdout.write(str(least_unique_id))
    sys.stdout.write("\n")

    r, g, b = card_dict.pop(least_unique_id)
    red_dict[r].remove(least_unique_id)
    green_dict[g].remove(least_unique_id)
    blue_dict[b].remove(least_unique_id)

    neighbors = uniqueness_dict.pop(least_unique_id)[2]

    if len(red_dict[r]) == 1:
        full = False
        neighbors.add(list(red_dict[r])[0])
    if len(green_dict[g]) == 1:
        full = False
        neighbors.add(list(green_dict[g])[0])
    if len(blue_dict[b]) == 1:
        full = False
        neighbors.add(list(blue_dict[b])[0])

    for neighbor in neighbors: ##update affected cards
        if neighbor in card_dict.keys():
            r, g, b = card_dict[neighbor]
            r_uniqueness, r_neighbors = find_uniqueness(red_dict, r)
            g_uniqueness, g_neighbors = find_uniqueness(green_dict, g)
            b_uniqueness, b_neighbors = find_uniqueness(blue_dict, b)
            uniqueness = r_uniqueness + g_uniqueness + b_uniqueness
            new_neighbors = r_neighbors + g_neighbors + b_neighbors
            uniqueness_dict[neighbor] = (uniqueness, -neighbor, set(new_neighbors))
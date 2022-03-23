import random
def genInput(n=1000):
    line_list = [n]
    prev_ids = set()
    for _ in range(n):
        r = str(random.randint(0,359))
        g = str(random.randint(0,359))
        b = str(random.randint(0,359))
        identity = random.randint(0,2e31)
        if identity not in prev_ids:
            line_list.append(str(identity)+" "+r+" "+g+" "+b)
        prev_ids.add(identity)
    return line_list

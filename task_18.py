

def count_vershin(n, s):
    level=0
    valley=0
    for direction in s:
        if direction == "U":
            level += 1
            if level == 0:
                valley += 1
        else:
            level -= 1
    return valley


print(count_vershin(8, 'UDDDUDUU'))

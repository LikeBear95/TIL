paddings = [3,7]
outers = [8,3,5]
inners = [5,3,8,5]

for padding in paddings:
    for outer in outers:
        for inner in inners:
            print(padding, outer, inner)

# 3 8 5   7 8 5
# 3 8 3   7 8 3
# 3 8 8   7 8 8
# 3 8 5   7 8 5

# 3 3 5   7 3 5
# 3 3 3   7 3 3
# 3 3 8   7 3 8
# 3 3 5   7 3 5

# 3 5 5   7 5 5
# 3 5 3   7 5 3
# 3 5 8   7 5 8
# 3 5 5   7 5 5


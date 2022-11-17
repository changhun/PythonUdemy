l = list(range(15))
print(l)

if len(l) < 10:
    start = 0
else:
    start = -10
sub_list = l[start:]
print(sub_list)
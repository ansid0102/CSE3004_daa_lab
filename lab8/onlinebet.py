# verdict in the sense the count list
verdict = list()
s, p = [int(i) for i in input().split()]

for i in range(s):
    a, b = [int(i) for i in input().split()]
    verdict.append((a,'l'))
    verdict.append((b,'r'))

points = input().split()
for i in points:
    verdict.append((int(i),'p'))

verdict.sort()

segment_count = 0
point_segment_map = dict()
for i in verdict:
    if i[1] == 'l':
        segment_count += 1
    elif i[1] == 'r':
        segment_count -= 1
    else:
        point_segment_map[i[0]] = segment_count

temp = ''
for i in points:
    temp += str(point_segment_map[int(i)]) + ' '
print("Output")
print(temp[:-1])


data = [1, 2, 2, 3, 1]
count1 = []
count2 = []
count3 = []
for i in data:
    if i not in count1:
        count1.append(i)
        count2.append(data.count(i))
for w in range(len(count1)):
    count3.append(count1[w] * count2[w])
print(min(count3))

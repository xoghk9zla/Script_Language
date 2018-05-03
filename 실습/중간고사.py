def delete_overlap(list):
    result = list[:]
    for i in list:
        overlap_count = result.count(i)
        if overlap_count > 1:
            result.remove(i)
    return result
    pass

def count_overlap(data):
    global index
    nonoverlap = delete_overlap(data)
    nonoverlap.sort()
    dict1 = dict()
    dict1[index].keys = nonoverlap
    dict1[index].values = data.count(nonoverlap)
    index += 1
    print(dict1)
    pass

s = input("영단어들 입력: ")

index = 0

list1 = []

for i in s:
    if i != " ":
        list1.append(i)

count_overlap(list1)
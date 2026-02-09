list1 = ["HELLO", "World", "PYTHON", "code"]
for list2 in list1:
    if list2.isupper():
        print(list2[::-1])
    else:
        print(list2)

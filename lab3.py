print("ex_1\n")
def ex_1(list1: list, list2: list):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    reunion = set1.union(set2)
    adiffb = set1.difference(set2)
    bdiffa = set2.difference(set1)

    return (intersection, reunion, adiffb, bdiffa)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

print(ex_1(l1, l2))
print("\n")

print("ex_2\n")
def ex_2(string):
    to_return = dict()
    for i in string:
        to_return[i] = to_return.get(i, 0) + 1
    return to_return


print(ex_2("Ana has apples."))
print("\n")

print("ex_3\n")
def ex_3(ct1, ct2):
    if isinstance(ct1, dict) and isinstance(ct2, dict):  # dictionaries
        if len(ct1) != len(ct2):
            return False

        for key, value in ct1.items():
            if not ex_3(value, ct2.get(key)):
                return False
        return True

    elif isinstance(ct1, type(ct2)):  # now checking if the args have the same type
        if isinstance(ct1, list) or isinstance(
            ct1, set
        ): 
            if len(ct1) != len(ct2):
                return False

            for i, j in zip(ct1, ct2):  
                if not ex_3(i, j):
                    return False

            return True

        elif isinstance(ct1, tuple):
            return ex_3(ct1[0], ct2[0]) and ex_3(
                ct1[1], ct1[1]
            )

        elif ct1 == ct2:  # basic types
            return True

    return False


print("basic", ex_3("aaa", "aaa"))

print("simple1", ex_3({"a": "dd", 3: 5}, {"a": "dd", 3: 5}))
print("simple2", ex_3({"a": "dd", 3: 5}, {"a": "dd", 3: 6}))

print("medium1", ex_3({"a": [1, 2], 3: {1, 2}}, {"a": [1, 2], 3: {1, 2}}))
print("medium2", ex_3({"a": [1, 2], 3: {1, 2}}, {"a": [1, 2], 3: {1, 4}}))

print(
    "hard1",
    ex_3(
        [
            {"a": [1, 2], 3: {1, 2}},
            {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
            [{3, 4, 5, 6}, {"a": "b", "c": 55}],
        ],
        [
            {"a": [1, 2], 3: {1, 2}},
            {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
            [{3, 4, 5, 6}, {"a": "b", "c": 55}],
        ],
    ),
)
print(
    "hard2",
    ex_3(
        [
            {"a": [1, 2], 3: {1, 2}},
            {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
            [{3, 4, 5, 6}, {"a": "b", "c": 55}],
        ],
        [
            {"a": [1, 2], 3: {1, 2}},
            {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
            [{3, 4, 5, 6}, {"a": "b", "c": 53}],
        ],
    ),
)


print(
    "harerest",
    ex_3(
        {
            "a": [
                {"a": [1, 2], 3: {1, 2}},
                {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
                [{3, 4, 5, 6}, {"a": "b", "c": 55}],
            ],
            "b": [
                {"a": [1, 2], 3: {1, 2}},
                {"a": [1, 2], 3: [{1, 4}, {"inside": "this"}]},
                [{3, 4, 5, 6}, {"a": "b", "c": 55}],
            ],
        },
        {
            "a": [
                {"a": [1, 2], 3: {1, 2}},
                {"a": [1, 2], 3: [{1, 4}, {"inside": "always"}]},
                [{3, 4, 5, 6}, {"a": "b", "c": 55}],
            ],
            "b": [
                {"a": [1, 2], 3: {1, 2}},
                {"a": [1, 2], 3: [{1, 4}, {"inside": "this"}]},
                [{3, 4, 5, 6}, {"a": "b", "c": 55}],
            ],
        },
    ),
)

print("ex_4\n")
def ex_4(tag, content, **attributes):
    to_return = "<" + tag

    for key, value in attributes.items():
        to_return += " "
        to_return += key
        to_return += '=\\"'
        to_return += value
        to_return += '\\"'

    to_return += "> "
    to_return += content
    to_return += " </" + tag + ">"

    return to_return


print(
    ex_4(
        "a",
        "Hello there",
        href=" http://python.org ",
        _class=" my-link ",
        id=" someid ",
    )
)
print("\n")

print("ex_5\n")
def ex_5(rules, d):
    for key, value in d.items():
        rule_not_found_flag = True

        for rule in rules:
            if key == rule[0]:
                prefix_pos = value.find(rule[1])

                if prefix_pos != 0:
                    return False
                mid_pos = value.find(rule[2], prefix_pos + 1)
                suffix_pos = value.rfind(rule[3])
                if suffix_pos != len(value) - len(rule[3]):
                    return False
                if mid_pos == -1 or mid_pos > suffix_pos:
                    return False
                
                rule_not_found_flag = False

        if(rule_not_found_flag):
            return False
        
    return True


print("rule not found: ",
    ex_5(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        {"key1": "come inside, it's too cold out", "key3": "this is not valid"},
    )
)
print("rule found + valid dict: ",
    ex_5(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        { "key1": "come inside, it's too cold out","key2": "start this middle in the winter"},
    )
)
print("rule found + invalid dict: ",
    ex_5(
        {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
        { "key1": "come inside, it's too cold out","key2": "star this middle in the winter"},
    )
)

print("\n")

print("ex_6\n")

def ex_6(list):
    unique_elements = set(list)
    return (len(unique_elements), len(list) - len(unique_elements))

print(ex_6([1, 2, 1, 3, 2]))
print("\n")

print("ex_7\n")

def ex_7(*sets):
    # processed=[0]*len(sets)
    to_return = dict()
    for i in range(0,len(sets)):
        for j in range(i+1,len(sets)):
            # if i != j:
                to_return[str(sets[i]) + " | " + str(sets[j])] = sets[i].union(sets[j])
                to_return[str(sets[i]) + " & " + str(sets[j])] = sets[i].intersection(sets[j])
                to_return[str(sets[i]) + " - " + str(sets[j])] = sets[i].difference(sets[j])
                to_return[str(sets[j]) + " - " + str(sets[i])] = sets[j].difference(sets[i])

    return to_return

print(ex_7({1, 2}, {2, 3}, {3,4}))
print("\n")

print("ex_8\n")

def ex_8(mapping):
    to_return = list()
    current_key = mapping["start"]
    
    while current_key != "start":
        to_return.append(current_key)
        current_key = mapping[current_key]
        if current_key in to_return:
            break
    
    return to_return
        

print(
    ex_8(
        {
            "start": "a",
            "b": "a",
            "a": "6",
            "6": "z",
            "x": "2",
            "z": "2",
            "2": "2",
            "y": "start",
        }
    )
)
print("\n")

print("ex_9\n")

def my_function(*positional_args, **keyword_args):

	keyword_values = [value for key,value in keyword_args.items()]

	return len([i for i in positional_args if i in keyword_values])
	

print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))

print("\n")


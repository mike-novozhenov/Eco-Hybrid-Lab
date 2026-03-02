# a, b, c = 1, 2.5, "Text"
#
# print ("{} {}".format( "text", a))
# print (type(a), type(b), type(c))


# values = [1, 2, "text"]
# print(values[-1])
# print(values[0:3])
# print(values)
#
# values.insert(1, "new text")
# print(values)
#
# first_value = values[0]
# values.insert(0, 2)
# print(values)
#
# first_value = values[0]
# if first_value == 2:
#     print("correct")
# else:
#     print("incorrect")
#
# values.append(12)
# print(values)
#
# values[0] = "new_value"
# print(values)
#
# del values[-1]
# print(values)


# print(len(values))
# assert len(values) == 3, f"Wrong value, actual is {len(values)}"


# new_list = [1, 2, 3]
# for i, x in enumerate(new_list):
#     print(f"Checking statuses for: {x}")
#     assert x == 1, f"It is the {i})"

candidates = [
    {"id": 1, "name": "Mikhail", "status": "Active"},
    {"id": 2, "name": "Alex", "status": "Pending"}
]

for person in candidates:
    # На каждом круге person — это новый словарь
    current_status = person["status"]
    assert current_status != "Pending", f"Empty status for candidate {person['name']}"
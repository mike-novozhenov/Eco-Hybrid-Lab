# user_age = 25
# user_name = "UA"
# product_price = 25.99
# online_status = True
#
# print (user_age, type(user_age), "//", user_name, type(user_name), "//", product_price, type(product_price), "//",online_status, type(online_status))

apple = 3
# text = "need to buy"
#
# total = "text" * apple
# print(f'What we need to buy: {apple}, {total}')


# a = (1, 6, 3)
#
# for i in a:
#     i = i + 1
#     print(*i)
#     print(i)


# a = 7
# b = 7
#
# if b > a:
#     print("b больше")
# elif b < a:
#     print("a больше")
# else:
#     print("Они равны")


# def my_way(number):
#     a = 5 * number
#     b = 3 * number
#     return a + b
#
#
# number = int(input("Enter a number: "))
# result = my_way(number)
# print(result)


# def calc(num):
#     x = num * 2
#     y = num * num
#     return x, y
#
# your_num = int(input("Enter a number: "))
# # result = calc(your_num)
# x,y = calc(your_num)
# print(x)
# print(y)




# response_data = [
#     {"id": 101, "name": "Sample_A", "status": "active"},
#     {"id": 102, "name": "Sample_B", "status": "inactive"},
#     {"id": 103, "name": "Sample_C", "status": "active"}
# ]
#
# for item in response_data:
#     if item["status"] == "active":
#         print(item["name"])
#     else:
#         pass


# users = ["Mikhail", "Admin", "Tester"]
#
# # Твой код тут:
# users.append("Newcomer")
# print(users)


samples = [
    {"id": 501, "status": "active"},
    {"id": 502, "status": "inactive"},
    {"id": 503, "status": "active"}
]

ids_to_test = []

# ТВОЙ КОД:
# 1. Пройди циклом по samples
# 2. Если статус "active"
# 3. Добавь id в список ids_to_test
for sample in samples:
    if sample["status"] == "active":
        ids_to_test.append(sample["id"])
    else: pass

print(ids_to_test)
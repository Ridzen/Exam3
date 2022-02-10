# ____________________________________4_____________________________________

a = [2, 3, 4, 23, 35, 23]
b = [1000, 4, 2, 2, 23, 45, 57]

same_things = list(set(a) & set(b))

print(f"So in the end, we will have : {same_things}, like the similar numbers in both lists")

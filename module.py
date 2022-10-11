from collections import Counter
phones = ["Iphone", "Samsung", "LG", "Iphone", "Iphone", "LG"]

count = Counter(phones)
print(count["LG"])

text = "Ехал Грека через реку, видит Грека в реке рак"
count = Counter(text.lower().replace(" ", ""))
print(count)
from functools import reduce


nums = [2, 5, 8, 11, 14]
print(list(filter(lambda even: even % 2 == 0, nums)))

names = ["alice", "BOB", "ChArLiE"]
names = list(map(lambda sentence: sentence[0].capitalize() + sentence[1:].lower(), names))
print(names)

nums = [3, 6, 9, 12]
result = reduce(lambda x, y: x * y, nums)
print(result)

words = ["python", "is", "really", "powerful"] 
print(sorted(words, key=lambda word: len(word), reverse=True))

people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 19}, {"name": "Charlie", "age": 30}]
people = list(filter(lambda person: person["age"] >= 21, people))
people = list(map(lambda person: person["name"], people))
print(people)
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
print("\033c")
text = [2, 3, 4, 5, 6]
Result = []
if len(text) % 2 == 0:
    L = len(text)//2
if len(text) % 2 > 0:
    L = len(text)//2+1
for i in range(L):
    X = text[i] * text[(len(text)-1-i)]
    Result.append(X)
print(Result)
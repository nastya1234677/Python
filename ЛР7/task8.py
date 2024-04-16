#Подсчет гласных и согласных 
user_input = input("Введите английское слово: ")
user_input = user_input.lower()
vowels_count = 0
consonants_count = 0
vowels_set = set("aeiou")
consonants_set = set("bcdfghjklmnpqrstvwxyz")
for char in user_input:
    if char in vowels_set:
        vowels_count += 1
    elif char in consonants_set:
        consonants_count += 1
print("Количество гласных:", vowels_count)
print("Количество согласных:", consonants_count)

seconds = int(input("number of seconds: "))

days_words = "день ", "дні", "днів"

days = seconds // 86400
hours = (seconds // 3600) % 24
minutes = (seconds // 60) % 60
seconds = seconds % 60

if days % 10 == 1 and days % 100 != 11:
    day_word = days_words[0]
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = days_words[1]
else:
    day_word = days_words[2]

print(f"{days} {day_word},  {hours}:{minutes}:{seconds}")

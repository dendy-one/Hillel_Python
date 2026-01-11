import string

span = input("ведите две букви через дефиз: ")

letters = string.ascii_letters
start = letters.index(span[0])
end = letters.index(span[2])

print(letters[start : end + 1])

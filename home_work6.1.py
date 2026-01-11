import string

span = input("Enter two letters separated by a hyphen: ")

letters = string.ascii_letters
start = letters.index(span[0])
end = letters.index(span[2])

print(letters[start : end + 1])

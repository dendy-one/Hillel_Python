import string

span = input("Enter two letters separated by a hyphen: ")

letters = string.ascii_letters
start_index = letters.index(span[0])
end_index = letters.index(span[2])

print(letters[start_index : end_index + 1])

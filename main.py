print("hello world")


def sort_on(dict):
    return dict["num"]


def printResult(dict):
    print("The '"+str(dict["letter"]) +
          "' character was found "+str(dict["num"]) + " times")


with open("./books/frankenstein.txt") as f:
    file__contents = f.read()

words = file__contents.split()

character_dict = {

}

for word in words:
    for letter in word:
        if letter.lower() in character_dict:
            character_dict[letter.lower()] = character_dict[letter.lower()]+1
        else:
            character_dict.update({letter.lower(): 1})

result = []

for character in character_dict:
    if character.isalpha():
        result.append({"letter": character, "num": character_dict[character]})

result.sort(reverse=True, key=sort_on)
for character in result:
    printResult(character)

print(len(words))

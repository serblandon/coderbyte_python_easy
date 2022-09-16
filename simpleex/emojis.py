def emoji_convert(string):
    output = ""
    emojis = {
        ":)": "😀",
        ":(": "☹"
    }
    string_split = string.split(" ")
    for word in string_split:
        output += emojis.get(word, word) + ' '
    return output

string = input("Type a sentence with :) or :(")
print(emoji_convert(string))

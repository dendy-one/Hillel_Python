import string

data = [
    ["Python Community"],
    ["i like python community!"],
    ["Should, I. subscribe? Yes!"],
    [
        (
            "Whispers of Dawn The night dissolves in silver air,As morning"
            "stirs the sky awake. A quiet hope begins to flare! In every"
            " breath the new days take?"
        )
    ],
]

for list in data:
    for text in list:
        cleaned = "".join(el for el in text if el not in string.punctuation)
        words = cleaned.split()
        capitalized = [word.capitalize() for word in words]
        hashtag = "#" + "".join(capitalized)
        if len(hashtag) > 140:
            hashtag = hashtag[:140]

    print(hashtag)

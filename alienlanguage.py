alien_dict = {
    "a": "zor",
    "b": "vak",
    "c": "mii",
    "d": "tek",
    "e": "lun",
    "f": "rax",
    "g": "plo",
    "h": "zik",
    "i": "nor",
    "j": "xel",
    "k": "qop",
    "l": "tri",
    "m": "wex",
    "n": "bor",
    "o": "yul",
    "p": "faz",
    "q": "kim",
    "r": "dex",
    "s": "vii",
    "t": "rok",
    "u": "zen",
    "v": "gal",
    "w": "tor",
    "x": "jix",
    "y": "nex",
    "z": "kri"
}

print("👽 Alien Language Translator")
print("Type 'exit' to quit.")

while True:
    text = input("\nEnter text: ").lower()

    if text == "exit":
        print("Goodbye, Earthling! 👋")
        break

    translated = []

    for char in text:
        if char in alien_dict:
            translated.append(alien_dict[char])
        else:
            translated.append(char)

    print("\n👾 Alien Translation:")
    print(" ".join(translated))

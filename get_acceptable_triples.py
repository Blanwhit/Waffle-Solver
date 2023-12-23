import itertools


def get_acceptable_triples(raw_grid: dict, raw_words: list):
    print("Acceptable words search started")

    # Get all acceptable letters
    acceptable_letters = ""
    for i in raw_grid.keys():
        if raw_grid[i] != "BLANK":
            acceptable_letters += raw_grid[i]["letter"]

    # Get all acceptable words
    acceptable_words = []
    for word in raw_words:
        acceptable_letters_copy = acceptable_letters
        for letter_index in range(5):
            if word[letter_index] in acceptable_letters_copy:
                if letter_index == 4:
                    acceptable_words.append(word)
                acceptable_letters_copy = acceptable_letters_copy.replace(
                    word[letter_index], "", 1
                )
            else:
                break
    print(f"Acceptable words search done. Found {len(acceptable_words)} of them")

    # Get all possible triples
    acceptable_triples = []
    print("Possible triples search started")
    possible_triples = list(itertools.combinations(acceptable_words, 3))
    print(f"Possible triples search done. Found {len(possible_triples)} of them")

    # Get all acceptable triples
    print("Acceptable triples filtering started")
    counter = 0
    for tu in possible_triples:
        # Counter
        counter += 1
        if counter % 1000000 == 0:
            print(
                f"Searched {counter//1000000}m triples, found {len(acceptable_triples)} acceptable ones"
            )

        # Check if the words can be made from the acceptable letters list
        if canMakeStr2(acceptable_letters, tu[0] + tu[1] + tu[2]):
            acceptable_triples.append(tu)

    print(
        f"Acceptable triple search done. Found {len(acceptable_triples)} possible triples."
    )
    return acceptable_triples, acceptable_letters, acceptable_words


# Function to check if string 2 can be made from string 1
def canMakeStr2(s1, s2):
    count = {s1[i]: 0 for i in range(len(s1))}

    for i in range(len(s1)):
        count[s1[i]] += 1

    for i in range(len(s2)):
        if count.get(s2[i]) == None or count[s2[i]] == 0:
            return False
        count[s2[i]] -= 1
    return True

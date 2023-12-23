import itertools


# Get all full grids by checking permutations of each triple
# If all the words both down and across are in the acceptable words list, the grid gets added to full_grids
def get_good_grids(triples: list, letters: str, fn_words: list):
    print("Full grid search started")

    full_grids = []
    counter = 0
    for triple in triples:
        # Counter
        counter += 1
        if counter % 1000 == 0:
            print(
                f"Checked {counter}/{len(triples)} triples, found {len(full_grids)} full grids"
            )

        # Calculate remaning letters
        remaining_letters = letters
        for letter in triple[0] + triple[1] + triple[2]:
            remaining_letters = remaining_letters.replace(letter, "", 1)

        # Calculate full grids
        for triple_permutation in list(itertools.permutations(triple)):
            for letter_permutation in list(itertools.permutations(remaining_letters)):
                # If all words across are in the words list, add grid to full_grids
                if (
                    triple_permutation[0][0]
                    + letter_permutation[0]
                    + triple_permutation[1][0]
                    + letter_permutation[1]
                    + triple_permutation[2][0]
                    in fn_words
                    and triple_permutation[0][2]
                    + letter_permutation[2]
                    + triple_permutation[1][2]
                    + letter_permutation[3]
                    + triple_permutation[2][2]
                    in fn_words
                    and triple_permutation[0][4]
                    + letter_permutation[4]
                    + triple_permutation[1][4]
                    + letter_permutation[5]
                    + triple_permutation[2][4]
                    in fn_words
                ):
                    full_grids.append(
                        (
                            triple_permutation,
                            (
                                triple_permutation[0][0]
                                + letter_permutation[0]
                                + triple_permutation[1][0]
                                + letter_permutation[1]
                                + triple_permutation[2][0],
                                triple_permutation[0][2]
                                + letter_permutation[2]
                                + triple_permutation[1][2]
                                + letter_permutation[3]
                                + triple_permutation[2][2],
                                triple_permutation[0][4]
                                + letter_permutation[4]
                                + triple_permutation[1][4]
                                + letter_permutation[5]
                                + triple_permutation[2][4],
                            ),
                        )
                    )

    print(f"Full Grid search done. Found {len(full_grids)} possible full grids.")
    return list(set(full_grids))

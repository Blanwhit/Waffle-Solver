import itertools


# Get all full grids by checking permutations of each triple
# If all the words both down and across are in the acceptable words list, the grid gets added to full_grids
def get_good_grids(
    triples_horizontal: list, triples_vertical: list, letters: str, fn_words: list
):
    print("Full grid search started")

    full_grids = []
    counter = 0
    for triple in triples_horizontal:
        # Counter
        counter += 1
        if counter % 1000 == 0:
            print(
                f"Checked {counter}/{len(triples_horizontal) + len(triples_vertical)} triples, found {len(full_grids)} full grids"
            )

        # Calculate remaning letters
        remaining_letters = letters
        for letter in triple[0] + triple[1] + triple[2]:
            remaining_letters = remaining_letters.replace(letter, "", 1)

        # Calculate full grids
        for letter_permutation in list(itertools.permutations(remaining_letters)):
            # If all words across are in the words list, add grid to full_grids
            if (
                triple[0][0]
                + letter_permutation[0]
                + triple[1][0]
                + letter_permutation[1]
                + triple[2][0],
                triple[0][2]
                + letter_permutation[2]
                + triple[1][2]
                + letter_permutation[3]
                + triple[2][2],
                triple[0][4]
                + letter_permutation[4]
                + triple[1][4]
                + letter_permutation[5]
                + triple[2][4],
            ) in triples_vertical:
                full_grids.append(
                    (
                        triple,
                        (
                            triple[0][0]
                            + letter_permutation[0]
                            + triple[1][0]
                            + letter_permutation[1]
                            + triple[2][0],
                            triple[0][2]
                            + letter_permutation[2]
                            + triple[1][2]
                            + letter_permutation[3]
                            + triple[2][2],
                            triple[0][4]
                            + letter_permutation[4]
                            + triple[1][4]
                            + letter_permutation[5]
                            + triple[2][4],
                        ),
                    )
                )

    print(f"Full Grid search done. Found {len(full_grids)} possible full grids.")
    return list(set(full_grids))

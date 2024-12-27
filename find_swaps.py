import mapping


def make_letters_unique(letters):
    letter_count = {}
    result = []

    for letter in letters:
        current_count = letter_count.get(letter, 0) + 1
        letter_count[letter] = current_count
        result.append(f"{letter}{current_count}")

    return result


def convert_grid_to_string(grid: dict[str, dict[str, str]]) -> str:
    grid_string = ""
    for i in grid.values():
        if i != "BLANK":
            grid_string += i["letter"]
    return grid_string


def generate_all_unique_combinations(letters):
    letter_freq = {}
    for letter in letters:
        letter_freq[letter] = letter_freq.get(letter, 0) + 1

    def get_possible_numbers(letter):
        return list(range(1, letter_freq[letter] + 1))

    def generate_combinations(current_position, used_numbers):
        if current_position == len(letters):
            return [[]]

        current_letter = letters[current_position]
        available_numbers = get_possible_numbers(current_letter)
        results = []

        used_for_letter = used_numbers.get(current_letter, set())

        for num in available_numbers:
            if num not in used_for_letter:
                new_used = {k: v.copy() for k, v in used_numbers.items()}
                if current_letter not in new_used:
                    new_used[current_letter] = set()
                new_used[current_letter].add(num)

                next_combinations = generate_combinations(
                    current_position + 1, new_used
                )

                for combo in next_combinations:
                    results.append([f"{current_letter}{num}"] + combo)

        return results

    return generate_combinations(0, {})


def find_min_swaps(s1: str, s2: str) -> list[tuple[int, int]]:
    from sympy.combinatorics.partitions import Partition
    from sympy.combinatorics.permutations import Permutation

    l1, l2 = list(s1), list(s2)
    l1_unique = make_letters_unique(l1)

    l2_options = generate_all_unique_combinations(l2)

    perms_options = []

    for option in l2_options:
        perm = [l1_unique.index(i) for i in option]
        perms_options.append(Permutation(perm))

    transposition_options = []

    for perm in perms_options:
        transposition_options.append(perm.transpositions())

    min_transpositions = 1000
    for transposition_sequence in transposition_options:
        if len(transposition_sequence) < min_transpositions:
            min_transpositions = len(transposition_sequence)
            best_transposition_sequence = transposition_sequence
            if len(transposition_sequence) <= 10:
                break

    return best_transposition_sequence


def find_min_grid_swaps(g1: dict, g2: dict) -> list[tuple[int, int]]:
    s1, s2 = convert_grid_to_string(g1), convert_grid_to_string(g2)
    swaps = find_min_swaps(s1, s2)
    swaps_readable = []
    for tu in swaps:
        swaps_readable.append(
            (
                mapping.str_index_to_grid_pos[tu[0]],
                mapping.str_index_to_grid_pos[tu[1]],
            )
        )
    return swaps_readable

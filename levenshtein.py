import os
import sys

def import_data(FILE_PATH):
    if not os.path.exists(FILE_PATH): raise Exception("FILE WAS NOT FOUND")

    f = open(FILE_PATH, "r")
    f_string = f.read()

    f_cat = f_string.split("#")
    f_lines_1 = [e for e in f_cat[0].split("\n") if not e == ""]
    f_lines_2 = [e for e in f_cat[1].split("\n") if not e == ""]

    f.close()

    return (f_lines_1, f_lines_2)

def import_data_kattis():
    f_string = sys.stdin.read()
    f_cat = f_string.split("#")
    f_lines_1 = [e for e in f_cat[0].split("\n") if not e == ""]
    f_lines_2 = [e for e in f_cat[1].split("\n") if not e == ""]
    return (f_lines_1, f_lines_2)

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def find_closest_matches(incorrect, correct_list):
    correct_words = []
    min_distance = float('inf')

    for correct_word in correct_list:
        distance = levenshtein_distance(incorrect, correct_word)
        if distance < min_distance:
            min_distance = distance
            correct_words = [correct_word]
        elif distance == min_distance:
            correct_words.append(correct_word)

    return (correct_words, min_distance)

def main(KATTIS=False):
    if KATTIS: 
        (val1, val2) = import_data_kattis()
        for incorrect_word in val2:
            (closest_match, distance) = find_closest_matches(incorrect_word, val1)
            print(f"{incorrect_word} ({distance}) {' '.join(closest_match)}")
    else: 
        (val1, val2) = import_data("./testfall/testmedordlista4.indata")
        print(val1)
        print(val2)

        for incorrect_word in val2:
            (closest_match, distance) = find_closest_matches(incorrect_word, val1)
            print(f"Incorrect: {incorrect_word}, Closest Match: {' '.join(closest_match)}, Distance: {distance}")


if __name__ == "__main__":
    main(True)
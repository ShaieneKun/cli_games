TRIES = 7
# continue_playing_ = True

def game():
    tries = TRIES
    word = read_word()
    word = word.lower()
    word_list = [char for char in word]

    discovered_word_list = []
    for char in word_list:
        if char == " ":
            discovered_word_list.append(" ")
        else:
            discovered_word_list.append("_")


    selected_chars = []
    words_match = False
    while (not words_match):
        if tries == 0:
            print(f"Poxa, não conseguiram dessa vez. A palavra era: {word}")
            break

        print_word_and_tries(discovered_word_list, tries, selected_chars)
        char = read_char()
        selected_chars = add_to_selected_chars(char, selected_chars)

        matches = match_char_in_word(user_char=char, word_list=word_list)

        if not matches:
            tries -= 1
            continue

        discovered_word_list = reveal_matched_chars(
            discovered_word_list,
            matches,
            char
        )

        words_match = compare_word_with_discovered(word_list, discovered_word_list)

        if words_match:
            print(f"Parabéns, vocês descobriram a palavra ou frase: {word}")
            break


def compare_word_with_discovered(word_list, discovered_word_list):
    return "".join(discovered_word_list) == "".join(word_list)


def read_word():
    word = input("Escreva a palavra ou frase a ser advinhada: ")
    print("\n"*1100)
    return word


def read_char():
    print("Escreva a próxima letra: ")
    char = "  "
    while len(char) != 1:
        char = input()

        if len(char) == 1:
            break
        print("Digite uma letra apenas:")
    char = char.lower()
    return char


def match_char_in_word(user_char, word_list):
    matches = []
    for index, word_char in enumerate(word_list):
        if word_char == user_char:
            matches.append(index)

    return matches


def reveal_matched_chars(discovered_word_list, matches, char):
    for index in matches:
        discovered_word_list[index] = char

    return discovered_word_list


def add_to_selected_chars(char, selected_chars):
    if char not in selected_chars:
        selected_chars.append(char)

    return selected_chars


def print_word_and_tries(discovered_word_list, tries, selected_chars):
    discovered_word = "".join(discovered_word_list)
    selected_chars_str = " ".join(selected_chars)
    print("\n"*50)
    print(f"{discovered_word} \n{tries} tentativas restantes \nletras já usadas: {selected_chars_str}\n")

def continue_playing():
    char = ""

    while char not in ("s", "n"):
        char = input("Continuar jogando? (s/n): ")
        char = char.lower()
        if char not in ("s", "n"):
            print('Digite "s" ou "n" apenas')

    return True if char == "s" else False

if __name__ == "__main__":
    game()
    while continue_playing():
        game()
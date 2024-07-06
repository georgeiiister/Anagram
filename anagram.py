import random


def words() -> tuple:
    return 'hello', 'world', 'town', 'city', 'address'


def main():
    err_words = tuple()

    for i, word in enumerate(tuple(i.upper() for i in words())):

        new_word = ''
        for j in word:
            while True:
                _ = random.choice(word)
                if not new_word or _ not in new_word or word.count(_) >= new_word.count(_) + 1:
                    break
            new_word += _

        if input(f'>> {new_word} <<\n You this known words? '
                 f'If "yes", type it on the keypad >>> ').upper() != word:
            err_words += (word,)

    print(f'do you this known words: {len(words()) - len(err_words)} from {len(words())} '
          f'error_word: {str(err_words) if len(err_words) > 0 else 0}'
          )


if __name__ == '__main__':
    main()

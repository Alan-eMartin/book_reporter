import os


class Book:
    def __init__(self, book):
        self.name = book
        self.__file_path = f"./books/{book.lower()}.txt"

    def __get_content(self):
        if not os.path.exists(self.__file_path):
            raise FileNotFoundError(f"cannot find {self.name} in our library")
        with open(self.__file_path) as file:
            content = file.read()
            return content

    def __get_word_count(self):
        contents = self.__get_content()
        total_words = len(contents.split())
        if total_words == 0:
            raise Exception(
                "Oh no, there are 0 words! It seems a dog ate your books pages 🐕🥣📖"
            )
        return total_words

    def __get_letter_counts(self):
        contents = self.__get_content()
        chars = [*contents]
        all_letters = []

        for char in chars:
            if char.isalpha():
                all_letters.append(char.lower())

        sorted_letters = sorted(all_letters)
        letter_counts = {}
        for letter in sorted_letters:
            if letter not in letter_counts:
                letter_counts.update({letter: 1})
            else:
                letter_counts[letter] += 1
        return letter_counts

    def read(self):
        has_content = self.__get_word_count()
        print(self.__get_content())

    def print_report(self):
        print(f"--- Begin report of {self.__file_path} ---")
        print(f"{self.__get_word_count()} words found in the document")
        print("")
        for letter, count in self.__get_letter_counts().items():
            print(f"The '{letter}' character was found {count} times")


def main():
    book = "Frankenstein"
    book = Book(book)
    book.print_report()

    # You can also try reading the book:
    # book.read()

    # throw some exceptions:
    # bad_book = Book("frankenWhaaat")
    # bad_book.read()
    # bad_book.print_report()


main()

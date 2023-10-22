from packages.library.library import Library


class Book:
    def __init__(self, name):
        self.name = name
        self.library = Library(self.name)

    def read(self):
        print(self.library.find_book())

    def __word_count(self):
        return len(self.library.find_book().split())

    def __letter_counts(self):
        contents = self.library.find_book()
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

    def print_report(self):
        print(f"\n--- Begin report of {self.name} ---")
        print(f"{self.__word_count()} words found in the document\n")
        print("--- Letter counts (a-z) ---")
        for letter, count in self.__letter_counts().items():
            print(f"The '{letter}' character was found {count} times")
        print("\n--- End of Report ---")

import os


class Library:
    LIB_PATH = "./book"

    def __init__(self, book_name):
        self.name = "Digital Library"
        self.book_name = book_name.strip()
        self.__file_path = os.path.join(self.LIB_PATH, f"{book_name.lower()}")

    # Returns book from library by name
    def find_book(self):
        try:
            with open(self.__file_path) as file:
                return file.read()

        except FileNotFoundError:
            raise FileNotFoundError(
                f"The book {self.book_name} does not exist in {self.name}"
            )

    def list_books(self):
        books = []
        files = os.listdir(self.LIB_PATH)

        if len(files) == 0:
            raise Exception(f"No books found in {self.name}")

        for file in files:
            book_file = os.path.splitext(file)[0].split("-")
            books.append(" ".join(book_file).title().strip())

        return books

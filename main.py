import os

from packages.book.book import Book


def main():
    book = Book("frankenstein.txt")
    book.print_report()


main()

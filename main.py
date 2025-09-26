import sys
from stats import get_word_count, get_sorted_chars


def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    return sys.exit(1)

  book_input = sys.argv[1]
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_input}...")
  print("----------- Word Count ----------")
  print(f"Found {get_word_count(book_input)} total words")
  print("--------- Character Count -------")
  sorted_chars = get_sorted_chars(book_input)
  for char_dict in sorted_chars:
    print(f"{char_dict["char"]}: {char_dict["num"]}")
  print("============= END ===============")

main()
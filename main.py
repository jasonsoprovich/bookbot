def get_book_text():
  book_input = "books/frankenstein.txt"
  with open(book_input) as book_content:
    book_content = book_content.read()
  return book_content

def get_num_words():
  book_content = get_book_text()
  words = book_content.split()
  return len(words)

def main():
  # book_content = get_book_text()
  num_words = get_num_words()
  output = f"Found {num_words} total words"
  print(output)

main()
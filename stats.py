def get_book_text():
  book_input = "books/frankenstein.txt"
  with open(book_input) as book_content:
    book_content = book_content.read()
  return book_content

def get_num_words():
  return len(get_book_text().split())

# def get_char_count():

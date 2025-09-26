def get_book_text():
  book_input = "books/frankenstein.txt"
  with open(book_input) as book_content:
    book_content = book_content.read()
  return book_content

def get_word_count():
  return len(get_book_text().split())

def get_char_count():
  char_list = list(get_book_text().lower())
  char_count = {}
  for char in char_list:
    if char.isalpha():
      char_count[char] = char_count.get(char, 0) + 1
  return char_count

def sort_on(dict):
  return dict["num"]

def get_sorted_chars():
  char_count = get_char_count()
  sorted_chars = []
  for char, count in char_count.items():
    sorted_chars.append({"char": char, "num": count})
  sorted_chars.sort(key=sort_on, reverse=True)
  return sorted_chars
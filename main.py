from stats import get_word_count, get_sorted_chars

def main():
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {get_word_count()} total words")
  print("--------- Character Count -------")
  sorted_chars = get_sorted_chars()
  for char_dict in sorted_chars:
    print(f"{char_dict["char"]}: {char_dict["num"]}")
  print("============= END ===============")

main()
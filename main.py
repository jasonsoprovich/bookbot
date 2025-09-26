from stats import get_word_count
from stats import get_char_count

def main():
  word_count = get_word_count()
  char_count = get_char_count()
  print(f"Found {word_count} total words")
  print(char_count)

main()
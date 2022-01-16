# file-uuid:    97375852-3f1e-4c9a-a498-4616f17ac17d
# project-uuid: 0d4d2fbf-596a-4fd9-9452-783d3dfa05d3
#-------------------------------------------------------------
#
from zero import *
from pathlib import Path

# SUI Definitions
# - lang: english
#-------------------------------------------------------------
No = False
Yes = True
show_data = No
#
#-------------------------------------------------------------

books_file = Path('./books.yaml')

with books_file.open('r') as file_stream:
  print(f'file {books_file.absolute()} is open') 
  bible_books = load(file_stream, Loader=Loader)
  book_keys  = bible_books.keys()

  for key in book_keys:
    book = bible_books[key]
    if show_data == Yes:
      print(f'- {key:20s}: {book}')
    else:
      print(f"    .add_book(named='{book[1]['name']}', abbreviation_as='{book[2]['abbreviation']}']\\" ) #', [{book['aliases']}]')\

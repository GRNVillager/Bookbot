from stats import get_text_number, get_letter_count,new_dic,sort_on
import sys

def checkinput():
     if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1) 
def get_book_text(path):
    with open(path) as b:
        file_contents = b.read()
        return file_contents
def main():
    path = sys.argv[1]
    text = get_book_text(path)
    count = get_text_number(text)
    abc = get_letter_count(text)
    listabc = new_dic(abc)
    end = f"Found {count} total words"
    listabc.sort(reverse=True,key=sort_on)
    print(end)
    for char, num in listabc:
        print(f"{char}: {num}")
checkinput()        
main()
def main():
    book_name = "frankenstein.txt"
    print_report(book_name)

def get_book_contents(file_name):
    with open(f"./books/{file_name}") as f:
        book_contents = f.read()
        return book_contents

def word_count(book_contents):
    words = book_contents.split()
    return len(words)

def character_count(book_contents):
    character_counts = {}
    characters = book_contents.lower()
    for char in characters:
        if char in character_counts:
            character_counts[char] +=1
        else:
            character_counts[char] = 1
    return character_counts

def sort_on(dict):
    return dict["count"]

def print_report(book_file_name):
    book_contents = get_book_contents(book_file_name)
    wc = word_count(book_contents)
    cc = character_count(book_contents)

    character_list = [{'char': char, 'count': count} for char, count in cc.items()]
    character_list.sort(key=sort_on,reverse=True)

    print(f"--Begin report of books/{book_file_name}")
    print(f"{wc} words found in the document")
    print("")
    for char_dict in character_list:
        if char_dict['char'].isalpha():
            print(f"The {char_dict['char']} was found {char_dict['count']} times")
    print("--- End report ---")
main()
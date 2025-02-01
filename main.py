def main():
    book = "books/frankenstein.txt"
    text = pages(book)
    count = words(text)
    char_dict = characters(text)
    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in document")
    print()
    report = lines(char_dict)
    print(f"--- End report---")

def pages(book):
    with open(book) as f:
        return f.read()

def words(text):
    w = text.split()
    return len(w)

def characters(text):
    low = text.lower()
    c = {}
    for y in low:
        if y in c:
            c[y] += 1
        else:
            c[y] = 1
    return c
def sort_on(dict):
    return dict["count"]

def lines(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    return char_list




main()
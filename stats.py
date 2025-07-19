def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def num_words(book):
    book = get_book_text(book)
    word_split = book.split()
    cnt = 0
    for word in word_split:
        cnt += 1
    return cnt

def sort_on(items):
    return items["num"]

def count_letters(file):
    book = get_book_text(file)
    booklist = list(book)
    letdict = {}
    for letters in booklist:
        lcase = letters.lower()
        if not lcase.isalpha():
            continue
        if lcase not in letdict:
            letdict[lcase] = 0
        letdict[lcase] += 1
    letlist = []
    for keys in letdict:
        letlist.append({"char": keys, "num": letdict[keys]})
    letlist.sort(reverse=True, key=sort_on)
    return letlist

def report(bookfile):
    totalwords = num_words(bookfile)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}")
    print("----------- Word Count ----------")
    print(f"Found {totalwords} total words")
    print("--------- Character Count -------")
    characterlist = count_letters(bookfile)
    for chars in characterlist:
        print(f"{chars["char"]}: {chars["num"]}")
    print("============= END ===============")
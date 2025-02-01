def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        def word_cnt(book):
            cnt=len(book.split())
            #print(cnt)
            return(cnt)
        words=word_cnt(file_contents)
        def char_cnt(book):
            book_char={}
            for char in book:
                if char.lower() not in book_char and char.isalpha():
                    book_char[char.lower()]=book.lower().count(char.lower())
            #print(book_char)
            return(book_char)
        charbook=char_cnt(file_contents)        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        print("")
        for char in charbook:
            counter=charbook[char]
            print(f"The '{char}' character was found {counter} times")



main()        



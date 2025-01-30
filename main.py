def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        def word_cnt(book):
            cnt=len(book.split())
            print(cnt)
            return
        word_cnt(file_contents)

main()        



def main():
    filename = 'books/frankenstein.txt'
    contents = read_book(filename)
    num_words = get_num_words(contents)
    chardic = count_chars(contents)
    report  = get_report(chardic,filename,num_words)
    print(report)
def read_book(filename):
        with open(filename,'r') as f:
            contents = f.read()
        return contents

def get_num_words(contents):
        return len(contents.split())

def count_chars(contents):
        chars = {}
        for i in contents:
            if i.lower() not in chars:
                chars[i.lower()]=1
            else:
                chars[i.lower()]+=1
        return chars

def get_report(chars,filename,num_words):
        letters = {k: v for k,v in chars.items() if k.isalpha()}
        startstr = f"--- Begin report of {filename} ---\n{num_words} words found in the document\n\n"
        midstr = ''
        for k,v in letters.items():
            midstr += f"The '{k}' character was found {v} times\n"
        endstr = "--- End report ---"
        return startstr + midstr + endstr

if __name__ == '__main__':
    main()
import deepl

def main():
    with open("abc.txt","r",encoding="utf8") as f:
        text_file=f.readlines()
    deepl.translate(text_file)

if __name__=="__main__":
    main()

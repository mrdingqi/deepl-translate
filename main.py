import deepl


def main():
    with open("abc.txt","r",encoding="utf8") as f:
        text_file=f.readlines()
    deepl.translate_by_file_path("abc.txt","abc.txt")
   

if __name__=="__main__":
    main()
    

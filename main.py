
from deepl import translate

def main(text,target_language,source_language ):

    kwargs = {}
    kwargs["formality_tone"] = "informal"

    try:
        print(translate(source_language, target_language, text, kwargs))
    except AssertionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    with open("E:\\deepl-translate\\abc.txt","r",encoding="utf8") as f:
        text=f.read()
    
    main(text,target_language="French", source_language="English")
from itertools import islice
import requests
from deepl.settings import API_URL
from deepl.settings import get_headers

from deepl.generators import genertate_body_basic
from deepl.extractors import extract_translated_sentences

from deepl.utils import abbreviate_language

headers = get_headers

def request_translation(source_language, target_language, text_list):
    data=genertate_body_basic(text_list,source_language, target_language,)
    # print("request_translation的data值如下")
    # print(data)

    response = requests.post(url=API_URL, headers=get_headers(), json=data)
    return response


def translate(text_list, target_language="FR",source_language="EN",  **kwargs):
    source_language = abbreviate_language(source_language)
    target_language = abbreviate_language(target_language)
    # print(f"输入的文本为{text_list}")
    # print("*"*50)

    response = request_translation(source_language, target_language, text_list)

    json_response = response.json()

    # print("返回的结果如下：")
    # print(json_response)

    translated_sentences = extract_translated_sentences(json_response)
    translated_text = "\n".join(translated_sentences)
    print(translated_text)

    return


def translate_by_file_path(input_file_path, output_file_path,batch_size=400):
    with open(input_file_path, 'r', encoding="utf8") as file:
        while True:
            batch = [line.strip() for line in islice(file, batch_size)]
            if not batch:
                break
            print("*" * 50)
            print("\n".join(batch))
            # 在这里对批处理的数据进行处理
            # 你可以在这里执行你想要的操作，比如写入其他文件或进行其他计算。
            pass

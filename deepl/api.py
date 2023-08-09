from itertools import islice
import requests
from deepl.settings import API_URL
from deepl.settings import get_headers

from deepl.generators import genertate_body_basic
from deepl.extractors import extract_translated_sentences

from deepl.utils import abbreviate_language

import time
def time_print(message):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{current_time}] {message}")

headers = get_headers

def request_translation(source_language, target_language, text_list):
    data=genertate_body_basic(text_list,source_language, target_language,)
    # print("request_translation的data值如下")
    # print(data)

    response = requests.post(url=API_URL, headers=get_headers(), json=data)
    return response


def translate(text_list, target_language="FR",source_language="EN",  **kwargs)->str:
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
    # print(translated_text)

    return translated_text


def translate_by_file_path(input_file_path, output_file_path,batch_size=400):
    seq=1
    with open(input_file_path, 'r', encoding="utf8") as file:
        while True:
            time_print(f"准备处理第{seq}批文字，每批{batch_size}行")
            
            batch = [line.strip() for line in islice(file, batch_size)]
            if not batch:
                break
            translated_text=translate(batch)
            with open(output_file_path,"a+",encoding="utf8") as file:
                file.write(translated_text)
            time_print(f"处理完毕第{seq}批文字，每批{batch_size}行")
            print("*"*50)
            print("\n")
            seq+=1
            # print("*" * 50)
            # print("\n".join(batch))
            # 在这里对批处理的数据进行处理
            # 你可以在这里执行你想要的操作，比如写入其他文件或进行其他计算。
            pass

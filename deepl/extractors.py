def extract_translated_sentences(json_response):
    translations = json_response["result"]["translations"]
    translated_sentences = [
        translation["beams"][0]["sentences"][0]["text"]
        for translation in translations
    ]
    return translated_sentences


def extract_split_sentences(json_response):
    return json_response["result"]["splitted_texts"][0]

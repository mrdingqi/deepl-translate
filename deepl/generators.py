from deepl.hacks import generate_timestamp
from deepl.settings import MAGIC_NUMBER, SUPPORTED_FORMALITY_TONES,HEADERS


def generate_splquitit_sentences_request_data(text):
    return {
        "jsonrpc": "2.0",
        "method": "LMT_split_text",
        "params": {
            "texts": [text],
            "commonJobParams": {
            "mode": "translate" 
            },
        },
            "lang": {
        "lang_user_selected": "auto",
        "preference": {
            "DE": 0.17468,
            "EN": 2.35799,
            "ES": 0.09085,
            "FR": 0.13127,
            "IT": 0.0254,
            "JA": 0.03672,
            "NL": 0.02493,
            "PL": 0.01293,
            "PT": 0.01336,
            "RU": 0.01489,
            "ZH": 0.37636,
            "BG": 0,
            "CS": 0,
            "DA": 0,
            "EL": 0,
            "ET": 0,
            "FI": 0,
            "HU": 0,
            "ID": 0,
            "LV": 0,
            "LT": 0,
            "RO": 0,
            "SK": 0,
            "SL": 0,
            "SV": 0,
            "TR": 0,
            "UK": 0,
            "KO": 0,
            "NB": 0
        },
        "default": "default"
    },

    }

#生成请求参数里的job参数
def generate_jobs(sentences, beams=1):
    jobs = []
    for idx, sentence in enumerate(sentences):
        job = {
            "kind": "default",
            "raw_en_sentence": sentence,
            "raw_en_context_before": sentences[:idx],
            "raw_en_context_after": [sentences[idx + 1]]
            if idx + 1 < len(sentences)
            else [],
            "preferred_num_beams": beams,
        }
        jobs.append(job)
    return jobs


def generate_common_job_params(formality_tone):
    if not formality_tone:
        return {}
    if formality_tone not in SUPPORTED_FORMALITY_TONES:
        raise ValueError(f"Formality tone '{formality_tone}' not supported.")
    return {"formality": formality_tone}


def generate_translation_request_data(
    source_language,
    target_language,
    sentences,
    identifier=MAGIC_NUMBER,
    alternatives=1,
    formality_tone=None,
):
    return {
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": generate_jobs(sentences, beams=alternatives),
            "lang": {
                "preference": {"weight": {}, "default": "default"},
                "source_lang_computed": source_language,
                "target_lang": target_language,
            },
            "priority": 1,
            "commonJobParams": generate_common_job_params(formality_tone),
            "timestamp": generate_timestamp(sentences),
        },
        "id": identifier,
    }
import time
from random import randrange

def genertate_body_basic(paragraphs,source_lang="EN",target_lang="ES"):
    return(
    {
    "jsonrpc":"2.0",
    "method":"LMT_handle_jobs",
    "params":{
        "jobs":generate_jobs(paragraphs, before_context=""),
        "lang":{
            "target_lang":target_lang,
            "preference":{
                "weight":{

                },
                "default":"default"
            },
            "source_lang_computed":source_lang
        },
        "priority":1,
        "commonJobParams":{
            "mode":"translate",
            "browserType":1,
            "formality":"formal"
        },
        "timestamp":int(time.time()*1000)
    },
    "id":randrange(10_000_000, 100_000_000)
})

#获得jobs的值
def generate_jobs(paragraphs, before_context=""):
    paragraph_qty=len(paragraphs)
    # print(f"一共有{paragraph_qty}段内容")
    jobs = []
    beams=1
    id=1
    for idx, paragraph in enumerate(paragraphs):
        if idx==0:
            # print(f"正在处理{idx+1}个元素,{paragraphs[idx]}")

            job = {
                "kind": "default",
                "sentences":[{"text":paragraph,"id":id,"prefix":""}],
                "raw_en_context_before": [],
                "raw_en_context_after": [paragraphs[idx + 1]],
                "preferred_num_beams": beams,
            }
            id+=1
        elif idx==paragraph_qty-1:
            # print(f"正在处理{idx+1}个元素,{paragraphs[idx]}")
            job = {
                "kind": "default",
                "sentences":[{"text":paragraph,"id":id,"prefix":""}],
                "raw_en_context_before": [paragraphs[idx - 1]],
                "raw_en_context_after": [],
                "preferred_num_beams": beams,
            }
            id+=1
        else:
            # print(f"正在处理{idx+1}个元素,{paragraphs[idx]}")
            job = {
                "kind": "default",
                "sentences":[{"text":paragraph,"id":id,"prefix":""}],
                "raw_en_context_before": [paragraphs[idx - 1]],
                "raw_en_context_after": [paragraphs[idx + 1]],
                "preferred_num_beams": beams,
            }
            id+=1
        jobs.append(job)
       
    return jobs
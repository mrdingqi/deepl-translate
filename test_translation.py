import requests,json

url = "https://api.deepl.com/jsonrpc?method=LMT_handle_jobs"
cookie='dapUid=ec35aa52-20a1-4e00-850e-46efbe3f62b0; LMTBID=v2|99c3158b-81a6-431a-962d-2485aa577f61|a8e62171d6bb4a8060b13eb8569e81b8; userCountry=US; privacySettings={\"v\":1,\"t\":1690416000,\"m\":\"LAX\",\"consent\":[\"NECESSARY\",\"PERFORMANCE\",\"COMFORT\",\"MARKETING\"]}; userRecommendations=RC-10.2; dapVn=2; __cf_bm=PKGqPG7rGsTv0bgTrTcDDPg359e901UBXs4btxppKVA-1691390406-0-Abt0lKxrdNdyi9uaGGZinfU2HDxJB73EcFVNR6e9Snttd7F9+8K8BrkVoFfqqX8o4DWl84iUCAn68KTdS960/qM=; dl_clearance=CTotvzGygtqrYT9K2SpyXp65OpHkvhasDwHqahMlwbuhSxlyIOjGFzOeRQ78RrK_fWLyDqTt0c1-ycmHQekvQenhJt2p0biV7vm56fhHj50; dl_session=bae9e47c-a29d-b011-c9f6-972f9cfea26a; dapGid=Y5NBbRPc2x_2-YIXnWrxfLeEh911Gj4kHQjk5ODnePh39vwsPS-N0N1QYVh5FwKEemplbQTdS9sH7GbR2ttdhqAoJW1BaE_85IckNEKr3IOBbh1ObikVqYcOL4sTC3vDgi8EHUo; releaseGroups=2274.DM-952.2.2_1808.DF-3339.2.2_2373.DM-1113.2.2_2346.DF-3049.2.2_2379.DM-997.1.1_2050.DM-455.1.3_2372.DM-1004.1.1_220.DF-1925.1.9_2347.DF-3557.2.2_1483.DM-821.2.2_2401.DWFA-602.2.1_2394.WDW-217.2.2_2383.DF-3505.1.1_2024.SEO-103.2.4_2278.DF-3430.1.4_866.DM-592.2.2_863.DM-601.2.2_1119.B2B-251.2.4_2365.WDW-179.2.2_2350.TACO-8.2.2_1577.DM-594.2.3_1585.DM-900.2.3_2371.DM-1018.1.1_976.DM-667.2.3_2395.WDW-151.2.1_2396.ACL-384.1.1_2022.DF-3340.2.2_2256.DF-3461.2.2_2370.DAL-568.2.1_2382.WDW-165.2.2_2068.DF-3045.2.3_978.AA-SUB1.1.2_1571.DM-791.2.4_1327.DWFA-391.2.2_2359.WDW-155.2.3_2055.DM-814.2.3_2374.DWFA-542.1.3_2369.DAL-371.2.1_1084.TG-1207.2.3_2357.TACO-19.1.2_2349.DWFA-553.2.2_1583.DM-807.2.5_2366.WDW-189.2.2_2356.B2B-515.2.2_2380.DWFA-494.2.1_1444.DWFA-362.2.2_2377.DUI-131.2.2_2345.DM-1001.2.2_1780.DM-872.2.2_975.DM-609.2.3_2378.DM-976.2.1_2400.WDW-238.2.2_1997.DM-941.2.3; dapSid={\"sid\":\"c8c8ce34-0c50-4822-811f-b8322e274682\",\"lastUpdate\":1691390498}'

headers = {
    "authority": "api.deepl.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "cookie": "cookie",
    "origin": "https://www.deepl.com",
    "pragma": "no-cache",
    "referer": "https://www.deepl.com/",
    "sec-ch-ua": "Not/A)Brand;v=99, Google Chrome;v=115, Chromium;v=115",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

headers["cookie"]=cookie

data = {
    "jsonrpc": "2.0",
    "method": "LMT_handle_jobs",
    "params": {
        "jobs": [
            {
                "kind": "default",
                "sentences": [
                    {
                        "text": "Chapter 1: Admission to Military School",
                        "id": 1,
                        "prefix": ""
                    }
                ],
                "raw_en_context_before": [],
                "raw_en_context_after": ["Rennes planet on the edge of the Cigar Galaxy."],
                "preferred_num_beams": 1
            },
            {
                "kind": "default",
                "sentences": [
                    {
                        "text": "Rennes planet on the edge of the Cigar Galaxy.",
                        "id": 2,
                        "prefix": ""
                    }
                ],
                "raw_en_context_before": ["Chapter 1: Admission to Military School"],
                "raw_en_context_after": ["This is a very barren and desolate planet, with a population of less than 100 million."],
                "preferred_num_beams": 1
            },
            # Add other sentences here...
        ],
        "lang": {
            "target_lang": "ES",
            "preference": {
                "weight": {},
                "default": "default"
            },
            "source_lang_computed": "EN"
        },
        "priority": 1,
        "commonJobParams": {
            "mode": "translate",
            "browserType": 1,
            "formality": "formal"
        },
        "timestamp": 1691390500596
    },
    "id": 48390008
}

print(type(headers))
print(type(data))

response = requests.post(url, headers=headers, json=data)
print(response.json())
# print(url)
# print(headers)
# print(type(headers))
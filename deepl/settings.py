API_URL = "https://api.deepl.com/jsonrpc?method=LMT_handle_jobs"


HEADERS={
    "authority": "api.deepl.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "cookie": "LMTBID=v2|c33ee2f1-893e-44eb-9a60-12663fe722e8|faf1bf359ec8cd8c4f10c423b241789c; userCountry=US; dapUid=dcc9e792-61ea-4643-a708-42603c45c9e4; privacySettings={\"v\":\"1\",\"t\":1691107200,\"m\":\"LAX\",\"consent\":[\"NECESSARY\",\"PERFORMANCE\",\"COMFORT\",\"MARKETING\"]}; cf_clearance=TZYg_SxFgfBTauA7wub8w2q.FrauHTrApS4qmTyDysY-1691161654-0-1-99bf7bf3.22f98b70.cebe2413-150.0.0; dl_session=52416092-ded4-789d-9579-917228517984; dapGid=9W3lT1-Ooi3W_thae9MlfrdZzdGyoQppxZPlX0Xvd0a3IBc_WYDtvaveJSbxU8xJCJJLRNt8z0eQ6raVJ9p4m5vhrB_hUcF8Dd5v4XS1_noS14YRLPM9joThiH2Y5VSISy2LKwI; userRecommendations=RC-10.1; releaseGroups=2024.SEO-103.1.4_2345.DM-1001.2.2_863.DM-601.2.2_2383.DF-3505.2.1_2395.WDW-151.2.1_2055.DM-814.2.3_2372.DM-1004.1.1_975.DM-609.2.3_1808.DF-3339.2.2_2382.WDW-165.2.2_2346.DF-3049.1.2_2350.TACO-8.2.2_2380.DWFA-494.2.1_2274.DM-952.2.2_2347.DF-3557.2.2_220.DF-1925.1.9_1585.DM-900.2.3_1780.DM-872.2.2_1583.DM-807.2.5_2401.DWFA-602.2.1_2374.DWFA-542.2.3_2369.DAL-371.1.1_2356.B2B-515.2.2_976.DM-667.2.3_2278.DF-3430.2.4_2394.WDW-217.2.2_2400.WDW-238.2.2_1327.DWFA-391.2.2_1997.DM-941.2.3_2349.DWFA-553.2.2_2373.DM-1113.1.2_866.DM-592.2.2_978.AA-SUB1.1.2_2378.DM-976.1.1_2365.WDW-179.2.2_2050.DM-455.1.3_1483.DM-821.2.2_1577.DM-594.2.3_2366.WDW-189.2.2_2068.DF-3045.2.3_1084.TG-1207.2.3_2357.TACO-19.2.2_2370.DAL-568.1.1_2371.DM-1018.2.1_2377.DUI-131.2.2_2379.DM-997.1.1_1444.DWFA-362.2.2_1571.DM-791.2.4_2359.WDW-155.2.3_2396.ACL-384.1.1_2022.DF-3340.2.2_1119.B2B-251.2.4_2256.DF-3461.2.2; dapVn=3; dapSid={\"sid\":\"c949dac9-07c3-41d8-b46f-b97ec9110008\",\"lastUpdate\":1691367829}",
    "origin": "https://www.deepl.com",
    "pragma": "no-cache",
    "referer": "https://www.deepl.com/",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


MAGIC_NUMBER = int("CAFEBABE", 16)

SUPPORTED_LANGUAGES = [
    {"code": "BG", "language": "Bulgarian"},
    {"code": "ZH", "language": "Chinese"},
    {"code": "CS", "language": "Czech"},
    {"code": "DA", "language": "Danish"},
    {"code": "NL", "language": "Dutch"},
    {"code": "EN", "language": "English"},
    {"code": "ET", "language": "Estonian"},
    {"code": "FI", "language": "Finnish"},
    {"code": "FR", "language": "French"},
    {"code": "DE", "language": "German"},
    {"code": "EL", "language": "Greek"},
    {"code": "HU", "language": "Hungarian"},
    {"code": "IT", "language": "Italian"},
    {"code": "JA", "language": "Japanese"},
    {"code": "LV", "language": "Latvian"},
    {"code": "LT", "language": "Lithuanian"},
    {"code": "PL", "language": "Polish"},
    {"code": "PT", "language": "Portuguese"},
    {"code": "RO", "language": "Romanian"},
    {"code": "RU", "language": "Russian"},
    {"code": "SK", "language": "Slovak"},
    {"code": "SL", "language": "Slovenian"},
    {"code": "ES", "language": "Spanish"},
    {"code": "SV", "language": "Swedish"},
]

SUPPORTED_FORMALITY_TONES = ["formal", "informal"]

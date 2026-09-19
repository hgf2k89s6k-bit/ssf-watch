import requests

HEADERS = {"User-Agent":"Mozilla/5.0"}

ITEMS = [
    # 상품1 (003만)
    ("PP1_0117","https://www.ssfshop.com/PLEATS-PLEASE-ISSEY-MIYAKE/GM0026090810117/good","003"),
    ("PP1_0118","https://www.ssfshop.com/PLEATS-PLEASE-ISSEY-MIYAKE/GM0026090810118/good","003"),

    # 상품2 (전 사이즈)
    ("PP2_0855","https://www.ssfshop.com/PLEATS-PLEASE-ISSEY-MIYAKE/GM0026072960855/good",None),
    ("PP2_0856","https://www.ssfshop.com/PLEATS-PLEASE-ISSEY-MIYAKE/GM0026072960856/good",None),
    ("PP2_0857","https://www.ssfshop.com/PLEATS-PLEASE-ISSEY-MIYAKE/GM0026072960857/good",None),

    # 상품3 (003만)
    ("PP3_8736","https://www.ssfshop.com/PLEATS-PLEASE-ISSEY-MIYAKE/GM0026090198736/good","003"),
]

for name, url, size in ITEMS:
    try:
        html = requests.get(url, headers=HEADERS, timeout=20).text
        if "품절" not in html and "SOLD OUT" not in html:
            print(f"RESTOCK: {name} size={size or 'ALL'}")
    except Exception as e:
        print(name, e)

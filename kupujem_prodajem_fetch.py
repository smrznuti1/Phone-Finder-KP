import re

import requests


def get_ads_for_phone(phone_name: str, price=300, additional_keywords: str = ""):
    cookies = {
        "machine_id": "e3037f5775ff98e496b62c55a4577dcb",
        "KUPUJEMPRODAJEM": "jf6t0rh68qu4519gtfag5r9bb7",
        "cookie_consent_v2": "1",
        "cookie[user_idSSL]": "4aabc4315b1f8a9baea3bc253ad28676",
        "KP-DEVICE-JWT": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMDQ0ODE1LCJhdXRob3JpemVkX3VzZXJzIjpbMTA0NDgxNV0sImV4cCI6MTc1MTcyNTE0OSwidmVyc2lvbiI6MSwibWFjaGluZV9pZCI6ImUzMDM3ZjU3NzVmZjk4ZTQ5NmI2MmM1NWE0NTc3ZGNiIiwiaXNzIjoiaHR0cHM6Ly93d3cua3VwdWplbXByb2RhamVtLmNvbS8iLCJpYXQiOjE3MjAxODkxNDksImp0aSI6IjZkZTJkN2FiZTY3ZDI5YTA1ODlkYjljNDk4NWZmNjJiIn0.HrlVqrc4dVOnaL0-NkZxisLFimz-Xg113Mfhm2cNrd0",
        "KP-TEMP-AUTH-JWT": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMDQ0ODE1LCJpc3MiOiJodHRwczovL3d3dy5rdXB1amVtcHJvZGFqZW0uY29tLyIsImlhdCI6MTcyMDE4OTE0OSwianRpIjoiNWIyMzZkMDAzMjI1NzYyMmIwNTFjY2I5YmNmYWMzODQifQ.1CFXKgZQ57WizNNczTIkpLbcb7j4Ut6Zoh5lruXjcYk",
        "recentSearchFilterIds": "[4030847969]",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }

    params = {
        "keywords": f"{phone_name} {additional_keywords}",
        "categoryId": "23",
        "priceTo": str(price),
        "currency": "eur",
        "order": "price desc",
        "page": "1",
        # 'keywordsScope': 'description',
        "hasPrice": "yes",
    }

    response = requests.get(
        "https://www.kupujemprodajem.com/kompjuteri-laptop-i-tablet/pretraga",
        params=params,
        headers=headers,
        # cookies=cookies,
    )

    text = response.text
    with open("test.txt", "w") as output:
        output.write(f"{text}\n")

    links = re.findall(
        r"(https://www.kupujemprodajem.com/mobilni-telefoni/.*/oglas/[^\"]+)", text
    )
    return links

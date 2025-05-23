# import re
from typing import Any, List

import regex
from requests import get


class PhoneBenchmarks:
    def __init__(self):
        pass

    @staticmethod
    def __find_phone_names_from_line(line):
        match = regex.match(r".*</span>(.*)<span.*", line)
        if match is None:
            return None
        return match.group(1)

    @staticmethod
    def get_phones() -> List[Any] | None:
        response = get("https://unite4buy.com/antutu/")
        if response.status_code != 200:
            return None

        response_text = response.text.replace("\n", " ")
        with open("output.txt", "w") as otp:
            print(response_text, file=otp)
        antutu_extracts = regex.findall(
            r'<div class="bn-numb">\s*<a href=\'([^\']+)\'>\s*(\d+)',
            response_text,
            concurrent=True,
        )

        extracts: List[Any] = []

        for antutu_extract in antutu_extracts:
            extracts.append(
                tuple(
                    [
                        antutu_extract[0]
                        .replace("-antutu", "")
                        .replace("/", "")
                        .replace("-", " "),
                        int(antutu_extract[1]),
                    ]
                )
            )

        extracts = sorted(extracts, key=lambda extract: -extract[1])
        # print(extracts)

        return list(map(lambda extract: extract[0], extracts))

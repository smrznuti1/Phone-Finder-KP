import re
from typing import Any, List

from requests import get


def __find_phone_names_from_line(line):
    match = re.match(r".*</span>(.*)<span.*", line)
    if match is None:
        return None
    return match.group(1)


def get_phones() -> List[str]:
    response = get("https://antutu.com/en/ranking/rank1.htm")
    if response.status_code != 200:
        return []

    ranking_lines = response.text.split("\n")

    ranking = map(lambda line: line.strip(), filter(lambda line: line.find("numrank numall link") != -1, ranking_lines))
    ranking = map(__find_phone_names_from_line, ranking)

    return list(ranking)

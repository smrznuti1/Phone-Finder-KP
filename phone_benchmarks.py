import re

from requests import get


def get_phones():
    ranking = get("https://antutu.com/en/ranking/rank1.htm")
    if ranking.status_code == 200:
        ranking = ranking.text.split("\n")

    ranking = map(lambda line: line.strip(), filter(lambda line: line.find("numrank numall link") != -1, ranking))
    ranking = map(lambda line: re.match(r".*</span>(.*)<span.*", line)[1], ranking)

    return list(ranking)

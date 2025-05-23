from multiprocessing.pool import ThreadPool

import click

from kupujem_prodajem_fetch import get_ads_for_phone

# from phone_benchmarks import get_phones
from phone_list import PhoneBenchmarks as pl


def print_phone_links(phone, price, keywords):
    ads = get_ads_for_phone(phone, price, additional_keywords=keywords)
    ads = list(map(lambda ad: f" - {ad}\n", ads))
    header = f"## {phone}"
    ads = "".join(ads)
    return f"{header}\n{ads}"


@click.command()
@click.option("--price", default="300", required=False)
@click.option("--keywords", default="", required=False)
def main(price, keywords):
    phone_list = pl.get_phones()
    # phone_list = get_phones()
    print("# List")
    pool = ThreadPool(32)
    for result in pool.map(
        lambda phone: print_phone_links(phone, price, keywords), phone_list
    ):
        print(result)


if __name__ == "__main__":
    main()

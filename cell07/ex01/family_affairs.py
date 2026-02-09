#!/usr/bin/env python3


def find_the_redheads(data: dict):
    return list(map(lambda item: item[0],filter(lambda item: item[1] == "red", data.items())))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red",
}
print(find_the_redheads(dupont_family))

# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
from collections import namedtuple
from bs4 import BeautifulSoup
import pprint

ctrl_tuple = namedtuple('CtrlTuple', field_names=('seq', 'decimal', 'hexadecimal', 'abbreviation', 'name'))


def parse_html(source=None):
    res = list()

    if source is None:
        source = os.path.join(os.path.dirname(__file__), 'resource/source_file.html')

    soup = BeautifulSoup(open(source).read(), "html.parser")
    for tr in soup.body.table.find_all('tr')[1:]:
        data = [td.text for td in tr.find_all('td')]
        data[1] = int(data[1])
        res.append(ctrl_tuple(*data))

    return res


if __name__ == '__main__':
    pprint.pprint(parse_html())

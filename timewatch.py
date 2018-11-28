# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

SITE_URL = "http://checkin.timewatch.co.il/punch/"
PUNCH_IN = r"כניסה"
PUNCH_OUT = r"יציאה"

HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    'Referer': "http://checkin.timewatch.co.il/punch/punch2.php"
}


def parse_html(html_doc):
    return BeautifulSoup(html_doc, 'html.parser')


def urljoin(*parts):
    parts = map(lambda x: x.strip('/'), parts)
    return '/'.join(parts)


class TimeWatchClient(object):
    def __init__(self, company, employee, password):
        self.ix_employee = ''
        self.company = company
        self.employee = employee
        self.password = password
        self.session = requests.Session()

    def login(self):
        data = {'comp': self.company, 'name': self.employee, 'pw': self.password}
        url = urljoin(SITE_URL, 'punch2.php')
        r = self.session.post(url, data=data, allow_redirects=False, headers=HEADERS)
        r.raise_for_status()

        response = parse_html(r.text)
        self.ix_employee = response.find('input', {'id': 'ixemplee'})['value']

    def punch(self, option, remark=''):
        data = {
            'comp': self.company,
            'name': self.employee,
            'remark': remark,
            'B1': option,
            'ix': self.ix_employee,
            'ts': '',
            'allowremarks': 1,
            'msgfound': 0,
            'thetask': 0,
            'teamleader': 0,
            'tflag': ''
        }
        url = urljoin(SITE_URL, 'punch3.php')
        r = self.session.post(url, data=data, headers=HEADERS)
        r.raise_for_status()

    def punch_in(self, remark=''):
        return self.punch(PUNCH_IN, remark)

    def punch_out(self, remark=''):
        return self.punch(PUNCH_OUT, remark)

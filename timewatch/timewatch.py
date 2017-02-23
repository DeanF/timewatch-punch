from http import HTTPStatus
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from .exceptions import TimeWatchLoginError, TimeWatchError

SITE_URL = 'http://checkin.timewatch.co.il/punch/'
PUNCH_IN = 'כניסה'
PUNCH_OUT = 'יציאה'


def parse_html(html_doc):
    return BeautifulSoup(html_doc, 'html.parser')


class TimeWatch(object):
    def __init__(self, company, employee, password):
        self.ix_employee = ''
        self.company = company
        self.employee = employee
        self.password = password
        self.session = requests.Session()

    def login(self):
        res = self.session.post(urljoin(SITE_URL, 'punch2.php'),
                                data={
                                    'comp': self.company,
                                    'name': self.employee,
                                    'pw': self.password
                                }, allow_redirects=False)

        if res.status_code != HTTPStatus.OK:
            raise TimeWatchLoginError(res.text)
        parsed = parse_html(res.text)
        self.ix_employee = \
            parsed.find('input', {'id': 'ixemplee'})['value']
        return True

    def punch(self, option, remark=''):
        res = self.session.post(urljoin(SITE_URL, 'punch3.php'),
                                data={
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
                                })
        if res.status_code != HTTPStatus.OK:
            raise TimeWatchError(res.text)
        return True

    def punch_in(self, remark=''):
        return self.punch(PUNCH_IN, remark)

    def punch_out(self, remark=''):
        return self.punch(PUNCH_OUT, remark)

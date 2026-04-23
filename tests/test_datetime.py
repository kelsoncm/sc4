"""
The MIT License (MIT)

Copyright (c) 2015 kelsoncm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from datetime import date, timedelta
from unittest import TestCase

from sc4py.datetime import daterange, now, now_str, others_months, this_month, this_year, today, today_str


class TestPythonBrfiedDatetime(TestCase):

    def test_this_year(self):
        self.assertEqual(now().year, this_year())

    def test_today_str(self):
        self.assertEqual(date.today().strftime("%d-%m-%Y"), today_str())

    def test_today(self):
        self.assertEqual(date.today(), today())

    def test_now_str(self):
        self.assertEqual(now().strftime("%d-%m-%Y %H:%M:%S"), now_str())

    def test_this_month(self):
        self.assertEqual(now().month, this_month())

    def test_others_months(self):
        t = this_month()
        self.assertEqual([m for m in range(1, 13) if m != t], others_months())

    def test_daterange_default_step(self):
        result = list(daterange(date(2026, 1, 1), date(2026, 1, 3)))
        self.assertEqual([date(2026, 1, 1), date(2026, 1, 2), date(2026, 1, 3)], result)

    def test_daterange_custom_step(self):
        result = list(daterange(date(2026, 1, 1), date(2026, 1, 5), step=timedelta(days=2)))
        self.assertEqual([date(2026, 1, 1), date(2026, 1, 3), date(2026, 1, 5)], result)

"""
Nose tests for acp_times.py

Tests based on examples given by https://rusa.org/pages/acp-brevet-control-times-calculator.
"""

import nose    # Testing framework
import logging
import arrow
from acp_times import open_time, close_time

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

start_time = arrow.get('2020-01-01 00:00:00', 'YYYY-MM-DD HH:mm:ss')
d1 = 60
d2 = 120
d3 = 175
d4 = 200

class TestOpenTimes:
    def test_openTime1(self):
        assert arrow.get(open_time(d1, 200, start_time)) == arrow.get('2020-01-01 01:46:00', 'YYYY-MM-DD HH:mm:ss')

    def test_openTime2(self):
        assert arrow.get(open_time(d2, 200, start_time) )== arrow.get('2020-01-01 03:32:00', 'YYYY-MM-DD HH:mm:ss')

    def test_openTime3(self):
        assert arrow.get(open_time(d3, 200, start_time) )== arrow.get('2020-01-01 05:09:00', 'YYYY-MM-DD HH:mm:ss')
        
    def test_openTime4(self):
        assert arrow.get(open_time(d4, 200, start_time) )== arrow.get('2020-01-01 05:53:00', 'YYYY-MM-DD HH:mm:ss')

class TestCloseTimes:
    def test_closeTime1(self):
        assert arrow.get(close_time(d1, 200, start_time) )== arrow.get('2020-01-01 04:00:00', 'YYYY-MM-DD HH:mm:ss')

    def test_closeTime2(self):
        assert arrow.get(close_time(d2, 200, start_time)) == arrow.get('2020-01-01 08:00:00', 'YYYY-MM-DD HH:mm:ss')

    def test_closeTime3(self):
        assert arrow.get(close_time(d3, 200, start_time)) == arrow.get('2020-01-01 11:40:00', 'YYYY-MM-DD HH:mm:ss')
from unittest import TestCase
from jd import jd, cd, cd_diff, cd_by_num, cd_inc, dow, doy


class TestJd(TestCase):

    def test_jd_before(self):
        self.assertEqual(jd(333, 1, 27.5), 1842713.0, "Incorrect Julian Date before the reform")

    def test_jd_after(self):
        self.assertEqual(jd(1957, 10, 4.81), 2436116.31, "Incorrect Julian Date after the reform")

    def test_jd_bc(self):
        self.assertEqual(jd(-584, 5, 28.63), 1507900.13, "Incorrect Julian Date BC")


class TestCd(TestCase):
    def test_cd_before(self):
        self.assertEqual(cd(1842713.0), (333, 1, 27.5), "Incorrect Calendar Date before the reform")

    def test_cd_after(self):
        self.assertEqual(cd(2436116.31), (1957, 10, 4.81), "Incorrect Calendar Date after the reform")

    def test_cd_bc(self):
        self.assertEqual(cd(1507900.13), (-584, 5, 28.63), "Incorrect Calendar Date BC")

    def test_cd_diff_1(self):
        self.assertEqual(cd_diff((1835, 11, 16), (1910, 4, 20)), 27183, "Incorrect difference between two dates")

    def test_cd_diff_2(self):
        self.assertEqual(cd_diff((2016, 1, 1), (2017, 1, 1)), 366, "Incorrect difference between two dates")

    def test_cd_by_num_1(self):
        self.assertEqual(cd_by_num(1900, 1), (1900, 1, 1), "Incorrect date by day number")

    def test_cd_by_num_2(self):
        self.assertEqual(cd_by_num(2017, 365), (2017, 12, 31), "Incorrect date by day number")

    def test_cd_inc_1(self):
        self.assertEqual(cd_inc(1954, 6, 30, 10000), (1981, 11, 15), "Incorrect date increment")

    def test_cd_inc_2(self):
        self.assertEqual(cd_inc(2017, 10, 30, -1), (2017, 10, 29), "Incorrect date increment")


class TestDay(TestCase):

    def test_dow_1(self):
        self.assertEqual(dow(1954, 6, 30), 3, "Incorrect day of week")

    def test_dow_2(self):
        self.assertEqual(dow(2017, 10, 29), 0, "Incorrect day of week")

    def test_doy_1(self):
        self.assertEqual(doy(1978, 11, 14), 318, "Incorrect day of year")

    def test_doy_2(self):
        self.assertEqual(doy(1980, 4, 22), 113, "Incorrect day of year")

    def test_doy_3(self):
        self.assertEqual(doy(1600, 12, 31), 366, "Incorrect day of year")

'''

'''
import unittest
import engarde.util.strutil as strutil

names = ( ' Nakagawa, Sean : ', ' Qiu, Nathan : ' )
vnames= ( 'Nakagawa, Sean', 'Qiu, Nathan' )


dates0 = [
 'Apr 27 - Apr 29, 2018',
 'Apr 27 - Apr 30, 2018',
 'May 2, 2018',
 'May 3, 2018',
 'May 4 - May 6, 2018',
 'May 6, 2018']

dates1 = [
 'Apr 29, 2018',
 'Apr 30, 2018',
 'May 2, 2018',
 'May 3, 2018',
 'May 6, 2018',
 'May 6, 2018']

dates2 = [
 'Apr 30, 2018',
 'May 18, 2018',
 'May 6, 2018',
]

dates3 = [
 20180430,
 20180518,
 20180506,
]

class Test( unittest.TestCase ):
    def test_norm1(self):
        for n, v in zip(names, vnames):
            n_ = strutil.normName(n)
            self.assertEqual( n_, v )

    def test_dates(self):
        for d, e1 in zip( dates0, dates1 ):
            e0 = strutil.normDate2(d)
            self.assertEqual(e0, e1)

    def test_dates2(self):
        for d, e1 in zip( dates2, dates3 ):
            e0 = strutil.normDate3(d)
            self.assertEqual(e0, e1)

if __name__ == '__main__':
    unittest.main()

'''
python engarde/test/unittest/util/test_strutil.py
'''

'''

'''
import unittest
import engarde.util.tmt_core as tmt_core

class Test( unittest.TestCase ):
    def test_norm1(self):
        data = [
            ('\nApr 29, 2018\n', 'Apr 29, 2018'),
        ]
        for d, e in data:
            r = tmt_core.normDate(d)
            self.assertEqual( e, r)


    def test_norm2(self):
        data = ['\n',
                'Y10 Mixed Saber:\n16 Competitors, a NR Event\n\n',
                '\n']
        r = tmt_core.normName(data)

        c = 'Y10 Mixed Saber:16 Competitors, a NR Event'
        self.assertEqual(r, r)

if __name__ == '__main__':
    unittest.main()

'''
python engarde/test/unittest/util/test_pool.py
'''
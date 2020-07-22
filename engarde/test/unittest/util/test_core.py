'''

'''
import engarde.util.core as core
import unittest

class Test( unittest.TestCase ):
    def test_norm1(self):
        s  = ['(1)Patil, Aaryan : ', '(16)Brubaker, Bronson : ']
        ee = ( ('Patil', 'Aaryan' ), ('Brubaker','Bronson'))
        for i,e in enumerate(s):
            f,l = core.normName2(e)
            print (ee[i])
            print (f,l)
            self.assertTrue( ee[i] == (f,l))
            
if __name__ == '__main__':
    unittest.main()

'''
python engarde/test/unittest/util/test_core.py
'''
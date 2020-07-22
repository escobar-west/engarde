'''

'''
import os
import shutil
import unittest
import engarde.util.data_index as dix

class Test( unittest.TestCase ):
    def test_ix1(self):
        root = '/tmp/dix/r1'
        if os.path.exists(root):
            shutil.rmtree(root)

        # import pdb; pdb.set_trace()
        ix = dix.IndexId( root, 'name0' )
        ix.add('one')
        ix.add('one')
        ix.add('two')
        id0 = ix.add('two')
        ix.flush()

        ix2 = dix.IndexId( root, 'name0' )
        id1 = ix2.add('two')
        print (id0, id1)
        ix2.flush()

        self.assertEqual( id0, id1 )

        ix = dix.IndexMap( root, 'map0' )
        ix.add('one', 'two')
        ix.add('one', 'two')
        ix.add('two', 'three')
        id0 = ix.get('two')
        ix.flush()

        ix2 = dix.IndexMap( root, 'map0' )
        id1 = ix2.get('two')
        print (id0, id1)
        ix2.flush()

        self.assertEqual( id0, id1 )

        ix = dix.IndexList( root, 'list0' )
        ix.add('one', 'two')
        ix.add('one', 'two1')
        ix.add('two', 'three')
        id0 = ix.get('two')
        ix.flush()

        ix2 = dix.IndexList( root, 'list0' )
        id1 = ix2.get('two')
        print (id0, id1)
        ix2.flush()

        self.assertEqual( id0, id1 )

        id0 = ix.get('one')
        id1 = ix2.get('one')
        print (id0, id1)
        self.assertEqual( id0, id1 )

        with self.assertRaises(ValueError):
            ix0 = dix.IndexList( root, 'list1', sorted=False, unique=True)
            ix0.add('one', 'two')
            ix0.add('one', 'two')

if __name__ == '__main__':
    unittest.main()

'''
python engarde/test/unittest/util/test_data_index.py
'''
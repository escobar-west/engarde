'''
'''


class BadData(Exception):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def _repr(self):
        return 'BadData %s ' % str( self._data)

    __repr__ = _repr
    __str__  = _repr


'''
python C:\\Users\\ilya\\GenericDocs\\dev\\engarde\\src\\util\\fileutil.py
'''

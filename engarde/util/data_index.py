'''

'''

import os
import pickle

class IndexBase( object ):
    def __init__(self, root, name, readOnly=False, keyType=None):
        self._root      = root
        self._name      = name
        self._modified  = False
        self._readOnly  = readOnly
        self._keyType   = keyType

    def _init(self):
        self._ix['keyType'] = self._keyType

        root = self._root
        if not os.path.exists( root):
            print ('init: making', root)
            os.makedirs( root )
        else:
            print ('init: alreday exists', root)
        self._dump(override=False)
        self._load()

    def checkType(self, name, val=None):
        if self._keyType is None:
            return

        if self._keyType:
            if not isinstance(self._keyType, (list, tuple)):
                self._keyType = (self._keyType, )

            if val:
                if len(self._keyType) > 1:
                    if not isinstance(val, self._keyType[1]):
                        raise ValueError('Bad value=%s type=%s' % (str(val), str(type(val))))
                if not isinstance(name, self._keyType[0]):
                    raise ValueError('Bad name=%s type=%s' % (str(name), str(type(name))))
            else:
                if not isinstance(name, self._keyType):
                    raise ValueError('Bad name=%s type=%s expected=%s' % (str(name), str(type(name)), self._keyType))

    def _fileName(self, root, name):
        return os.path.join(root, '%s_ix.pkl' % name)

    def _dump(self, override=True):
        fn = self._fn
        if not override:
            if not os.path.exists(fn):
                print ('IndexBase: dump: dumping', fn)
                with open(fn, 'wb') as fd:
                    pickle.dump(self._ix, fd)
            else:
                print ('IndexBase: dump: exists', fn)
        else:
            print ('IndexBase: dump: dumping', fn)
            with open(fn, 'wb') as fd:
                pickle.dump(self._ix, fd)

    def _load(self):
        fn = self._fn
        print ('IndexBase: load: loading', fn)
        with open(fn, 'rb') as fd:
            _ix = pickle.load(fd)
            if _ix['indexType'] != self._indexType:
                raise ValueError('IndexBase: loading wrong index %s %s %s' % (fn, self._indexType, _ix['indexType']))
            self._ix = _ix
            self._keyType = _ix['keyType']
        print ('_load: keyType: ', self._keyType)
    def __del__(self):
        print ('IndexBase: finishing')
        if not self._modified:
            print ('IndexBase: dump: nothing was mofified', self._fn)
            return
        self._dump(override=True)

    def flush(self):
        self._dump(override=True)


    def _repr(self):
        c = self._api
        s = c[0] + '\n\t' + '\n\t'.join( c[1:])
        return s

    __repr__ = _repr
    __str__  = _repr

class IndexId( IndexBase ):
    _indexType = 'IndexId'
    _api = ['IndexId', 'add(self, name)', 'get(self, name)', 'exists(self, name)']

    def __init__(self, root, name, readOnly=False, keyType=None):
        self._ix   = {'name2ix':{}, 'max':0, 'indexType': 'IndexId'}
        super().__init__(root=root, name=name, readOnly=readOnly, keyType=keyType)
        self._fn   = self._fileName(self._root, self._name)
        self._init()

    def add(self, name, dump=False):
        self._modified = True

        name2ix = self._ix['name2ix']
        if name not in name2ix:
            maxNum = self._ix['max']
            maxNum += 1
            name2ix[name] = maxNum
            self._ix['max'] = maxNum
            if dump:
                self._dump(override=True)
        return name2ix[name]

    def get(self, name):
        ix = self._ix['name2ix']
        return ix[name]

    def exists(self, name):
        self.checkType(name=name)
        ix = self._ix['name2ix']
        return name in ix


class IndexMap( IndexBase ):
    _indexType = 'IndexMap'
    _api = ['IndexBase', 'add(self, name, target)', 'get(self, name=None, inverted=False)', 'exists(self, name)', 'reset(self, name, target)']

    def __init__(self, root, name, unique=True, hasinvet=True, readOnly=False, keyType=None):
        self._ix     = { 'name2target':{}, 'target2name': {}, 'indexType': 'IndexMap' }
        self._unique = unique
        self._hasinvet = hasinvet
        super().__init__(root=root, name=name, readOnly=readOnly, keyType=keyType)
        self._fn     = self._fileName(self._root, self._name)
        self._init()

    def add(self, name, target, dump=False):
        self._modified = True

        name2target = self._ix['name2target']
        target2name = self._ix['target2name']
        if name not in name2target:
            name2target[name  ] = target
            if self._hasinvet:
                target2name[target] = name
            if dump:
                self._dump(override=True)
        else:
            if self._unique:
                target_ = name2target[name]
                if target != target_:
                    raise ValueError('Reuse of the name=%s new="%s", old="%s"' % ( name, target, target_))
        return name2target[name]

    def reset(self, name, target, dump=False):
        name2target = self._ix['name2target']
        target2name = self._ix['target2name']

        name2target[name  ] = target
        if self._hasinvet:
            target2name[target] = name
        if dump:
            self._dump(override=True)

        return name2target[name]

    def exists(self, name, typeCheck=True):
        if typeCheck:
            self.checkType(name=name)

        ix = self._ix['name2target']
        return name in ix

    def get(self, name=None, inverted=False):
        if inverted:
            ix = self._ix['target2name']
        else:
            ix = self._ix['name2target']

        if name:
            return ix[name]
        else:
            return ix


class IndexList( IndexBase ):
    _indexType = 'IndexList'
    _api = ['IndexList', 'add(self, name, val)', 'get(self, name=None)', 'exists(self, name, val)' ]

    def __init__(self, root, name, sorted=False, unique=False, readOnly=False, keyType=None):
        self._unique = unique
        self._sorted = sorted

        self._ix   = { 'name2list':{}, 'name2set': {}, 'indexType': 'IndexList' }
        super().__init__(root=root, name=name, readOnly=readOnly, keyType=keyType)
        self._fn   = self._fileName(self._root, self._name)
        self._init()

    def add(self, name, val, dump=False):
        self._modified = True

        name2list = self._ix['name2list']
        name2set  = self._ix['name2set']

        if name not in name2list:
            name2list[name] = []
            name2set[name]  = set()

        if self._unique:
            if val in name2set[name]:
                raise ValueError('Not unique! name=%s val=%s ix=%s' %(name, val, self._name))

        name2set[name].add(val)
        name2list[name].append(val)

        if dump:
            self._dump(override=True)
        return name2list[name]

    def get(self, name=None):
        ix = self._ix['name2list']
        if name is None:
            return ix

        if self._sorted:
            return sorted(ix[name])
        else:
            return ix[name]

    def exists(self, name, val):
        self.checkType(name=name,val=val)
        ix = self._ix['name2set']
        if not name in ix:
            return False
        return val in ix[name]

class IndexSet( IndexBase ):
    _indexType = 'IndexSet'
    _api = ['IndexSet', 'add(self, name, val)', 'get(self, name=None)', 'exists(self, name, val)' ]

    def __init__(self, root, name, sorted=False, unique=False, readOnly=False, keyType=None):
        self._unique = unique
        self._sorted = sorted

        self._ix   = { 'name2set': {}, 'indexType': 'IndexSet' }
        super().__init__(root=root, name=name, readOnly=readOnly, keyType=keyType)
        self._fn   = self._fileName(self._root, self._name)
        self._init()

    def add(self, name, val, dump=False):
        self._modified = True

        name2set  = self._ix['name2set']
        if name not in name2set:
            name2set[name]  = set()

        if self._unique:
            if val in name2set[name]:
                raise ValueError('Not unique! name=%s val=%s ix=%s' %(name, val, self._name))

        name2set[name].add(val)

        if dump:
            self._dump(override=True)
        return name2set[name]

    def get(self, name=None):
        ix = self._ix['name2set']
        if name is None:
            return ix

        if self._sorted:
            return sorted(ix[name])
        else:
            return ix[name]

    def exists(self, name, val):
        self.checkType(name=name,val=val)
        ix = self._ix['name2set']
        if not name in ix:
            return False
        return val in ix[name]

'''
'''

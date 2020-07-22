'''
'''
import datetime

def normName(name):
    '''
    ' Nakagawa, Sean : ', ' Qiu, Nathan : '
    '''
    n = name.lstrip(': ').rstrip(' :')
    return n

def normDate(date):
    return date.rstrip().lstrip()

def normDate2(date):
    date  = date.rstrip().lstrip()
    parts = date.split('-')
    if len(parts) == 1:
        return date
    date = parts[1].rstrip().lstrip()
    return date

def normDate3(date):
    date = normDate2(date)
    dd   = datetime.datetime.strptime(date, '%b %d, %Y')
    return dd.year * 10000 + dd.month * 100 + dd.day

def normEventName(event_name):
    data = [e for e in event_name if len(e)>1]
    assert len(data) == 1
    return data[0].replace('\n','')

'''
python C:\\Users\\ilya\\GenericDocs\\dev\\engarde\\src\\util\\fileutil.py
'''

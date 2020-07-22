'''

'''
import unittest
import engarde.util.pool_core as core

data = {
    "pool_url": "https://askfred.net/Results/roundResults.php?seq=1&event_id=146787",
    "tmt_id": "37163", "event_id": "146787",
    "pools": [
        {"pool_no": "Pool #1", "fencers": [
                {"name": " Trayanov, David : ",     "pool_pos": "1","results": ["D0", "D0", "D0", "D1", "D0"]},
                {"name": " Thomas, Devin : ",       "pool_pos": "2","results": ["V5", "D0", "D2", "D1", "V5"]},
                {"name": " Tann, Justin : ",        "pool_pos": "3","results": ["V5", "V5", "V5", "V5", "V5"]},
                {"name": " Swords, Evan : ",        "pool_pos": "4","results": ["V5", "V5", "D3", "D3", "V5"]},
                {"name": " Qiu, Nathan : ",         "pool_pos": "5","results": ["V5", "V5", "D2", "V5", "V5"]},
                {"name": " Nakagawa, Sean : ",      "pool_pos": "6","results": ["V5", "D2", "D1", "D0", "D3"]}]
         }, {
            "pool_no": "Pool #2", "fencers": [
                {"name": " Popovich, Elizabeth : ", "pool_pos": "1", "results": ["D1", "D3", "D1", "D4"]},
                {"name": " Nieto, Titus : ",        "pool_pos": "2", "results": ["V5", "V5", "D3", "D3"]},
                {"name": " Sheres, Asher : ",       "pool_pos": "3", "results": ["V5", "D1", "V5", "D2"]},
                {"name": " Lira, Daine : ",         "pool_pos": "4", "results": ["V5", "V5", "D4", "D3"]},
                {"name": " Patil, Aaryan : ",       "pool_pos": "5", "results": ["V5", "V5", "V5", "V5"]}
            ]
        },
    ]
}

res = [{('Nakagawa, Sean', 'Qiu, Nathan'): [3, 5],
  ('Nakagawa, Sean', 'Swords, Evan'): [0, 5],
  ('Nakagawa, Sean', 'Tann, Justin'): [1, 5],
  ('Nakagawa, Sean', 'Thomas, Devin'): [2, 5],
  ('Nakagawa, Sean', 'Trayanov, David'): [5, 0],
  ('Qiu, Nathan', 'Swords, Evan'): [5, 3],
  ('Qiu, Nathan', 'Tann, Justin'): [2, 5],
  ('Qiu, Nathan', 'Thomas, Devin'): [5, 1],
  ('Qiu, Nathan', 'Trayanov, David'): [5, 1],
  ('Swords, Evan', 'Tann, Justin'): [3, 5],
  ('Swords, Evan', 'Thomas, Devin'): [5, 2],
  ('Swords, Evan', 'Trayanov, David'): [5, 0],
  ('Tann, Justin', 'Thomas, Devin'): [5, 0],
  ('Tann, Justin', 'Trayanov, David'): [5, 0],
  ('Thomas, Devin', 'Trayanov, David'): [5, 0]},
 {('Lira, Daine', 'Nieto, Titus'): [5, 3],
  ('Lira, Daine', 'Patil, Aaryan'): [3, 5],
  ('Lira, Daine', 'Popovich, Elizabeth'): [5, 1],
  ('Lira, Daine', 'Sheres, Asher'): [4, 5],
  ('Nieto, Titus', 'Patil, Aaryan'): [3, 5],
  ('Nieto, Titus', 'Popovich, Elizabeth'): [5, 1],
  ('Nieto, Titus', 'Sheres, Asher'): [5, 1],
  ('Patil, Aaryan', 'Popovich, Elizabeth'): [5, 4],
  ('Patil, Aaryan', 'Sheres, Asher'): [5, 2],
  ('Popovich, Elizabeth', 'Sheres, Asher'): [3, 5]}]

from pprint import pprint as pp
class Test( unittest.TestCase ):
    def test_norm1(self):
        r = core.pool2ser(data['pools'])
        for i,e in enumerate(r):
            self.assertEqual( e, res[i])

if __name__ == '__main__':
    unittest.main()

'''
python engarde/test/unittest/util/test_pool.py
'''
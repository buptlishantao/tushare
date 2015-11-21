import sys
sys.path.append("..")

import tushare as ts
import util
import pandas

class DownloadData(object):
    """docstring for DownloadData"""
    def __init__(self):
        self.today = util.get_today_str()
        self.begin_day = util.get_begin_day_str()

    def get_stocks_id(self):
        pass


    def _get_stock_info(self):
        pass


    def _get_history_data(self):
        pass

    def _merge_to_history(self, sid):
        pass


    def download(self):
        stocks_id = self.get_stocks_id()
        for sid in stocks_id:
            self._merge_to_history(sid)




if __name__ == '__main__':
    DL = DownloadData()
    DL.download()
        


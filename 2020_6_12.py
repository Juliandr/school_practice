import time
import datetime
 
 
def get_diff_days_2_now(date_str):
    now_time = time.localtime(time.time())
    compare_time = time.strptime(date_str, "%Y-%m-%d")
    date1 = datetime.datetime(compare_time[0], compare_time[1], compare_time[2])
    date2 = datetime.datetime(now_time[0], now_time[1], now_time[2])
    diff_days = (date1 - date2).days
    return diff_days
 
 
print(get_diff_days_2_now("2020-07-7"))
 
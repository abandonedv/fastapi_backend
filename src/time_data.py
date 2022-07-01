month_d = {"Jan": "01",
           "Feb": "02",
           "Mar": "03",
           "Apr": "04",
           "May": "05",
           "Jun": "06",
           "Jul": "07",
           "Aug": "08",
           "Sep": "09",
           "Oct": "10",
           "Nov": "11",
           "Dec": "12"}


def time_data(tm, time_need=False):
    year = tm[-4:]
    month = tm[4:7]
    month = month_d[month]
    date = tm[8:10].split(" ")[-1]
    if len(date) == 1:
        date = "0" + date

    if time_need:
        time_list = tm[11:19].split(":")
        my_time = time_list[0] + "-" + time_list[1] + "-" + time_list[2]
        dt = year + "-" + month + "-" + date + "-" + my_time
    else:
        dt = year + "-" + month + "-" + date
    return dt

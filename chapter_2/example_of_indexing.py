# _*_ coding:utf-8 _*_
# 根据给定的年月日以数字形式打印出日期
months = ['january',
          'februray',
          'march',
          'april',
          'may',
          'june',
          'july',
          'august',
          'september',
          'october',
          'november',
          'december']
# 以1~31的数字作为结尾的列表
ending = ['st', 'nd', 'rd'] + 17 * ['th'] \
    + ['st', 'nd', 'rd'] + 7 * ['th'] \
    + ['st']
year = raw_input('Year: ')
month = raw_input('Month(1-12):')
day = raw_input('Day(1-31):')

month_number = int(month)
day_number = int(day)

month_number = int(month)
day_number = int(day)

# 记得要将年月份和天数减1，以获得正确的索引
month_name = months[month_number-1]
ordinal = day + ending[day_number-1]
print month_name + ' ' +ordinal + ',' + year
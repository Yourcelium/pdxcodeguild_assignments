import datetime

import operator

import matplotlib.pyplot as plt


def get_list_data(file):
    with open(file, 'r') as f:
        fread = f.read()  # readlines() here?
        spltfile = fread.splitlines()
        enumeratedfile = enumerate(spltfile)
        string_data = []
        for line in enumeratedfile:
            if '-------' in line[1]:
                string_data = spltfile[line[0] + 1:]
        data = []
        for i in string_data:
            data_row = i.split()
            date = datetime.datetime.strptime(data_row[0], '%d-%b-%Y')
            data_row = [x.replace('-', '0') for x in data_row]
            daily_total = int(data_row[1])
            hourly_data = data_row[2:]
            clean_hourly_data = []
            for x in hourly_data:
                clean_hourly_data.append(x.replace('-', '0'))
            clean_hourly_data = [int(hd) for hd in clean_hourly_data]
            data.append((date, daily_total, clean_hourly_data))
    return data


def total_average_daily_rainfall(data):
    averages = []
    for i in data:
        averages.append(i[1])
    total_average = sum(averages) / len(averages)
    return total_average


def most_rain_day(data):
    most_rain = data[0]
    for i in data:
        if i[1] > most_rain[1]:
            most_rain = i
    print(f'Date: {most_rain[0]}:\nRainfall: {most_rain[1]}')


def get_biggest_year(data):
    totals = {}
    for i in data:
        if i[0].year in totals:
            totals[i[0].year] = totals[i[0].year] + i[1]
        else:
            totals[i[0].year] = i[1]
    return max(totals.items(), key=operator.itemgetter(1))[0]


def get_years(data):
    years = {datarow[0].year for datarow in data}
    years = list(years)
    years.sort()
    return years


def rainfall_by_month_across_years(data, month):
    years = get_years(data)
    year_total = {}
    for year in years:
        year_total[year] = 0
    for datarow in data:
        if datarow[0].month == month:
            year_total[datarow[0].year] += datarow[1]
    totals = []
    for year in years:
        totals.append(year_total[year])
    return (years, totals)


def rainfall_whole(data):
    days = []
    rainfall = []
    for datarow in data:
        days.append(datarow[0])
        rainfall.append(datarow[1])
    return (days, rainfall)


def get_historical_averages_day(data):
    days = list(range(366))
    totals = [0]*366
    counts = [0]*366
    print(min([datarow[0].timetuple().tm_yday for datarow in data]))
    for datarow in data:
        #print(datarow[0].timetuple().tm_yday)
        doy = datarow[0].timetuple().tm_yday-1
        totals[doy] += datarow[1]
        counts[doy] += 1
    #for i in range(366):
    #    totals[i] /= counts[i]
    return(days,totals)


if __name__ == '__main__':
    mt_tabor = get_list_data('mt_tabor.rain.txt')
    print(get_biggest_year(mt_tabor))
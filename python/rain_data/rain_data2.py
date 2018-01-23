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
            data.append(i.split())
            data_row = i.split()
            data = datetime.datetime.strptime(data_row[0], '%d-%b-%Y')

    return data


def get_date(day):
    date = datetime.datetime.strptime(day[0], '%d-%b-%Y')
    print(f'Year: {date.year}')
    print(f'Month: {date.month}')
    print(f'Day: {date.day}')


def get_year(day):
    date = datetime.datetime.strptime(day[0], '%d-%b-%Y')
    return date.year


def get_month(day):
    date = datetime.datetime.strptime(day[0], '%d-%b-%Y')
    return date.month


def get_day(day):
    date = datetime.datetime.strptime(day[0], '%d-%b-%Y')
    return date.day


def average_daily_rainfall(file):
    averages = []
    for i in file:
        daily_average = int(i[1])
        averages.append(daily_average)
    total_average = sum(averages) / len(averages)
    return total_average


def clean_data(file):
    clean = []
    for i in file:
        cleani = [i[0]]
        for a in i[1:]:
            w = a.replace('-', '0')
            cleani.append(w)
        clean.append(cleani)
    return clean


def most_rain_day(file):
    most_rain = file[0]
    for i in file:
        if int(i[1]) > int(most_rain[1]):
            most_rain = i
    print(f'Rainfall: {most_rain[1]}')
    get_date(most_rain)


def get_biggest_year(file):
    totals = {}
    for i in file:
        year = get_year(i)
        if year in totals:
            totals[year] = totals[year] + int(i[1])
        else:
            totals[year] = int(i[1])
    return max(totals.items(), key=operator.itemgetter(1))[0]


#
# def get_average_rainfall_of_month(file, month, year):
#     total = []
#     for i in file:
#         if get_year(i) == int(year) and get_month(i) == int(month):
#             total.append(int(i[1]))
#     return sum(total)


def plot_rainfall_month(file, month):
    years = {}
    for i in file:
        if get_month(i) == month:
            if int(get_year(i)) in years:
                years[int(get_year(i))] = years[int(get_year(i))] + i[1]
            else:
                years[int(get_year(i))] = i[i]
    for i in
        plt.plot()


if __name__ == '__main__':
    mt_tabor = get_list_data('mt_tabor.rain.txt')
    cleantabor = clean_data(mt_tabor)
    print(get_average_rainfall_of_month(cleantabor, 1, 2016))
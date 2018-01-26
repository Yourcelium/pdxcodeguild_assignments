import datetime as dt

import operator

import csv

import matplotlib.pyplot as plt
'''
Print out a summary of the data:

* The specific most common crime type.
* The rarest crimes.
* The year with the most crime.

'''


def get_data_list(datafile):
    with open(datafile, 'r') as f:
        readdata = csv.reader(f)
        list_data = list(readdata)
        list_data = list_data[1:]
        data = []
        for datarow in list_data:
            strdatetime = datarow[1] + ' ' + datarow[2]
            datetime = dt.datetime.strptime(strdatetime.replace('/','-'), '%m-%d-%Y %X')
            # address = str
            dataline= []
            dataline.append(datarow[0])     #Record ID
            dataline.append(datetime)       #Date/Time of incident
            dataline.append(datarow[3])     #Type of Offence
            dataline.append(datarow[4])     #Address
            dataline.append(datarow[5])     #Neighborhood
            dataline.append(datarow[6])     #Police Precint
            dataline.append(datarow[7])     #Police District
            dataline.append(datarow[8] + ", " + datarow[9])  #x,y coordinates
            data.append(dataline)

    return data


def most_common_crime(data):
    crimes = {}
    for datarow in data:
        if datarow[2] in crimes:
            crimes[datarow[2]] += 1
        else:
            crimes[datarow[2]] = 1
    most_common = max(crimes.items(), key=operator.itemgetter(1))
    print(f'The most common crime for this period was {most_common[0]} which occured {most_common[1]} times')
    return most_common[0]


def least_common_crime(data):
    crimes = {}
    for datarow in data:
        if datarow[2] in crimes:
            crimes[datarow[2]] += 1
        else:
            crimes[datarow[2]] = 1
    least_common = min(crimes.items(), key=operator.itemgetter(1))
    crime_tuple = crimes.items()
    sorted_crimes = sorted(crime_tuple, key= lambda x: x[1])
    print(f'The least common crime for this period was {least_common[0]} which occured {least_common[1]} times')
    return least_common[0]


def most_crime_year(data):
    years = {}
    for datarow in data:
        if datarow[1].year in years:
            years[datarow[1].year] += 1
        else:
            years[datarow[1].year] = 1
    most_common = max(years.items(), key=operator.itemgetter(0))
    print(f'The year with the most crime was {most_common}')
    return most_common

if __name__ == '__main__':
    data = get_data_list('crime_incident_data_recent.txt')
    most_common_crime(data)
    least_common_crime(data)
    most_crime_year(data)

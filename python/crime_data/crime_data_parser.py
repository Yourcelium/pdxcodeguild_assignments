import datetime as dt

import operator

import matplotlib.pyplot as plt
'''
Print out a summary of the data:

* The specific most common crime type.
* The rarest crimes.
* The year with the most crime.

'''


def get_data_list(datafile):
    with open(datafile, 'r') as f:
        readdata = f.read()
        string_data = readdata.splitlines()
        string_data = string_data[1:]
        data = []
        for i in string_data:
            cleanstring = i.replace("\"", "")
            datarow = cleanstring.split(',')
            strdatetime = datarow[1] + ' ' + datarow[2]
            datetime = dt.datetime.strptime(strdatetime.replace('/','-'), '%m-%d-%Y %X')
            address = i[4] + i[5] + i[6]
            # address = str
            dataline= []
            dataline.append(datarow[0])     #Record ID
            dataline.append(datetime)       #Date/Time of incident
            dataline.append(datarow[3])     #Type of Offence
            dataline.append(address)     #Address
            dataline.append(datarow[7])     #Neighborhood
            dataline.append(datarow[8])     #Police Precint
            dataline.append(datarow[9])     #Police District
            data.append(dataline)
            #data.append(datarow[10] + datarow[11])  #x,y coordinates

    return data


if __name__ == '__main__':
    print(get_data_list('crime_incident_data_recent.txt'))
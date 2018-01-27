import requests
from bs4 import BeautifulSoup
import datetime


if __name__ == '__main__':

    print("""
 (`\ .-') /`   ('-.   ('-.     .-') _    ('-. .-.   ('-.  _  .-')                      .-') _          _ (`-.              _  .-')   .-') _               ('-.         .-') _  _ .-') _   
   `.( OO ),' _(  OO) ( OO ).-.(  OO) )  ( OO )  / _(  OO)( \( -O )                    ( OO ) )        ( (OO  )            ( \( -O ) (  OO) )             ( OO ).-.    ( OO ) )( (  OO) )  
,--./  .--.  (,------./ . --. //     '._ ,--. ,--.(,------.,------.         ,-.-') ,--./ ,--,'        _.`     \ .-'),-----. ,------. /     '._ ,--.       / . --. /,--./ ,--,'  \     .'_  
|      |  |   |  .---'| \-.  \ |'--...__)|  | |  | |  .---'|   /`. '        |  |OO)|   \ |  |\       (__...--''( OO'  .-.  '|   /`. '|'--...__)|  |.-')   | \-.  \ |   \ |  |\  ,`'--..._) 
|  |   |  |,  |  |  .-'-'  |  |'--.  .--'|   .|  | |  |    |  /  | |        |  |  \|    \|  | )       |  /  | |/   |  | |  ||  /  | |'--.  .--'|  | OO ).-'-'  |  ||    \|  | ) |  |  \  ' 
|  |.'.|  |_)(|  '--.\| |_.'  |   |  |   |       |(|  '--. |  |_.' |        |  |(_/|  .     |/        |  |_.' |\_) |  |\|  ||  |_.' |   |  |   |  |`-' | \| |_.'  ||  .     |/  |  |   ' | 
|         |   |  .--' |  .-.  |   |  |   |  .-.  | |  .--' |  .  '.'       ,|  |_.'|  |\    |         |  .___.'  \ |  | |  ||  .  '.'   |  |  (|  '---.'  |  .-.  ||  |\    |   |  |   / : 
|   ,'.   |   |  `---.|  | |  |   |  |   |  | |  | |  `---.|  |\  \       (_|  |   |  | \   |         |  |        `'  '-'  '|  |\  \    |  |   |      |   |  | |  ||  | \   |   |  '--'  / 
'--'   '--'   `------'`--' `--'   `--'   `--' `--' `------'`--' '--'        `--'   `--'  `--'         `--'          `-----' `--' '--'   `--'   `------'   `--' `--'`--'  `--'   `-------'  """)

    response = requests.get('https://katu.com/weather')
    response.raise_for_status()

    html = BeautifulSoup(response.text, 'html.parser')
    html = html.find(class_='weather-boxes-container')
    forecasts = html.find_all(class_='daily-forecast')

    for i, day in enumerate(forecasts):
        date = datetime.datetime.now() + datetime.timedelta(days=i)
        high_temp = day.find(class_='high').text
        low_temp = day.find(class_='low').text
        conditions = day.find(class_='wx-text').text
        chance_of_precip = day.find(class_ = 'wx-conditions').find(class_='value').text
        print(f'Forcast for {date.strftime("%A")} {date.strftime("%x")}')
        print(f"Conditions: {conditions}")
        print(f"High: {high_temp}")
        print(f"Low:  {low_temp}")
        print(f"Chance of Percipitation: {chance_of_precip}")
        print("--------------------------------------------")
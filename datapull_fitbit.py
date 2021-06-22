import fitbit
from fitbit import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime
import json
from pathlib import Path
import sys


# CLIENT_ID = '22BCH2'
# CLIENT_SECRET = '5894fe3f3ee07fb2e767027e98aac37e'
#
# server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
# server.browser_authorize()
#
# ACCESS_TOKEN = server.fitbit.client.session.token['access_token']
# REFRESH_TOKEN = server.fitbit.client.session.token['refresh_token']
#
# client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


# steps_data = client.intraday_time_series('activities/heart', '2019-10-21')
# #
# # df = pd.DataFrame()
# #
# # df=steps_data
# #
# # print(df)


def dumpToFile(data_type, dumpDir, date, data):
    directory = dumpDir / str(date.year) / str(date)
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / "{}.json".format(data_type)).open(mode='w') as f:
        f.write(json.dumps(data, indent=True))



def dumpDay(client, dumpDir: Path, date):
    # steps_data = client.intraday_time_series('activities/date', date)


    # dumpToFile("activity", dumpDir, date, steps_data)
    # dumpToFile("sleep", dumpDir, date, client.get_sleep(date))

    # dumpToFile("calories", dumpDir, date, client.intraday_time_series('activities/calories', date))
    # dumpToFile("distance", dumpDir, date, client.intraday_time_series('activities/distance', date))
    # dumpToFile("floors", dumpDir, date, client.intraday_time_series('activities/floors', date))
    # dumpToFile("elevation", dumpDir, date, client.intraday_time_series('activities/elevation', date)
# )
    dumpToFile("sleep", dumpDir, date, client.sleep(date=date))
    dumpToFile("heartbeat", dumpDir, date, client.intraday_time_series('activities/heart', date))
    dumpToFile("activity", dumpDir, date, client.activities(date=date))
#     dumpToFile("BP", dumpDir, date, client.bp())



def scrapeFromTodayAndBackward(dumpDir: Path, client, limit):
    # dumping
    count = 1
    date = datetime.date.today()
    while count < limit:
        dumpDay(client, dumpDir, date)
        date -= datetime.timedelta(days=1)
        count += 1



def main(_=None):
    # parser = argparse.ArgumentParser(description='Fitbit Scraper')
    # parser.add_argument('--out', metavar='outDir', dest='outDir', required=True,
    #                     help="output data destination folder")
    #
    # args = parser.parse_args()

    dumpDir = Path('Python FitBit')
    startDate = '2019-09-23'

    CLIENT_ID = '22BCH2'
    CLIENT_SECRET = '5894fe3f3ee07fb2e767027e98aac37e'

    server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
    server.browser_authorize()

    ACCESS_TOKEN = server.fitbit.client.session.token['access_token']
    REFRESH_TOKEN = server.fitbit.client.session.token['refresh_token']

    client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN,
                           refresh_token=REFRESH_TOKEN)



    DateRange = 1;
    scrapeFromTodayAndBackward(dumpDir, client,2)


if __name__ == "__main__":
    main(sys.argv[1:])
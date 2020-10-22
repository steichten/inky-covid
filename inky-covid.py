import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from PIL import Image, ImageDraw, ImageFont
import argparse, io
from datetime import datetime, timedelta
from matplotlib import font_manager

# Create the parser
my_parser = argparse.ArgumentParser(description='inky-pHAT dashboard of daily COVID-19 positives')

# Add the arguments
my_parser.add_argument('--state',
                       metavar='state',
                       type=str,
                       help='two-letter US state abbreviation')
my_parser.add_argument('--flip',
                       metavar='flip',
                       type=str,
                       help='flip the display 180 degrees')

# Execute the parse_args() method
args = my_parser.parse_args()


def GrabData(state):
    url = 'https://api.covidtracking.com/v1/states/{}/daily.csv'.format(state)
    df = pd.read_csv(url, nrows=20, parse_dates=['date'])
    return df

df=GrabData(args.state.lower())

x = df["date"]
y = df["positiveIncrease"]
myFmt = mdates.DateFormatter('%m-%d')
current=x[0]

fig, ax = plt.subplots()
ax.plot(x,y)
ax.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()

# define inky-pHAT resolutiom
w, h = (212, 104)
dpi = 144
fig, ax = plt.subplots(figsize=(212/dpi, 104/dpi), dpi=dpi)

fig.subplots_adjust(top=1, bottom=0, left=0.15, right=.95)

ticks_font = font_manager.FontProperties(fname='font1.TTF', size=4)
plt.rcParams['text.antialiased'] = False
for label in ax.get_yticklabels() :
    label.set_fontproperties(ticks_font)
ax.yaxis.set_tick_params(pad=2, width=1)
ax.xaxis.set_ticks([])
ax.set_frame_on(False)
ax.plot(x,y,marker="o",markersize=2)
ax.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()
ax.autoscale_view()

ymin, ymax = ax.get_ylim()

font = ImageFont.truetype('font1.TTF', 16)

with io.BytesIO() as f:
    fig.savefig(f, dpi=dpi, cmap="bwr", interpolation="none", origin="lower", pad_inches=0)
    f.seek(0)
    i = Image.open(f)#.convert('P', palette=(0,1,2))
    d = ImageDraw.Draw(i)


    from inkyphat import RED, BLACK, text, set_image, set_rotation, show
    set_image(i)
    if args.flip:
        set_rotation(180)

    #text((60, 25), '{:.0f}'.format(last_change), BLACK, font)
    text((0, 90), "MN COVID+", BLACK, font)
    text((100,90),'{}: {:.0f}'.format(x[0].strftime('%m-%d'),last_change), RED, font)
    #i.save('test.tif')
    #raise SystemExit

    show()

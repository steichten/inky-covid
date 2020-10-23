# inky-covid

![drawing](https://i.imgur.com/ClLXJvZ.jpeg=250x)

A covid dashboard for the inky pHAT showing the last 20 days of positive cases.

This dashboard uses the [covidtracking.com](covidtracking.com/) API to get a given state's historical results

# installation

This used python 3.7 and the [inky-phat libraries](https://github.com/pimoroni/inky-phat)

```
pip3 install -r requirements.txt
```

# usage

```
usage: inky-covid.py [-h] [--state state] [--flip flip]

inky-pHAT dashboard of daily COVID-19 positives

optional arguments:
  -h, --help     show this help message and exit
  --state state  two-letter US state abbreviation
  --flip flip    flip the display 180 degrees
```

```
python3 inky-covid.py --state mn
```
# license
GPL-3

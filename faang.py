#! /usr/bin/env python      
# https://stackoverflow.com/questions/2429511/why-do-people-write-usr-bin-env-python-on-the-first-line-of-a-python-script

 # Dates & Times. https://atlantictu-my.sharepoint.com/personal/ian_mcloughlin_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fian%5Fmcloughlin%5Fatu%5Fie%2FDocuments%2Fstudent%5Fshares%2Fcomputer%2Dinfrastructure%2F22%2Ddatetime%2Emkv&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Eca70c99c%2D5d51%2D4c6a%2D8743%2D670d34da45a7
import datetime as dt

# Yahoo finance
import yfinance as yf

# Get Data
df = yf.download("META AAPL AMZN NFLX GOOG", period="5d")

# Show current date & time                                        #Ref. - https://docs.python.org/3/library/datetime.html
now = dt.datetime.now()

# File Name
filename = now.strftime("%Y%m%d-%H:%M:%S")+ ".csv"

# Save timestamped csv to Data folder
df.to_csv(filename)



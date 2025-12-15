#! /usr/bin/env python      
# https://stackoverflow.com/questions/2429511/why-do-people-write-usr-bin-env-python-on-the-first-line-of-a-python-script

 # Dates & Times. https://atlantictu-my.sharepoint.com/personal/ian_mcloughlin_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fian%5Fmcloughlin%5Fatu%5Fie%2FDocuments%2Fstudent%5Fshares%2Fcomputer%2Dinfrastructure%2F22%2Ddatetime%2Emkv&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Eca70c99c%2D5d51%2D4c6a%2D8743%2D670d34da45a7
import datetime as dt

# Yahoo finance
import yfinance as yf

# Folder creation + listing files
import os

# Get Data
df = yf.download("META AAPL AMZN NFLX GOOG", period="5d")

# Show current date & time                                        #Ref. - https://docs.python.org/3/library/datetime.html
now = dt.datetime.now()

# File Name
filename = now.strftime("%Y%m%d-%H:%M:%S")+ ".csv"

# Save timestamped csv to Data folder
df.to_csv(filename)

*************************************Need to review below code - plotting not working *******************************
#! /usr/bin/env python      
# https://stackoverflow.com/questions/2429511/why-do-people-write-usr-bin-env-python-on-the-first-line-of-a-python-script

 # Dates & Times. https://atlantictu-my.sharepoint.com/personal/ian_mcloughlin_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fian%5Fmcloughlin%5Fatu%5Fie%2FDocuments%2Fstudent%5Fshares%2Fcomputer%2Dinfrastructure%2F22%2Ddatetime%2Emkv&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Eca70c99c%2D5d51%2D4c6a%2D8743%2D670d34da45a7
import datetime as dt

# Yahoo finance
import yfinance as yf

# Folder creation + listing files
import os

 # Set up the function 'get_data()' that can be called for hourly prices of FAANG stocks over the last 5 days
def get_data(): 
    df = yf.download("META AAPL AMZN NFLX GOOG", period="5d",interval="1h")

    now = dt.datetime.now()             #Ref. - https://docs.python.org/3/library/datetime.html
    now.strftime("%Y%m%d-%H:%M:%S")     #Format date & time for current date & time above as a string -  'now' 
                                        ## Ref. format codes - https://docs.python.org/3/library/datetime.html#format-codes
                                        
    # Create folder called 'data'                  https://www.geeksforgeeks.org/python/python-os-makedirs-method/
    os.makedirs('./data', exist_ok=True)           # exist_ok=True - means when code re-ran no handling error will appear as folder exists - add as markdown cell

    # File Name - Save to data folder # cOMMENT oCT 19TH - nEED TO ADD LOCATION OF folder where file will save
    filename = "data/" + now.strftime("%Y%m%d-%H%M%S")+ ".csv"

# Save timestamped csv to data folder
    df.to_csv(filename)

    return df

# References:
# Python functions - https://www.w3schools.com/python/python_functions.asp
# Yfinance Download -  https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html

 
 # Call the function
df = get_data()

# Load latest file from data folder & plot closing prices

def plot_data(): 
    data_files = os.listdir('./data/')          # List files in data folder
    data_files.sort(reverse=True)
    df = pd.read_csv(f'data/{data_files[0]}',header=[0,1],index_col=0,parse_dates=True) # lecture 33 - 
    
# Closing prices for plotting
    closing_prices = df['Close']

#Create new figure and axis
    fig, ax = plt.subplots()

# Plot closing prices
    closing_prices.plot(ax=ax)

# Labels xlabel and ylabel
    ax.set_xlabel("Date and Time")
    ax.set_ylabel("Closing Prices (USD)")

# Show current date & time                                        #Ref. - https://docs.python.org/3/library/datetime.html
    now = dt.datetime.now()

# Create folder called 'plots'                  https://www.geeksforgeeks.org/python/python-os-makedirs-method/
    os.makedirs('./plots', exist_ok=True)           # exist_ok=True - means when code re-ran no handling error will appear as folder exists - add as markdown cell

# File Name naming convention + save to plots folder
    filename = "./plots/" + now.strftime("%Y%m%d-%H%M%S")+ ".png"

#Title of plot
    ax.set_title(f"Plot of file {data_files[0]} - Closing FAANG Prices" )

#Add Legend 
    ax.legend(title="Stocks", loc="best")    # loc options ref = https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html


# Save figure in plots folder
    fig.savefig(filename, dpi=300)    # dpi ref = https://stackoverflow.com/questions/39870642/how-to-plot-a-high-resolution-graph
    plt.show()
# Call the function
plot_data()





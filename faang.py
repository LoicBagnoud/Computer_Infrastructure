#! /usr/bin/env python

# This imports datetime
from datetime import datetime


# This imports yfinance
import yfinance as yf

# Download function to get the data
df = yf.download(["META", "AAPL", "AMZN", "NFLX", "GOOG"],
        period="5d",
        interval="1h"
        )

# We have our current time
now = datetime.now()

# We have our format
time_format = now.strftime("%Y%m%d-%H%M%S")

# Save it to CSV
data = f"data/{time_format}.csv"
df.to_csv(data)

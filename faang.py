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

# Create new figure and axis.
fig, ax = plt.subplots()

# Plot all closing prices.
df['Close'].plot(ax=ax)

# Give our labels and titles. 

# We need to force the legend to go to the upper right, since it was in the middle of the plot.
ax.legend(loc='upper right')

ax.set_title("Close Price – Last 5 Days")
ax.set_xlabel("Date")
ax.set_ylabel("Price")

# # Format timestamp for filename.
now = datetime.now()
time_format = now.strftime("%Y%m%d-%H%M%S")

# Build file path inside existing 'plots' folder.
filepath = f"plots/{time_format}.png"

# # Save it with our desired resolution.
fig.savefig(filepath, dpi=300)

# YouTube Live View Count Tracker

This project fetches live viewer counts from selected Kenyan TV channels on YouTube and logs the data into an Excel file. It automatically updates the counts at regular intervals using a scheduler.

## Features

- Fetches live concurrent viewer counts from YouTube for multiple channels:
  - Citizen TV
  - NTV
  - KTN
- Stores timestamped viewer counts in an Excel file (`live_view_counts.xlsx`).
- Automatically updates every 5 minutes using a scheduler.
- Works with Nairobi timezone.

## Requirements

- Python 3.8+
- Libraries:
  - `requests`
  - `pandas`
  - `pytz`
  - `schedule`
  - `openpyxl`  

Install dependencies with:

```bash
pip install requests pandas pytz schedule openpyxl

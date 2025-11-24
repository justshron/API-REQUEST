from datetime import datetime
import time
import pytz
import schedule
import requests

# Set timezone to Nairobi
nairobi_tz = pytz.timezone('Africa/Nairobi')
timestamp = datetime.now(nairobi_tz)
import requests
import pandas as pd
from datetime import datetime
import pytz  

# Replace with your API key and video IDs
API_KEY = 'AIzaSyCp07g06SLxDUJKhXWcnP6ktw0ZbsRrZIE'
LIVE_VIDEO_IDS = {
    'Citizen TV': 'Cbdbi44urAE',
    'NTV': 'gWkhyPxMdEQ',
    'KTN': 'g2I779jOLtM'
}
OUTPUT_FILE = 'live_view_counts.xlsx'

def fetch_live_view_counts():
    """
    Fetch live viewer counts for each TV station and append to the Excel file.
    """
    try:
        existing_data = pd.read_excel(OUTPUT_FILE)
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=['Timestamp'] + list(LIVE_VIDEO_IDS.keys()))

    # Get Nairobi time and remove timezone info for Excel
    nairobi_tz = pytz.timezone('Africa/Nairobi')
    timestamp = datetime.now(nairobi_tz).replace(tzinfo=None)

    new_data_row = {'Timestamp': timestamp}

    for station, video_id in LIVE_VIDEO_IDS.items():
        try:
            url = f'https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id={video_id}&key={API_KEY}'
            response = requests.get(url)
            response.raise_for_status()

            video_data = response.json()
            live_details = video_data.get('items', [{}])[0].get('liveStreamingDetails', {})
            view_count = live_details.get('concurrentViewers', 0)

            new_data_row[station] = int(view_count)
        except Exception as e:
            print(f"Error fetching data for {station}: {e}")
            new_data_row[station] = None

    updated_data = pd.concat([existing_data, pd.DataFrame([new_data_row])], ignore_index=True)
    updated_data.to_excel(OUTPUT_FILE, index=False)

    print(f"Data successfully updated in {OUTPUT_FILE}.")
    print(updated_data.tail())

schedule.every(5).minutes.do(fetch_live_view_counts)

print("Scheduler started. Fetching data every 5 minutes...")
fetch_live_view_counts()

while True:
    schedule.run_pending()
    time.sleep(1)
    
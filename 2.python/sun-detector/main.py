import urllib.request
from datetime import datetime
from PIL import Image
import os
import time

# Editable variables
image_url = "https://put-your-url-here.com/webcam/image.jpg"
interval_seconds = 60  # Number of seconds between each image download
max_retries = 2  # Maximum number of retries for server-side errors
retry_delay_seconds = 10  # Number of seconds to wait between retries

# Function to detect sunrise or sunset in an image
def detect_sunrise_sunset(image_path, threshold=5000):
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Resize image for faster processing

    hsv_image = image.convert("HSV")

    sunrise_sunset_hue_range = (0, 30)  # Define the hue range for sunrise/sunset colors, see https://en.wikipedia.org/wiki/Hue#/media/File:HueScale.svg

    sunrise_sunset_pixel_count = 0
    for pixel in hsv_image.getdata():
        hue = pixel[0]
        if sunrise_sunset_hue_range[0] <= hue <= sunrise_sunset_hue_range[1]:
            sunrise_sunset_pixel_count += 1

    if sunrise_sunset_pixel_count > threshold:
        return True
    else:
        return False

# Create directories if they don't exist
os.makedirs("./cam-images/downloads", exist_ok=True)
os.makedirs("./cam-images/sun", exist_ok=True)

try:
    retries = 0
    while True:
        try:
            # Download the image from the provided URL
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_filename = f"./cam-images/downloads/cam-image-{timestamp}.jpg"
            urllib.request.urlretrieve(image_url, image_filename)

            # Detect sunrise or sunset in the downloaded image
            is_sunrise_sunset = detect_sunrise_sunset(image_filename)

            # Move the file to the "sun" directory if sunrise or sunset is detected
            if is_sunrise_sunset:
                new_filename = f"./cam-images/sun/cam-image-{timestamp}.jpg"
                os.rename(image_filename, new_filename)
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Sunrise or sunset detected. File moved to './cam-images/sun'")
            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - No sunrise or sunset detected.")

            retries = 0  # Reset the retry counter on successful request

        except urllib.error.HTTPError as e:
            if 500 <= e.code < 600 and retries < max_retries:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Server-side error ({e.code}). Retrying in {retry_delay_seconds} seconds...")
                retries += 1
                time.sleep(retry_delay_seconds)
                continue
            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Error: {e.code}. Maximum retries reached. Proceeding to the next interval.")

        time.sleep(interval_seconds)

except KeyboardInterrupt:
    print("Script interrupted by the user. Exiting...")
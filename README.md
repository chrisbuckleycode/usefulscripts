# usefulscripts
A mix of useful scripts I have made in python and bash (and hopefully in future, Powershell)

**Important Note!**
The code for these scripts may look unoptimized and messy, insufficient comments etc.

This code is intended first and foremost for my own use, to get 'the job done'. Right now, I prefer to code for as many use cases as possible and leave excess code in there as aide memoires and educational reminders - hopefully one day I will return to optimize, modularize, comment my code. **That is not my priority or goal at this moment**.

**This is of course not how I code in a production, enterprise-level environment** where I would focus on more readable code, modularized structure and generally take a much more collaborative approach!

# bigfiles.sh
Scan home directory (and sub-directories) and report files in decreasing size order. Good for freeing up disk space.

# comic_of_the_day.py
Scrape and display a daily comic image.

# convert_to_csv.py
Convert a particular file format of sentence pairs (native and target foreign language) into a csv-style format for importation into Excel/LibreOffice Calc.

# display_bitcoin_price.py
Scrape and display current bitcoin price.

# download_images_thread_an.py
Download all images from a sub-page of a popular site.

# download_images_thread_bs.py
Download all images from a sub-page of a(nother) popular site.

# move_files.sh
Migrate files from single source to multiple destination directories based on file extension.

# parse_sentences.py
Extract foreign language sentence pairs from a specific pdf.

# randompic.py
Take a random image from a directory and display it on a web page.

# show_rss_on_page.py
Show your favorite rss feeds on a single page.

# sysreport.sh
Full system report displayed in the Terminal and saved to a text file.

# system_health.sh
Basic stats such as uptime, free mem/disk, memory errors, most expensive processes, network connections, virt. memory etc.

# telegraph.py
Post with preview via API to telegra.ph - download and edit markdown.txt. Only single (optional) image url and plain text supported for now. Separate each paragraph with a blank line. Create a file called access_token.txt and put your access token in there. You can obtain an access token and read the rest of the API docs here: https://telegra.ph/api#createAccount

# temps.sh
Record laptop temperatures into a timestamped logfile, ready for import into Excel/LibreOffice Calc for analysis/charting purposes.

# weather.py
Scrape and display local weather forecast.

# web_page_change_monitor.sh
Monitors a web page for changes, logs the time of change and notifies via desktop alert.

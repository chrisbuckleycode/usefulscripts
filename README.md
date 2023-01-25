# usefulscripts
A mix of useful scripts I have made in python and bash (and hopefully in future, Powershell)

**Important Note!**
These scripts are not optimized. They are short and to the point, to get the job done.

# bigfiles.sh
Scan home directory (and sub-directories) and report files in decreasing size order. Good for freeing up disk space.

# bmarks-sort-alpha-title-only.py
Import bookmarks file, populate dictionary with titles and urls. Sort alphabetically by url. Recreate bookmarks file with hyperlinked title only.

# bmarks-sort-alpha-url-title.py
Import bookmarks file, populate dictionary with titles and urls. Sort alphabetically by url. Recreate bookmarks file with hyperlinked url and hyperlinked title.

# comic_of_the_day.py
Scrape and display a daily comic image.

# convert_to_csv.py
Convert a particular file format of sentence pairs (native and target foreign language) into a csv-style format for importation into Excel/LibreOffice Calc.

# crop_image_top.py
Remove banner or in any other way batch crop a number of images.

# display_bitcoin_price.py
Scrape and display current bitcoin price.

# download_images_thread_an.py
Download all images from a sub-page of a popular site.

# download_images_thread_bs.py
Download all images from a sub-page of a(nother) popular site.

# dupe_file_checker.sh
Scans recursively all files and prints a table of those that are duplicated (md5 checksum).

# function_grepper.py
Scans recursively all .py files and greps function names.

# grab_webcam.sh
Download jpg frames of a static webcam feed

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
Post with preview via API to telegra.ph - download and edit markdown.txt. Only single (optional) image url and plain text supported for now. Separate each paragraph with a blank line. Create a file called access_token.txt and put your access token in there. You can obtain an access token and read the rest of the API docs here: https://telegra.ph/api#createAccount Note that there is a mirror for all telegra.ph posts at graph.org

# temps.sh
Record laptop temperatures into a timestamped logfile, ready for import into Excel/LibreOffice Calc for analysis/charting purposes.

# webcam_capture_long.py

Download jpg frames of a dynamic webcam feed (mjpg). For longer, time-lapse, captures.

# webcam_capture_short.py

Download jpg frames of a dynamic webcam feed (mjpg). For shorter, burst, captures.

# web_page_change_monitor.sh
Monitors a web page for changes, logs the time of change and notifies via desktop alert.

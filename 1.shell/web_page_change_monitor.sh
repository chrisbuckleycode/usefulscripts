#!/bin/bash
##
## FILE: web_page_change_monitor.sh
##
## DESCRIPTION: Monitors a url and notifies when underlying page changes.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: web_page_change_monitor.sh
##

# This script downloads a page approx every minute and runs a comparison with the last download.
# As soon as a difference is noticed, it will alert with a desktop notification.
# It also writes a log so if you miss the notification you can see when it fired.

URL="https://www.rivm.nl/sites/default/files/2020-03/20200308%20kaart%20actueel%20corona08032020_mettitel.png"

curl -Is $URL | head -n 1 > reloaded.html

while [[ $stop != "1" ]]; do
    mv reloaded.html original.html 2> /dev/null
    curl -Is $URL | head -n 1 > reloaded.html
    DIFFERENCE="$(diff reloaded.html original.html)"
    if [ "0" = "${#DIFFERENCE}" ]; then
        echo $(date -u) "monitoring, no change yet" >> web_page_change_monitor.txt
        echo "nothing has changed yet, waiting one minute:"
        echo -ne '                       (0%)\r'
        sleep 12
        echo -ne '####                  (20%)\r'
        sleep 12
        echo -ne '########              (40%)\r'
        sleep 12
        echo -ne '############          (60%)\r'
        sleep 12
        echo -ne '################      (80%)\r'
        sleep 12
        echo -ne '#################### (100%)\r'
        echo -ne '\n'
    fi    
    if [ "0" != "${#DIFFERENCE}" ]; then
        echo $(date -u) "RIVM map changed" >> web_page_change_monitor.txt
        notify-send 'Alert!' 'RIVM Map Has Changed!'
        sleep 30
        notify-send 'Alert!' 'RIVM Map Has Changed!'
        sleep 30
        notify-send 'Alert!' 'RIVM Map Has Changed!'
        sleep 30
        notify-send 'Alert!' 'RIVM Map Has Changed!'
        sleep 30
        notify-send 'Alert!' 'RIVM Map Has Changed!'
        sleep 30
        stop=1
    fi  
done

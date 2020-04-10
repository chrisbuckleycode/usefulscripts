System Report

#!/bin/bash
# this script will collect system info and display and save it to a file.

filename="System_Report_$(date +"%FT%H%M%S%z").log"

# filename="test123.log"

touch $filename

echo ""
echo "Report will be opened in LESS. Then press q to quit."
echo ""
echo "Report will also be saved as $filename"
echo ""
echo "REMINDER: you must run this script as sudo. Ctrl-C to quit now"
echo ""
echo ""
read -n1 -r -p "Press any key to continue..." key

stty -echo



# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "External IP Address" >> $filename
echo "" >> $filename
curl --silent ifconfig.me >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "BIOS Information" >> $filename
echo "" >> $filename
dmidecode -t bios >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "Distro Info" >> $filename
echo "" >> $filename
cat /etc/lsb-release >> $filename
cat /etc/os-release >> $filename
cat /etc/issue >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "Last 5 User and System Sessions" >> $filename
echo "" >> $filename
last | head -n 10 >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "Top 10 Memory Processes" >> $filename
echo "" >> $filename
ps aux | sort -rk 4,4 | head -n 10 | awk '{print $4,$11}' >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "No. of Connections by Host - IPv4" >> $filename
echo "" >> $filename
netstat -4tn | awk -F'[\t :]+' '/ESTABLISHED/{hosts[$6]++} END{for(h in hosts){printf("%s\t%s\t",h,hosts[h]);for(i=0;i<hosts[h];i++){printf("*")};print ""}}' >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "Active Internet Use" >> $filename
echo "" >> $filename
lsof -P -i -n >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "CPU Architecture" >> $filename
echo "" >> $filename
lscpu >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "Disk Info" >> $filename
echo "" >> $filename
find /dev/disk/by-id -type l -printf "%l\t%f\n" | cut -b7- | sort >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


# Start Block

echo "" >> $filename
echo "-------------------------------------" >> $filename
echo "Currently Mounted File Systems" >> $filename
echo "" >> $filename
mount | column -t >> $filename
echo "" >> $filename
echo "--- --- --- --- --- --- --- --- --- -" >> $filename
echo ""

# End Block


stty echo

less $filename

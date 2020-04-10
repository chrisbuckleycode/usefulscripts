#!/bin/bash
# this script will scan all files in your home directory (or just the Downloads folder) and then list them in order of descending size using less.

RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo ""
echo ""
echo "List files in descending size order"
echo "Choose an option below and press the Enter key."
echo ""
echo -e "${RED}!!!! IMPORTANT !!!!!"
echo "Press Ctrl-C to cancel at any time!"
echo -e "!!!! IMPORTANT !!!!!${NC}"
echo ""
echo "  1) All files in home directory  -WARNING, may take time, also no TOTALs"
echo "  2) Downloads folder only"
echo "  3) operation 3"
echo "  4) operation 4" 

read choice

case $choice in
  1) find ~ -type f -name "*.*" -print0 | xargs -0 du -sh | sort -h -r -k1 | less;;
  2) find ~/Downloads/ -type f -name "*.*" -print0 | xargs -0 du -sch | sort -h -r -k1 | less;;
  3) echo "You chose Option 3";;
  4) echo "You chose Option 4";;
  *) echo ""; echo ""; echo -e "${CYAN}!! Invalid input!!"; echo "!! Invalid input!!"; echo -e "!! Invalid input!!${NC} , choose again or Ctrl-C to exit"; ./$(basename $0);;
esac

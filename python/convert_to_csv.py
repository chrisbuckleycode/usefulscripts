## FILE: convert_to_csv.py
##
## DESCRIPTION: Converts language sentence pairs document to custom "ampersand-separated" format.
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: python3 convert_to_csv.py
##

# This is used to convert a file of sentence pairs that alternate in language so they are ampersand separated and easily imported like a csv into Excel or LibreOffice Calc.

with open('bigfile.txt', "r") as f:
    lines = f.readlines()
f.close()
with open('bigfile4.csv', "w") as g:
    linecounter = 0
    for line in lines:
        linecounter += 1
        if (linecounter % 2 != 0):
            line = line.strip() + '&'
        g.write(line)        
g.close()

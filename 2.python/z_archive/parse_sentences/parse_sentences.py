## FILE: parse_sentences.py
##
## DESCRIPTION: Parses a PDF and converts sentence pairs to txt format (n.b. very bad early-days code!).
##
## AUTHOR: Chris Buckley (github.com/chrisbuckleycode)
##
## USAGE: python3 parse_sentences.py
##

# TODO(chrisbuckleycode): Refactor this script from my early days!

# If you have access to a particular language course, this script will parse sentence pairs from pdfs for personal use to aid your learning. Works on a single file. If you want to do a batch, I recommend capturing a bare filename listing and creating a batch list of commands.

# pip install PyPDF2

from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup
import re

def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        numpages = pdf.getNumPages()
        
        totalpagetext = ""
        
        for i in range(1, numpages):
            singlepage = pdf.getPage(i)
            singlepagetext = singlepage.extractText()
            totalpagetext = totalpagetext + singlepagetext
        
        soup = BeautifulSoup(totalpagetext)
        stringofsoup = str(soup)
                
        pattern=r'^(SAMPLE.*GRAMMAR[,\s])'

        second=re.search(pattern,stringofsoup,re.MULTILINE | re.DOTALL)
        chunk = second.group(0)
        
        chunkcleaned = '\n'.join(chunk.split('\n')[1:-2])
                
        print(chunkcleaned)
        
        textfile = open(path[:-4] + '.txt', 'w')
              
        textfile.write(chunkcleaned)
        
        textfile.close()
        
        counter = 0
        with open(path[:-4] + '.txt', "r") as f:
            lines = f.readlines()
        with open(path[:-4] + '.txt', "w") as f:
            for line in lines:
                line = line.strip() + '\n'
                if (line.strip("\n") != "CANTONESECLASS101.COM" and
                   "ABSOLUTE BEGINNER" not in line.strip("\n")
                   ):
                    f.write(line)
        f.close()
               
path = 'something.pdf'
text_extractor(path)

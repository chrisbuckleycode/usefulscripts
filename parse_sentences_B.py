# parse pdf
# If you have access to a particular language course, this script will parse sentence pairs from pdfs for personal use to aid your learning. Works on a single file. If you want to do a batch, I recommend capturing a bare filename listing and creating a batch list of commands.

# sudo -H pip3 install --upgrade setuptools
# sudo apt-get install python3-dev
# sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python-dev
# sudo -H pip3 install pdftotext

import pdftotext
import io


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = pdftotext.PDF(f)
        numpages = len(pdf)
        # print("number of pages is " + str(numpages))
        
        
        
        
        # get the first page
        # page = pdf.getPage(1)
        # print(page)
        # print('Page type: {}'.format(str(type(page))))

        # text = page.extractText()
        # print(text)
        
        totalpagetext = ""
        # print (totalpagetext)
        
        for i in range(48, 311):
            singlepagetext = pdf[i]
            # print(singlepagetext)
            totalpagetext = totalpagetext + singlepagetext
            
            
        # print(totalpagetext)
        
        newbuffer = io.StringIO(totalpagetext)
        
        # strip leading spaces
        
        line_lst = [line.lstrip() for line in newbuffer.readlines()]
        totalpagetext = ''.join(line_lst)
        
        # print(totalpagetext)
        
        # write to .txt file
        textfile = open(path[:-4] + '.txt', 'w')
              
        textfile.write(totalpagetext)
        
        textfile.close()
        
        
        
        # read the lines out of the text file
        with open(path[:-4] + '.txt', "r") as g:
            lines = g.readlines()
        g.close()
        
        # read the text file and extract only starting with YALE or EN
        with open(path[:-4] + '.txt', "w") as h:
            for line in lines:
                line = line.strip() + '\n'
                # print(line)
                if (line.startswith('EN ') == True or line.startswith('YALE') == True):
                # if (line.startswith('EN ') == True or line.startswith('YALE') == True or line.startswith('JYUT') == True):
                    h.write(line)
        h.close()


        # create spaced file, carriage return after every second/third line

        # reading in lines again
        with open(path[:-4] + '.txt', "r") as k_read:
            lines = k_read.readlines()
        k_read.close()
        
        
        with open(path[:-4] + '_spaced' + '.txt', "w") as k:
            linecounter = 0
            for line in lines:
                linecounter += 1
                # for every even line. set as 2 for two or 3 for three languages
                if (linecounter % 2 == 0):
                    line = line.strip() + '\n' + '\n'
                k.write(line)        
        k.close()        
     
        
        
        # create csv
        with open(path[:-4] + '.txt', "r") as i:
            lines = i.readlines()
        i.close()
        
        with open(path[:-4] + '.csv', "w") as j:
            linecounter = 0
            for line in lines:
                linecounter += 1
                # for every non-even line. set as 2 for two or 3 for three languages
                if (linecounter % 2 != 0):
                    line = line.strip() + '&'
                j.write(line)        
        j.close()        
        
   
        
        
        
        


        
path = 'g.pdf'
text_extractor(path)





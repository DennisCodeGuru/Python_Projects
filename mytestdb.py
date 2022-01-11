#import os for open file ArithmeticError.txt
import os
#import sqlite for create DB
import sqlite3
# Create DB and connect
conn = sqlite3.connect('mytest.db')
# Create table book
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_book(\
        book_id INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_title TEXT, \
        col_isbn TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('mytest.db')
#tuple of file
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
#loop through each object in the tuple to find the file names from the list ending with “.txt”
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
        # Will denote a one element tuple for each name ending with .txt
            cur.execute("INSERT INTO tbl_book(col_title) VALUES(?)", (x,))
            print(x)
conn.close()


# supplied
def openFile():    
    with open('hello.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()

if __name__ == "__main__":
    openFile()


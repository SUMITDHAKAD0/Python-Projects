import pyttsx3
import PyPDF2

book = open('oop.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(f'Book Contains {pages} Pages')

start = int(input('enter the page where you want to start reading '))
end = int(input('enter page number, as far as you want to read '))
try:
    speaker = pyttsx3.init()
    for num in range(start, end):
        pages = pdfReader.getPage(num)
        text = pages.extractText()
        print(text)
        speaker.say(text)
        speaker.runAndWait()
    book.close()
except:
    print('enter valid page number')
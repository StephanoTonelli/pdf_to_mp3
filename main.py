import PyPDF2
import pyttsx3

pdfreader = PyPDF2.PdfReader(open("GoPro.pdf", 'rb'))
speaker = pyttsx3.init()

for page_n in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_n].extract_text()
    clean_text = text.strip().replace("\n"," ")
    print(clean_text)

speaker.save_to_file(clean_text, "audio.mp3")
speaker.runAndWait()

speaker.stop()

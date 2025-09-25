import pyttsx3
from pypdf import PdfReader

# Load the PDF
reader = PdfReader("C++.pdf")

# Access the correct page (0-based index)
page = reader.pages[3]

# Extract text from the page
text = page.extract_text()

# Initialize text-to-speech engine
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()

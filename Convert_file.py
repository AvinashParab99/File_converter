from tkinter import *
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2



# Function to convert hexadecimal to binary
def hex_to_binary(hex_string):
    # Remove non-hex characters from the string
    clean_hex_string = ''.join(c for c in hex_string if c.isdigit() or (c.isalpha() and c.lower() in 'abcdef'))

    try:
        decimal_integer = int(clean_hex_string, 16)  # Convert cleaned hexadecimal to decimal
        binary_string = bin(decimal_integer)[2:]  # Convert decimal to binary, remove '0b' prefix
        return binary_string
    except ValueError:
        return "Invalid hexadecimal input"

def openFile_hexa():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Admin\\PycharmProjects\\Main",
                                          title="Open file ",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))

    if filepath:
        output_file = "output_binary_file.txt"
        hex_file_to_binary_file(filepath, output_file)
        print("Hex file has been converted to Binary file.")
        window.destroy()

# Function to convert hexadecimal file to binary file
def hex_file_to_binary_file(input_file, output_file):
    with open(input_file, 'r') as file:
        hex_data = file.read().splitlines()

    binary_data = [hex_to_binary(hex_string) for hex_string in hex_data]

    with open(output_file, 'w') as file:
        file.writelines("%s\n" % binary_string for binary_string in binary_data)

# -----------------------------function to convert text file to pdf file---------------------------------------------------------

def text_to_pdf(filepath1, output_file1):
        with open(filepath1, 'r', encoding='utf-8') as input_file:
            text_content = input_file.read()

        c = canvas.Canvas(output_file1, pagesize=letter)
        width, height = letter

        # Set font and font size
        c.setFont("Helvetica", 12)

        # Split text content into lines to fit in PDF
        lines = text_content.split('\n')

        # Calculate line height
        line_height = 14

        # Set starting y-coordinate
        y = height - 50

        # Write text to PDF
        for line in lines:
            c.drawString(50, y, line)
            y -= line_height

            # Check if new page is needed
            if y <= 50:
                c.showPage()
                y = height - 50

        c.save()

    # Example usage



#2nd
def openFile_text2pdf():
    filepath1 = filedialog.askopenfilename(initialdir="C:\\Users\\Admin\\PycharmProjects\\Main",
                                              title="Open file ",
                                              filetypes=(("text files", "*.txt"),
                                                         ("all files", "*.*")))

    if filepath1:
        output_file1 = "output1.pdf"
        text_to_pdf(filepath1, output_file1)
        print("Text file has been converted to PDF.")
        window.destroy()
# ------------------------------------function to convert pdf file to text file----------------------------------------------------
#3rd
def openFile_pdf2text():
    filepath2 = filedialog.askopenfilename(initialdir="C:\\Users\\Admin\\PycharmProjects\\Main",
                                              title="Open file ",
                                              filetypes=(("text files", "*.txt"),
                                                         ("all files", "*.*")))

    if filepath2:
        output_file2 = "New_output.txt"
        pdf_to_text(filepath2, output_file2)
        print("PDF file has been converted to text.")

        window.destroy()


def pdf_to_text(filepath2, output_file2):
    pdf_file = open(filepath2, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text_content = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text_content += page.extract_text()

    pdf_file.close()

    with open(output_file2, 'w', encoding='utf-8') as output_file:
        output_file.write(text_content)






choise = int(input('Hey Welcome ! Select your option\n1) HEX_FILE TO DECIMAL_FILE \n2) TEXT_FILE TO PDF\n3) PDF_FILE TO TEXT_FILE\n'))

if choise == 1:
    window = Tk()
    window.geometry("420x210")
    window.title("file converter")

    welcome = Label(window, text="Select File From Your  Device")
    welcome.place(x=0, y=0)

    file_button = Button(window, text="Open", command=openFile_hexa)
    file_button.pack()

    window.mainloop()

elif choise == 2:
    window = Tk()
    window.geometry("420x420")
    window.title("file converter")

    welcome = Label(window, text="Select Your File From Device")
    welcome.place(x=0, y=0)

    file_button = Button(window, text="Open", command=openFile_text2pdf)
    file_button.pack()

    window.mainloop()

elif choise == 3:
    window = Tk()
    window.geometry("420x420")
    window.title("file converter")

    welcome = Label(window, text="Select Your File From Device")
    welcome.place(x=0, y=0)

    file_button = Button(window, text="Open", command=openFile_pdf2text)
    file_button.pack()

    window.mainloop()

















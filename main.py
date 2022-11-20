import pyperclip

def whitespace_remover (paragraph):
    
    #new lines?
    paragraph = paragraph.strip()
    paragraph = paragraph.split(" ")

    while "" in paragraph:
        paragraph.remove("")

    paragraph = " ".join(paragraph)

    return pyperclip.copy(paragraph)
    


text = str()

while text != "q":
    text = str(input("\nPLEASE ENTER YOUR TEXT or PRESS q TO EXIT: \n"))
    if text != 'q':
        whitespace_remover(text)
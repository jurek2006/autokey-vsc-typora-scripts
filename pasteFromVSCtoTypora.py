# Skrypt do wklejania fragmentów kodu zskopiowanych z VSC do Typory, tak, żeby mogła rozpoznać nazwę pliku przy wklejaniu i wkleić tę nazwę jako nagłówek odpowiedniego poziomu, a następnie kod, jako javascript lub python (w zależności od rozszerzenia pliku)
# Należy go umieścić w ~/.config/autokey/data
import time

programName = "- Visual Studio Code"
filenameEndMarkup = "[/title]" #znacznik końca nazwy pliku dołączanej przed treścią zaznaczenia
headingMarkup = "##### " #znacznik (markup) stosowany do nazwy wklejanego pliku


fromclipboard = clipboard.get_clipboard()

title = headingMarkup + fromclipboard[0:fromclipboard.find(programName)].strip() # wyodrębnienie tytułu (i dodanie do niego znacznika headingu)
code = fromclipboard[fromclipboard.find(programName) + len(programName) + len(filenameEndMarkup):] # wyodrębnienie kodu (bez tytułu i znacznika końca tytułu)

clipboard.fill_clipboard(title) #wysłanie do schowka nazwy pliku
keyboard.send_keys("<ctrl>+v")
keyboard.send_key("<enter>")

time.sleep(0.25)

keyboard.send_keys("```javascript")
keyboard.send_key("<enter>")

time.sleep(0.25)

clipboard.fill_clipboard(code) #wysłanie do schowka kopiowanego kodu
# dialog.info_dialog("Test", "test '%s'." % ('Testowy'))

time.sleep(0.5)
keyboard.send_keys("<ctrl>+v")

# time.sleep(0.25) #wysłanie do schowka ponownie całości kopiowanego schowka
# clipboard.fill_clipboard(fromclipboard)
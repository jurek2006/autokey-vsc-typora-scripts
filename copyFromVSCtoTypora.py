# Skrypt do kopiowania fragmentów kodu z VSC do Typory, tak, żeby mogła rozpoznać nazwę pliku przy wklejaniu
# Skrypt do kopiowania fragmentów kodu, więc dodaje ... przed i po fragmencie kodu
# Jeśli kopiowanie nie odbywa się z Visual Studio Code to wyświetla okno ostrzeżenia i kopiuje "normalnie"
# Należy go umieścić w ~/.config/autokey/data

programName = "Visual Studio Code"
filenameEndMarkup = "[/title]" #znacznik końca nazwy pliku dołączanej przed treścią zaznaczenia
snippetStart = "...\n" #znacznik dodawany przed fragmentem kopiowanego kodu 
snippetEnd = "\n..." #znacznik dodawany po fragmencie kopiowanego kodu 

winTitle = window.get_active_title() #pobranie tytułu okna w którym uruchomiono skrypt
selection = clipboard.get_selection()

if winTitle.find(programName) > -1:
    toClipboard = winTitle + filenameEndMarkup + snippetStart + selection + snippetEnd
    clipboard.fill_clipboard(toClipboard)
else:
    clipboard.fill_clipboard(selection)
    dialog.info_dialog("Błąd", "Kopiowanie specjalne działa tylko w '%s'. Skopiowano normalnie" % (programName))
    
# Skrypt do kopiowania fragmentów kodu z VSC do Typory, tak, żeby mogła rozpoznać nazwę pliku przy wklejaniu
# Należy go umieścić w ~/.config/autokey/data

filenameEndMarkup = "[/title]" #znacznik końca nazwy pliku dołączanej przed treścią zaznaczenia
winTitle = window.get_active_title() #pobranie tytułu okna w którym uruchomiono skrypt
selection = clipboard.get_selection()

if winTitle.find("Visual Studio Code") > -1:
    toClipboard = winTitle + filenameEndMarkup + selection
    clipboard.fill_clipboard(toClipboard)
    dialog.info_dialog("Kopiowanie", "Kopiowanie z\n'%s'" % (toClipboard))
else:
    clipboard.fill_clipboard(selection)
    dialog.info_dialog("Błąd", "Kopiowanie specjalne działa tylko w '%s'. Skopiowano normalnie" % ("VSC"))
    
# Skrypt do wklejania fragmentów kodu zskopiowanych z VSC do Typory, tak, żeby mogła rozpoznać nazwę pliku przy wklejaniu i wkleić tę nazwę jako nagłówek odpowiedniego poziomu, a następnie kod, jako javascript lub python (w zależności od rozszerzenia pliku)
# Należy go umieścić w ~/.config/autokey/data
import time

keyboard.send_keys("```javascript")
keyboard.send_key("<enter>")

time.sleep(0.25)
keyboard.send_keys(" <ctrl>+v")

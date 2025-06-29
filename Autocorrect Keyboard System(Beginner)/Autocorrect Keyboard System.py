from spellchecker import SpellChecker  # type: ignore
import tkinter as tk


spell = SpellChecker()

def autocorrect():
    text = entry.get()
    words = text.split()
    misspelled = spell.unknown(words)
    
    corrected_words = []
    for word in words:
        if word in misspelled:
            corrected_words.append(spell.correction(word))
        else:
            corrected_words.append(word)
    
    corrected_text = " ".join(corrected_words)
    result_var.set(corrected_text)


root = tk.Tk()
root.title("Autocorrect Keyboard System")


entry = tk.Entry(root, width=50, font=("Arial", 14))
entry.pack(pady=10)


tk.Button(root, text="Autocorrect", command=autocorrect).pack()


result_var = tk.StringVar()
output = tk.Label(root, textvariable=result_var, font=("Arial", 14), fg="blue", wraplength=500)
output.pack(pady=10)

root.mainloop()

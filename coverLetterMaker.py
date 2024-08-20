import tkinter as tk
from tkinter import scrolledtext

# Template for the cover letter
cover_letter_template = """
Dear Hiring Manager,

I am writing to express my interest in the {job_title} position at {company_name}.

Sincerely,
Taimur Adam
"""

def generate_cover_letter():
    # Get values from the entries
    job_title = entry_job_title.get()
    company_name = entry_company_name.get()

    # Generate the cover letter
    cover_letter = cover_letter_template.format(
        job_title=job_title,
        company_name=company_name,
    )

    # Display the cover letter in the text area
    txt_cover_letter.delete(1.0, tk.END)
    txt_cover_letter.insert(tk.INSERT, cover_letter)

# Create the main window
root = tk.Tk()
root.title("Cover Letter Generator")

# Create and place labels and entries for each field
labels_entries = [
    ("Job Title", "job_title"),
    ("Company Name", "company_name"),
]

entries = {}
for i, (label_text, var_name) in enumerate(labels_entries):
    tk.Label(root, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky=tk.E)
    entry = tk.Entry(root, width=50)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries[var_name] = entry

entry_job_title = entries["job_title"]
entry_company_name = entries["company_name"]

# Create a button to generate the cover letter
tk.Button(root, text="Generate Cover Letter", command=generate_cover_letter).grid(row=len(labels_entries), columnspan=2, pady=10)

# Create a scrolled text widget to display the cover letter
txt_cover_letter = scrolledtext.ScrolledText(root, width=80, height=20)
txt_cover_letter.grid(row=len(labels_entries) + 1, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()

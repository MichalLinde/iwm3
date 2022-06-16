import tkinter
from tkinter import *

# First create application class


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.name = ""

        self.pack()
        self.create_widgets()

    # Create main GUI window
    def create_widgets(self):
        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.titleLabel = Label(self, text="Wybierz pacjenta", font=("Arial", 32))
        self.entry = Entry(self, textvariable=self.search_var, width=13)
        self.lbox = Listbox(self, width=45, height=15)
        self.lbox.bind("<Double-Button-1>", self.pop_window)

        self.titleLabel.grid(row=0, column=0, padx=10, pady=3)
        self.entry.grid(row=1, column=0, padx=10, pady=3)
        self.lbox.grid(row=2, column=0, padx=10, pady=3)

        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def update_list(self, *args):
        search_term = self.search_var.get()

        # Just a generic list to populate the listbox
        lbox_list = ["Jan Kowalski", "Szymon Sielecki", "Adam Nowak", "Bruce Wayne", "Adam Smasher", "Tony Stark", "Peter Parker",
            "Jan Kowalski", "Szymon Sielecki", "Adam Nowak", "Bruce Wayne", "Adam Smasher", "Tony Stark", "Peter Parker",
            "Jan Kowalski", "Szymon Sielecki", "Adam Nowak", "Bruce Wayne", "Adam Smasher", "Tony Stark", "Peter Parker",
            "Jan Kowalski", "Szymon Sielecki", "Adam Nowak", "Bruce Wayne", "Adam Smasher", "Tony Stark", "Peter Parker",
            "Jan Kowalski", "Szymon Sielecki", "Adam Nowak", "Bruce Wayne", "Adam Smasher", "Tony Stark", "Peter Parker",
            "Jan Kowalski", "Szymon Sielecki", "Adam Nowak", "Bruce Wayne", "Adam Smasher", "Tony Stark", "Peter Parker",
            "Jan Kowalski", "Szymon Sielecki", "Adam Nowak", "Bruce Wayne", "Adam Smasher", "Tony Stark", "Peter Parker"]

        self.lbox.delete(0, END)

        for item in lbox_list:
                if search_term.lower() in item.lower():
                    self.lbox.insert(END, item)

    def pop_window(self, dummy_event):
        data = self.lbox.get(self.lbox.curselection()[0])
        self.name = data
        print(self.name)
        #top = tkinter.Toplevel(root)
        self.details_frame()

    def details_frame(self):
        details = Toplevel()
        details.title = "Dane pacjenta"

        detailsNameLabel = tkinter.Label(master=details, text=self.name, font=("Arial", 32))
        detailsNameLabel.grid(row=0, column=0, padx=10, pady=3)


root = Tk()
root.title('Dane medyczne')
app = Application(master=root)
print('Starting mainloop()')
app.mainloop()
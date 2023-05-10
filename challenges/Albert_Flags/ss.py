import tkinter as tk
import sys
import time
import os


class SelfScanCheckout:
    def __init__(self, master):
        self.master = master
        master.title("Self-Scan Checkout")

        self.welcome_label = tk.Label(master, text="Welcome to the Albert Flags self checkout,\nplease scan your item", font=("Arial", 28))
        self.input_label = tk.Label(master, text="Scan item:", font=("Arial", 18))
        self.input_entry = tk.Entry(master, width=100, font=("Arial", 18))
        self.input_entry.bind("<Return>", self.add_item)

        self.textbox = tk.Text(master, width=80, state=tk.DISABLED, font=("Arial", 32))

        self.welcome_label.pack()

        self.textbox.pack()
        self.input_label.pack()
        self.input_entry.pack()

        self.input_entry.focus() 

        # Bind Ctrl-Q to exit the program -> disabled so hackers can't exit the program and read the debug log!
        #master.bind("<Control-q>", self.exit_program)

        self.items = []
        self.totalItems = 0

    def add_item(self, event):
        inp = self.input_entry.get()

        if inp == "End":
            total = self.calculate_total()
            self.checkout_screen(total)

        else:
            self.totalItems+=1
            item_name = self.get_product(inp)
            if item_name != "Unknown product":
                self.items.append(item_name) 

            self.textbox.config(state=tk.NORMAL) # enable the textbox to insert text
            self.textbox.insert(tk.END, item_name + "\n")
            self.textbox.config(state=tk.DISABLED) # disable the textbox again
            self.input_entry.delete(0, tk.END)
            self.input_entry.focus() # set focus back to the input entry widget
        
    def exit_program(self, event):
        global soft_exit
        soft_exit = False
        os.system("clear")
        time.sleep(0.5)
        self.master.destroy() # destroy the root window to exit the program

    def checkout_screen(self, total):

        label_text = "Your subtotal is "+total+" euro."


        # Remove existing widgets
        self.input_label.pack_forget()
        self.input_entry.pack_forget()
        self.textbox.pack_forget()
        self.welcome_label.pack_forget()

        # Create new widgets
        self.new_label = tk.Label(self.master, text=label_text, font=("Arial", 50))
        self.new_label.pack()

        self.new_input_label = tk.Label(self.master, text="Scan \"new checkout\" for new order", font=("Arial", 18))
        self.new_input_label.pack()

        self.new_input_entry = tk.Entry(self.master, width=30)
        self.new_input_entry.pack()

        self.new_input_entry.focus() # set focus on the new input entry widget



        # Bind Enter to add_item method
        self.new_input_entry.bind("<Return>", self.reset)

    def get_product(self, number):
        with open('products.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                if parts[0] == number:
                    return parts[1]
        return "Unknown product"


    def calculate_total(self):
        try:
            total = 0
            for i in range(self.totalItems):
                with open('prices.txt', 'r') as file:
                    for line in file:
                        parts = line.strip().split(', ')
                        if parts[0] == self.items[i]:
                            total += int(parts[1])
            return str(total)
        except:
            self.master.destroy()
            raise Exception("Error occured!")

    def reset(self, _):
        # Reset input box and text box
        self.new_label.pack_forget()
        self.new_input_label.pack_forget()
        self.new_input_entry.pack_forget()

        self.input_entry.delete(0, tk.END)
        self.textbox.config(state=tk.NORMAL) # enable the textbox to insert text
        self.textbox.delete("1.0", tk.END)
        self.textbox.config(state=tk.DISABLED) # disable the textbox again

        # Reset variable to 0
        self.items = []
        self.totalItems = 0

        # Re-show the initial screen
        self.welcome_label.pack()
        self.textbox.pack()
        self.input_label.pack()
        self.input_entry.pack()
        self.input_entry.bind("<Return>", self.add_item)
        self.input_entry.focus() # set focus back to the input entry widget
        

if len(sys.argv) < 2:
    print("No api flag given!\nExitting!!!!1!!")
    exit()

if not sys.argv[1].startswith("UHCTF"):
    print("Bad api flag given!\nExitting!!!11!")
    exit()


soft_exit = 1
while soft_exit:
    print("Debug log")
    print("Version 1.56")
    print("Api flag in use:", sys.argv[1])
    print()
    print("Restarting")
    for _ in range(5):
        time.sleep(1)
        print(".", end="",flush=True)
    print("\nDone!")
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    my_gui = SelfScanCheckout(root)
    root.mainloop()

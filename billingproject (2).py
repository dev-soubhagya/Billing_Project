import random
from tkinter import *
root = Tk()
bg_color = "blue"
fg_color = "yellow"
lbl_color = 'white'

class Pharmacy_Billing(object):

    def __init__(self, root):
        self.root = root
        self.root.maxsize(width=1370, height=720)
        self.root.minsize(width=1370, height=720)
        self.root.title("Pharmacy Billing System")

        # this function for variables
        self.customer_name = StringVar()
        self.customer_contact_number = StringVar()

        # this function for Generating Random Invoice Numbers
        x = random.randint(1, 9999)
        self.cus_invoice_no = StringVar()

        # this fucntion is to Set Value to a variable
        self.cus_invoice_no.set(str(x))
        self.medicol_advance = IntVar()
        self.toseran_forte = IntVar()
        self.imodium = IntVar()
        self.mefenamic = IntVar()
        self.amoxicillin = IntVar()
        self.tiki_tiki_star = IntVar()
        self.neutrilin_drops = IntVar()
        self.profan_tlc = IntVar()
        self.ceelin_plus = IntVar()
        self.cheriper = IntVar()
        self.lidocaine_ointment = IntVar()
        self.canesten_cream = IntVar()
        self.tabeta_ointment = IntVar()
        self.nerisone_ointment = IntVar()
        self.clotrimazole_cream = IntVar()
        self.total_medicine = StringVar()
        self.total_vitamins = StringVar()
        self.total_cream_ointment = StringVar()
        self.tax_medicine = StringVar()
        self.tax_vitamins = StringVar()
        self.tax_cream_ointment = StringVar()



        # This function for title frame
        title = Label(self.root, text="Pharmacy Billing System", bd=12, relief=RAISED, fg=fg_color, bg=bg_color,
        font=("Calibri", 36, "bold"), pady=3).pack(fill=X)

        # This function for Customers Frame
        F1 = LabelFrame(text="Customer Information", font=("Calibri", 12, "bold"), fg="gold", bg=bg_color,
        relief=RAISED, bd=10)
        F1.place(x=0, y=80, relwidth=1)

        # This function for customer name
        customername_lbl = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color,
        font=("Calibri", 15, "bold")).grid(row=0, column=0, padx=10, pady=5)
        customername_en = Entry(F1, bd=8, relief=RAISED, textvariable=self.customer_name)
        customername_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        # This function for customer contact number
        customercontact_lbl = Label(F1, text="Phone No", bg=bg_color, fg=fg_color, font=("Calibri", 15, "bold")).grid(
        row=0, column=2, padx=20)
        customercontact_en = Entry(F1, bd=8, relief=RAISED, textvariable=self.customer_contact_number)
        customercontact_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # This fucntion for Invoice Number
        customerinvoice_lbl = Label(F1, text="Invoice No.", bg=bg_color, fg=fg_color, font=("Calibri", 15, "bold"))
        customerinvoice_lbl.grid(row=0, column=4, padx=20)
        customerinvoice_en = Entry(F1, bd=8, relief=RAISED, textvariable=self.cus_invoice_no)
        customerinvoice_en.grid(row=0, column=5, ipadx=30, ipady=4, pady=5)

        # This function for Invoice Search Button
        invoice_btn = Button(F1, text="Enter", bd=7, relief=RAISED, font=("Calibri", 12, "bold"), bg=bg_color,
        fg=fg_color)
        invoice_btn.grid(row=0, column=6, ipady=5, padx=60, ipadx=19, pady=5)

        # This function for Medicine Capsule Frame
        F2 = LabelFrame(self.root, text='Medicine Capsule', bd=10, relief=RAISED, bg=bg_color, fg="gold",
        font=("Calibri", 13, "bold"))
        F2.place(x=5, y=180, width=325, height=380)

        # This function for Medicol Advance
        medicol_advance_lbl = Label(F2, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Medicol Advance")
        medicol_advance_lbl.grid(row=0, column=0, padx=10, pady=20)
        medicol_advance_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.medicol_advance)
        medicol_advance_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # This function for Toseran Forte
        toseran_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Toseran Forte")
        toseran_lbl.grid(row=1, column=0, padx=10, pady=20)
        toseran_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.toseran_forte)
        toseran_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # This function for Imodium
        imodium_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Imodium")
        imodium_lbl.grid(row=2, column=0, padx=10, pady=20)
        imodium_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.imodium)
        imodium_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # This function for Mefenamic
        mefenamic_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Mefenamic")
        mefenamic_lbl.grid(row=3, column=0, padx=10, pady=20)
        mefenamic_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.mefenamic)
        mefenamic_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # This function for Amoxicillin
        amoxicillin_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Amoxicillin")
        amoxicillin_lbl.grid(row=4, column=0, padx=10, pady=20)
        amoxicillin_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.amoxicillin)
        amoxicillin_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # This function for Vitamins Frame
        F2 = LabelFrame(self.root, text='Vitamins', bd=10, relief=RAISED, bg=bg_color, fg="gold",
        font=("Calibre", 13, "bold"))
        F2.place(x=330, y=180, width=325, height=380)

        # This function for Tiki tiki Star
        tikitiki_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Tiki Tiki Star")
        tikitiki_lbl.grid(row=0, column=0, padx=10, pady=20)
        tikitiki_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.tiki_tiki_star)
        tikitiki_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # This function for Neutrilin Drops
        neutrilin_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Neutrilin Drops")
        neutrilin_lbl.grid(row=4, column=0, padx=10, pady=20)
        neutrilin_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.neutrilin_drops)
        neutrilin_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # This function for Profan Tlc
        profan_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Profan Tlc")
        profan_lbl.grid(row=1, column=0, padx=10, pady=20)
        profan_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.profan_tlc)
        profan_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # This function for Ceelin PLus
        ceelin_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Ceelin Plus")
        ceelin_lbl.grid(row=2, column=0, padx=10, pady=20)
        ceelin_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.ceelin_plus)
        ceelin_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # This function for Cheriper
        cheriper_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Cheriper")
        cheriper_lbl.grid(row=3, column=0, padx=10, pady=20)
        cheriper_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.cheriper)
        cheriper_en.grid(row=3, column=1, ipady=5, ipadx=5)



        # This function for Cream and Ointment
        F2 = LabelFrame(self.root, text='Cream and Ointment', bd=10, relief=RAISED, bg=bg_color, fg="gold", font=("Calibre", 13, "bold"))
        F2.place(x=655, y=180, width=325, height=380)

        # This function for Lidocaine Ointment
        licodaine_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Lidocaine Ointment")
        licodaine_lbl.grid(row=0, column=0, padx=10, pady=20)
        licodaine_en = Entry(F2, bd=10, relief=RAISED, textvariable=self.lidocaine_ointment)
        licodaine_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # This function for Canesten Cream
        canesten_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Canesten Cream")
        canesten_lbl.grid(row=1, column=0, padx=10, pady=20)
        canesten_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.canesten_cream)
        canesten_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # This function for Tabeta Ointment
        tabeta_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Tabeta Ointment")
        tabeta_lbl.grid(row=2, column=0, padx=10, pady=20)
        tabeta_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.tabeta_ointment)
        tabeta_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # This function for Nerizone Ointemnt
        nerizone_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="Nerizone Ointemnt")
        nerizone_lbl.grid(row=3, column=0, padx=10, pady=20)
        nerizone_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.nerisone_ointment)
        nerizone_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # This function for CLotrimazole Cream
        clotrimazole_lbl = Label(F2, font=("Calibre", 15, "bold"), fg=lbl_color, bg=bg_color, text="CLotrimazole Cream")
        clotrimazole_lbl.grid(row=4, column=0, padx=10, pady=20)
        clotrimazole_en = Entry(F2, bd=8, relief=RAISED, textvariable=self.clotrimazole_cream)
        clotrimazole_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # This function for Reciept Area frames
        F3 = Label(self.root, bd=10, relief=RAISED)
        F3.place(x=1010, y=180, width=350, height=350)
        # ===========
        receipt_title = Label(F3, text="Receipt Area", font=("Lucida", 13, "bold"), bd=7, relief=RAISED)
        receipt_title.pack(fill=X)

        #This function for Scroll bar Button frames
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.txt = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # This function for Buttons Frame
        F4 = LabelFrame(self.root, text='Total Menu', bd=10, relief=RAISED, bg=bg_color, fg="gold",
        font=("Calibri", 13, "bold"))
        F4.place(x=0, y=560, relwidth=1, height=145)

        # This function for Total Medicine
        medicine_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Medicine")
        medicine_lbl.grid(row=0, column=0, padx=10, pady=0)
        medicine_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.total_medicine)
        medicine_en.grid(row=0, column=1, ipady=2, ipadx=5)

        # This function for Total Vitamins
        vitamins_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Vitamins")
        vitamins_lbl.grid(row=1, column=0, padx=10, pady=5)
        vitamins_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.total_vitamins)
        vitamins_en.grid(row=1, column=1, ipady=2, ipadx=5)

        # This function for Total cream and ointment
        cream_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Cream and Ointment")
        cream_lbl.grid(row=2, column=0, padx=10, pady=5)
        cream_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.total_cream_ointment)
        cream_en.grid(row=2, column=1, ipady=2, ipadx=5)

        #This function for Tax Medicine
        taxmedicine_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Medicine Tax")
        taxmedicine_lbl.grid(row=0, column=2, padx=30, pady=0)
        taxmedicine_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.tax_medicine)
        taxmedicine_en.grid(row=0, column=3, ipady=2, ipadx=5)

        # This function for tax Vitamins
        vitamins_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Vitamins Tax")
        vitamins_lbl.grid(row=1, column=2, padx=30, pady=5)
        vitamins_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.tax_vitamins)
        vitamins_en.grid(row=1, column=3, ipady=2, ipadx=5)

        # This function for Tax Cream and Ointment
        ointment_lbl = Label(F4, font=("Calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Cream and Ointment Tax")
        ointment_lbl.grid(row=2, column=2, padx=10, pady=5)
        ointment_en = Entry(F4, bd=8, relief=RAISED, textvariable=self.tax_cream_ointment)
        ointment_en.grid(row=2, column=3, ipady=2, ipadx=5)

        # This function for Total Button
        total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=RAISED,
        command=self.total_section)
        total_btn.grid(row=1, column=4, ipadx=20, padx=30)

        # This function for Generate Bill
        generatebill_button = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=RAISED, command=self.billing_section)
        generatebill_button.grid(row=1, column=5, ipadx=20)

        # This function for Clear Button
        clear_button = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=RAISED, command=self.clear)
        clear_button.grid(row=1, column=6, ipadx=20, padx=30)

        # This function for Exit Button
        exit_buttonn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7, relief=RAISED, command=self.exit)
        exit_buttonn.grid(row=1, column=7, ipadx=20)

        # This function for to get total prices

    def total_section(self):
        self.total_medicine_prices = (
        (self.medicol_advance.get() * 12) +
        (self.toseran_forte.get() * 12) +
        (self.imodium.get() * 15) +
        (self.mefenamic.get() * 38) +
        (self.amoxicillin.get() * 5)
        )
        self.total_medicine.set("Rs. " + str(self.total_medicine_prices))
        self.tax_medicine.set("Rs. " + str(round(self.total_medicine_prices * 0.05)))

        self.total_vitamins_prices = (
        (self.tiki_tiki_star.get() * 150) +
        (self.neutrilin_drops.get() * 250) +
        (self.profan_tlc.get() * 350) +
        (self.ceelin_plus.get() * 250) +
        (self.cheriper.get() * 400)

        )
        self.total_vitamins.set("Rs. " + str(self.total_vitamins_prices))
        self.tax_vitamins.set("Rs. " + str(round(self.total_vitamins_prices * 0.05)))

        self.total_cream_ointment_prices = (
        (self.lidocaine_ointment.get() * 340) +
        (self.canesten_cream.get() * 450) +
        (self.tabeta_ointment.get() * 420) +
        (self.nerisone_ointment.get() * 580) +
        (self.clotrimazole_cream.get() * 600)
        )
        self.total_cream_ointment.set("Rs. " + str(self.total_cream_ointment_prices))
        self.tax_cream_ointment.set("Rs. " + str(round(self.total_cream_ointment_prices * 0.05)))

    def welcome_customer(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "Welcome To Soubhagya Pharmacy Store\n")
        self.txt.insert(END, f"\nInvoice No. : {str(self.cus_invoice_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.customer_name.get())}")
        self.txt.insert(END, f"\nContact No. : {str(self.customer_contact_number.get())}")
        self.txt.insert(END, "\nProduct: Quantity: Price:")
        self.txt.insert(END, "\n___________________________________")

    # Function to clear the receipt area

    def clear(self):
        self.txt.delete('1.0', END)

    # This function for Add Product name , qty and price to bill section

    def billing_section(self):
        self.welcome_customer()
        if self.medicol_advance.get() != 0:
            self.txt.insert(END, f"\nMedicol Advance {self.medicol_advance.get()} {self.medicol_advance.get() * 12}")
        if self.toseran_forte.get() != 0:
            self.txt.insert(END, f"\nToseran Forte {self.toseran_forte.get()} {self.toseran_forte.get() * 12}")
        if self.imodium.get() != 0:
            self.txt.insert(END, f"\nImodium {self.imodium.get()} {self.imodium.get() * 15}")
        if self.mefenamic.get() != 0:
            self.txt.insert(END, f"\nMefenamic {self.mefenamic.get()} {self.mefenamic.get() * 38}")
        if self.amoxicillin.get() != 0:
            self.txt.insert(END,
        f"\nAmoxicillin {self.amoxicillin.get()} {self.amoxicillin.get() * 5}")
        if self.tiki_tiki_star.get() != 0:
            self.txt.insert(END, f"\nTiki Tiki Star {self.tiki_tiki_star.get()} {self.tiki_tiki_star.get() * 150}")
        if self.neutrilin_drops.get() != 0:
            self.txt.insert(END, f"\nNeutrilin Drops {self.neutrilin_drops.get()} {self.neutrilin_drops.get() * 250}")
        if self.profan_tlc.get() != 0:
            self.txt.insert(END, f"\nProfan Tlc {self.profan_tlc.get()} {self.profan_tlc.get() * 350}")
        if self.ceelin_plus.get() != 0:
            self.txt.insert(END, f"\nCeelin Plus {self.ceelin_plus.get()} {self.ceelin_plus.get() * 250}")
        if self.cheriper.get() != 0:
            self.txt.insert(END, f"\nCheriper {self.cheriper.get()} {self.cheriper.get() * 400}")
        if self.lidocaine_ointment.get() != 0:
            self.txt.insert(END, f"\nLicodaine Ointment {self.lidocaine_ointment.get()} {self.lidocaine_ointment.get() * 340}")
        if self.canesten_cream.get() != 0:
            self.txt.insert(END, f"\nCanesten Cream {self.canesten_cream.get()} {self.canesten_cream.get() * 450}")
        if self.tabeta_ointment.get() != 0:
            self.txt.insert(END, f"\nTabeta Ointment {self.tabeta_ointment.get()} {self.tabeta_ointment.get() * 420}")
        if self.nerisone_ointment.get() != 0:
            self.txt.insert(END, f"\nNerizone Ointment {self.nerisone_ointment.get()} {self.nerisone_ointment.get() * 580}")
        if self.clotrimazole_cream.get() != 0:
            self.txt.insert(END, f"\nClotrimazole Cream {self.clotrimazole_cream.get()} {self.clotrimazole_cream.get() * 20}")
        self.txt.insert(END, "\n___________________________________")
        self.txt.insert(END,
        f"\n Total : {self.total_medicine_prices + self.total_vitamins_prices + self.total_cream_ointment_prices + self.total_medicine_prices * 0.05 + self.total_vitamins_prices * 0.05 + self.total_cream_ointment_prices * 0.05}")

    # Function to exit

    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    object = Pharmacy_Billing(root)
    root.mainloop()
import tkinter as tk
from tkinter import Label, PhotoImage, messagebox
from tkinter import ttk


window = tk.Tk()  # create a window widget

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
# window.state("zoomed") 
window.geometry("1200x600")
  


page1 = tk.Frame(window)
page2 = tk.Frame(window)
page3 =tk.Frame(window)
page4=tk.Frame(window)
page5=tk.Frame(window)

for frame in (page1, page2, page3, page4,page5):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page1)

# ============= Page 1 =========
page1.config(background="#FFC948")
bg = PhotoImage(file = "page4.png")
  
# Show image using label
label1 = Label( page1, image = bg)
label1.place(x = 0,y = 0)

tombol =tk.Button(window, text = " START ", font=("MONOSPACE",15), activebackground="blue", command=lambda: show_frame(page2))
tombol.place(x=730, y=550)

teks = tk.Label(window, text = " Click Here ↓ ", font = ("Anton", 12, "bold"),fg= "black", bg="white")
teks.place(x=730, y=500)


# pg1_button = Button(page1, text='LOGIN', font=('Arial', 13, 'bold'),activebackground="blue", command=lambda: show_frame(page2))
# pg1_button.place(x=190, y=400)

# ======== Page 2 ===========
page2.config(background="white")
logo1= tk.PhotoImage(file="logo3.png")

pag2_label =tk.Label(page2, text='SIGN IN', font=('Arial', 30, 'bold'), bg = "white" , fg='black')
pag2_label.place(x=90, y=50)

pag3_label =tk.Label(page2, text='', font=('Arial', 30, 'bold'), bg = "white" , fg='black' ,image=logo1, compound="right")
pag3_label.place(x=400, y=50)
# pg2_button = Button(page2, text='Back < ', font=('Arial', 13, 'bold'), command=lambda: show_frame(page1))
# pg2_button.place(x=100, y=500)

# Fungsi untuk cek login

def cek_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "kelompok1" and password == "kuliner123":
        label_error.config(text="")
        page2.pack_forget()
        show_frame(page3)
    
             
    else:
        messagebox.showinfo("WARNING"," password anda salah")

    
# Membuat label dan entry untuk username
label_username = tk.Label(master=page2, text="Username", font=("Argent",15),fg='black', bg= "#FFC948")
label_username.place(x=100, y=140)

entry_username = tk.Entry(master=page2, bg="#7CFAFF")
entry_username.place(x=100, y=170)

# Membuat label dan entry untuk password
label_password = tk.Label(master=page2, text="Password",font=("Argent", 15), bg= "#FFC948")
label_password.place(x=100, y=210)

entry_password = tk.Entry(master=page2, bg= "#7CFAFF", show="*")
entry_password.place(x=100, y=240)

# Membuat button untuk login
button_login = tk.Button(master=page2, text=" Login ", font=("MONOSPACE",15), activebackground='blue', command= cek_login)
button_login.place(x=100, y=280)

# Membuat label untuk pesan error
label_error = tk.Label(master=page2)
label_error.place(x=100, y=280)

button_login = tk.Button(master=page2, text=" Back< ", font=("MONOSPACE",15), activebackground='blue', command=lambda: show_frame(page1))
button_login.place(x=100, y=600)

#=================Page 3================
bg2 = PhotoImage(file = "page5.png")
  
# Show image using label
label3 = Label( page3, image = bg2)
label3.place(x = 0,y = 0)
next_button = tk.Button(page3, text="ADMIN", command=lambda: show_frame(page4), font=(20), activebackground='blue')
next_button.place(x=1030, y=500)

next_button = tk.Button(page3, text="USER", command=lambda: show_frame(page5), font=(20), activebackground='blue')
next_button.place(x=300, y=500)


# ======== Page 4 ===========
page4.config(background="#ACF1F4")
bg1 = PhotoImage(file = "page.png")
  
# Show image using label
label2 = Label( page4, image = bg1)
label2.place(x = 0,y = 0)
# Data makanan tradisional dan harganya
makanan = {
    "Rendang": 35000,
    "Gudeg": 25000,
    "Sate Ayam": 15000,
    "Nasi Lemak": 20000,
    "Bakso": 10000
}

def bubble_sort():
    # Membuat daftar makanan dari dictionary
    daftar_makanan = list(makanan.items())

    # Melakukan Bubble Sort berdasarkan harga (nilai kedua pada tuple)
    n = len(daftar_makanan)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if daftar_makanan[j][1] > daftar_makanan[j + 1][1]:
                daftar_makanan[j], daftar_makanan[j + 1] = daftar_makanan[j + 1], daftar_makanan[j]

    # Menampilkan makanan dan harga setelah diurutkan
    sorted_treeview.delete(*sorted_treeview.get_children())
    for item in daftar_makanan:
        sorted_treeview.insert("", tk.END, values=item)

def tambah_makanan():
    nama = nama_entry.get()
    harga = harga_entry.get()
    makanan[nama] = int(harga)
    sorted_treeview.insert("", tk.END, values=(nama, harga))
    nama_entry.delete(0, tk.END)
    harga_entry.delete(0, tk.END)
    
    
def hapus_makanan():
    selection = sorted_treeview.selection()
    if selection:
        item = sorted_treeview.item(selection[0])
        makanan_name = item["values"][0]
        del makanan[makanan_name]
        sorted_treeview.delete(selection[0])


# Membuat tombol "Urutkan bubble sort"
urutkan_button = tk.Button(page4, text="Update", command=bubble_sort, font=(15), activebackground='blue')
urutkan_button.place(x=670, y=130)

# Membuat treeview untuk makanan yang diurutkan
sorted_treeview = ttk.Treeview(page4, columns=("name", "price"), show="headings")
sorted_treeview.heading("name", text="Nama Makanan")
sorted_treeview.heading("price", text="Harga")
sorted_treeview.place(x=500, y=170)

# Menampilkan data awal di treeview
for item in makanan.items():
    sorted_treeview.insert("", tk.END, values=item)

# Membuat frame untuk menambahkan makanan
tambah_frame = tk.Frame(page4)
tambah_frame.place(x=600, y=450)

nama_label = tk.Label(tambah_frame, text="Nama:",font=(15))
nama_label.grid(row=0, column=0)

nama_entry = tk.Entry(tambah_frame,bg="#B9C6C8")
nama_entry.grid(row=0, column=1)

harga_label = tk.Label(tambah_frame, text="Harga:", font=(15))
harga_label.grid(row=1, column=0)
harga_entry = tk.Entry(tambah_frame, bg="#B9C6C8")
harga_entry.grid(row=1, column=1)

tambah_button = tk.Button(tambah_frame, text="Tambah", command=tambah_makanan, font=(15), activebackground='blue')
tambah_button.grid(row=2, columnspan=2)

# Membuat tombol "Hapus"
hapus_button = tk.Button(page4, text="Hapus", command=hapus_makanan, font=(15), activebackground='blue')
hapus_button.place(x=660, y=540)

next_button = tk.Button(page4, text="back<", command=lambda: show_frame(page3), font=(15), activebackground='blue')
next_button.place(x=100, y=600)

next_button = tk.Button(page4, text="keluar<", command=lambda: show_frame(page2), font=(15), activebackground='blue')
next_button.place(x=1150, y=600)



#==================Page 5====================================
page5.config(background="#ACF1F4")
bg4 = PhotoImage(file = "page.png")
  
# Show image using label
label4 = Label( page5, image = bg4)
label4.place(x = 0,y = 0)
# Data makanan tradisional dan harganya
makanan= {
    "Rendang": 35000,
    "Gudeg": 25000,
    "Sate Ayam": 15000,
    "Nasi Lemak": 20000,
    "Bakso": 10000
}

def bubble_sort():
    # Membuat daftar makanan dari dictionary
    daftar_makanan = list(makanan.items())

    # Melakukan Bubble Sort berdasarkan harga (nilai kedua pada tuple)
    n = len(daftar_makanan)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if daftar_makanan[j][1] > daftar_makanan[j + 1][1]:
                daftar_makanan[j], daftar_makanan[j + 1] = daftar_makanan[j + 1], daftar_makanan[j]

    # Menampilkan makanan dan harga setelah diurutkan
    sorted_treeview1.delete(*sorted_treeview1.get_children())
    for item in daftar_makanan:
        sorted_treeview1.insert("", tk.END, values=item)

    # Membuat tombol "Urutkan bubble sort"
urutkan_button = tk.Button(page5, text="Update", command=bubble_sort, font=(15), activebackground='blue')
urutkan_button.place(x=670, y=130)

# Membuat treeview untuk makanan yang diurutkan
sorted_treeview1 = ttk.Treeview(page5, columns=("name", "price"), show="headings")
sorted_treeview1.heading("name", text="Nama Makanan")
sorted_treeview1.heading("price", text="Harga")
sorted_treeview1.place(x=500, y=170)

# Menampilkan data awal di treeview
for item in makanan.items():
    sorted_treeview1.insert("", tk.END, values=item)

m_button = tk.Button(page5, text="back", command=lambda: show_frame(page3), font=(15), activebackground='blue')
m_button.place(x=100, y=600)

m_button = tk.Button(page5, text="keluar", command=lambda: show_frame(page1), font=(15), activebackground='blue')
m_button.place(x=1150, y=600)

# Menjalankan aplikasi
window.mainloop()

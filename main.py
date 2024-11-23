import time

import bcrypt
import customtkinter as ctk
from PIL import Image


def user_save_data(username, password):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with open("user_data.txt", "a") as file:
        file.write(f"{username}:{hashed_pw.decode()}\n")
    print("Data berhasil disimpan.")


def shake_widget(widget):
    """Efek getar untuk widget tertentu"""
    x, y = widget.winfo_x(), widget.winfo_y()
    for _ in range(3):  # Getar sebanyak 3 kali
        widget.place(x=x + 5, y=y)
        widget.update()
        time.sleep(0.05)
        widget.place(x=x - 5, y=y)
        widget.update()
        time.sleep(0.05)
    widget.place(x=x, y=y)  # Kembalikan ke posisi awal


def register_user():
    username = entry_usn.get()
    password = entry_pw.get()
    is_checked = ckbox.get()  # Ambil status checkbox (1 jika dicentang, 0 jika tidak)

    if not is_checked:  # Jika checkbox belum dicentang
        status_label.configure(
            text="""Tolong setujui kebijakan 
privasi!"""
        )
        shake_widget(ckbox)  # Efek getar pada checkbox
        return

    if username and password:  # Jika semua kolom diisi
        user_save_data(username, password)
        status_label.configure(text="Data berhasil disimpan!")
    else:
        status_label.configure(text="Silakan isi semua kolom.")


# Konfigurasi awal
app = ctk.CTk()
app.title("User Login")
app.geometry(
    f"{500}x{500}+{app.winfo_screenwidth() // 2 - 500 // 2}+{app.winfo_screenheight() // 2 - 500 // 2}"
)
app.resizable(0, 0)
ctk.set_default_color_theme("MoonlitSky.json")

# Load Images
user_icon = ctk.CTkImage(Image.open("img/user.png"), size=(15, 15))
padlock_icon = ctk.CTkImage(Image.open("img/padlock.png"), size=(15, 15))

# Tambahkan logo aplikasi
app_logo = ctk.CTkImage(Image.open("img/logo.png"), size=(100, 100))

# Tampilkan logo di aplikasi
logo_label = ctk.CTkLabel(app, image=app_logo, text="")
logo_label.place(x=200, y=20)  # Sesuaikan posisi logo

# Label Username dengan Icon
user_icon_label = ctk.CTkLabel(app, image=user_icon, text="")
user_icon_label.place(x=150, y=120)

label_usn = ctk.CTkLabel(app, text="Username")
label_usn.place(x=181, y=120)

# Entry Username
entry_usn = ctk.CTkEntry(app, fg_color="transparent")
entry_usn.place(x=181, y=150)

# Label Password dengan Icon
padlock_icon_label = ctk.CTkLabel(app, image=padlock_icon, text="")
padlock_icon_label.place(x=150, y=190)

label_pw = ctk.CTkLabel(app, text="Password")
label_pw.place(x=181, y=190)

# Entry Password
entry_pw = ctk.CTkEntry(app, fg_color="transparent", show="*")
entry_pw.place(x=181, y=220)

# Tombol Login
button1 = ctk.CTkButton(
    app, text="Login", width=180, height=34, corner_radius=12, command=register_user
)
button1.place(x=164, y=300)

# Checkbox
ckbox = ctk.CTkCheckBox(
    app, text="I agree to the privacy policy and terms of use", font=("Arial", 10)
)
ckbox.place(x=130, y=350)

# Label Status
status_label = ctk.CTkLabel(app, text="")
status_label.place(x=181, y=260)

app.mainloop()

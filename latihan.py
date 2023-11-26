import tkinter as tk
import sqlite3
from tkinter import messagebox

#perhitungan
'''Membuat fungsi untuk perbandingan'''

def hitung(bio,ing,fiks):
    if bio > ing and bio > fiks:
      return "kedokteran"
    elif ing > fiks and ing > bio:
         return "Bahasa"
    elif fiks > bio and fiks > ing:
         return "Teknik"
    else:
         return "Tidak memprediksi"

# menyimpan data
'''membuat definisi untuk menyimpan data kedalam database'''

def simpan_data(nama,nil_bio,nil_ing,nil_fiks, prediksi_fk):

    # Membuka atau membuat database SQLite
    '''mengkoneksikan ke database'''

    conn = sqlite3.connect("DBPelajar.db")
    cursor = conn.cursor()

    # Membuat tabel 
    '''perintah untuk membuat tabel baru di database'''

    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nama INTEGER,
                nil_bio INTEGER, 
                nil_ing INTEGER,
                nil_fiks INTEGER,
                prediksi_fk TEXT)''')


    # Memasukkan data mata pelajaran ke dalam tabel
    '''perintah untuk memasukan nilai kedalam tabel database'''

    cursor.execute('''INSERT INTO hasil_prediksi (nama,nil_bio,nil_ing,nil_fiks, prediksi_fk) VALUES (?,?,?,?,?)''',
    (nama,nil_bio,nil_ing,nil_fiks, prediksi_fk))
    # Melakukan commit dan menutup koneksi
    '''perintah untuk commit setelah memasukan data'''

    conn.commit()
    conn.close()

#menampilkan ulang hasil
'''membuat definisi show untuk menampilkan kembali data setelah menekan submit, data yang di masukan akan di perbandingkan dengan dengan fungsi yang telah dibuat'''

def show():
    nama = e1.get()
    nil_bio = e2.get()
    nil_ing = e3.get()
    nil_fiks = e4.get()

    prediksi = hitung(nil_bio, nil_ing, nil_fiks)

    hasilnama = f"Nama Mahasiswa: {nama}"
    hasilbio = f"Nilai Biologi: {nil_bio}"
    hasiling = f"Nilai B.Inggris: {nil_ing}"
    hasilfiks = f"Nilai Fisika: {nil_fiks}"
    prediksi = f"Hasil Prediksi: {prediksi}"


    label_hasilnama.config(text=hasilnama)
    label_hasilbio.config(text=hasilbio)
    label_hasiling.config(text=hasiling)
    label_hasilfiks.config(text=hasilfiks)
    labe_prediksi.config(text=prediksi)

    frame_hasil.pack()
    simpan_data(nama, nil_bio, nil_fiks, nil_ing, prediksi)
    messagebox.showinfo("info", f"Data Tersimpan")

    
# box input
'''membuat bemntuk frame untuk input data'''

top = tk.Tk()
top.title("Prediksi Prodi Mahasiswa")
top.geometry("400x600")
top.resizable(False, False)

inputframe=tk.LabelFrame(top)
inputframe.pack(padx=10, pady=10, fill="x", expand=True)

#Bikin Label Untuk Judul
'''membuat title di judul frame'''
var = tk.Label(inputframe, text="Aplikasi Prediksi Prodi Pilihan")
var.pack()

#Bikin Input nama
'''membuat text box untuk memasukan nama'''

Input=tk.Label(inputframe, text="Masukan Nama: " )
Input.pack(padx=10, pady=5,fill="x", expand=True)
e1=tk.Entry(inputframe)
e1.pack(padx=10, pady=5,fill="x", expand=True)

#Bikin Input Biologi
'''membuat text box untuk memasukan nilai biologi'''

Input2=tk.Label(inputframe, text="Masukan Nilai Biologi: " )
Input2.pack(padx=10, pady=5,fill="x", expand=True)
e2=tk.Entry(inputframe)
e2.pack(padx=10, pady=5,fill="x", expand=True)

#Bikin Input Inggris
'''membuat text box untuk memasukan nilai b. inggris'''

Input3=tk.Label(inputframe, text="Masukan Nilai B.Inggris: " )
Input3.pack(padx=10, pady=5,fill="x", expand=True)
e3=tk.Entry(inputframe)
e3.pack(padx=10, pady=5,fill="x", expand=True)

#Bikin Input Fisika
'''membuat text box untuk memasukan nilai fisika'''

Input4=tk.Label(inputframe, text="Masukan Nilai Fisika: " )
Input4.pack(padx=10, pady=5,fill="x", expand=True)
e4=tk.Entry(inputframe)
e4.pack(padx=10, pady=5,fill="x", expand=True)


#tombol hasil
'''membuat tombol untuk submit'''

tombol=tk.Button(inputframe, text="Submit", command=show)
tombol.pack(padx=10, pady=5,fill="x", expand=True)

frame_hasil = tk.LabelFrame(inputframe, labelanchor="n")
frame_hasil.pack_forget()

#label hasil
'''membuat label yang akan ditampilkan setelah data dimasukan kedalam database'''

label_hasilnama = tk.Label(frame_hasil,text="")
label_hasilnama.pack(pady=5,fill= "x")

label_hasilbio = tk.Label(frame_hasil,text="")
label_hasilbio.pack(pady=5)

label_hasiling = tk.Label(frame_hasil,text="")
label_hasiling.pack(pady=5)

label_hasilfiks = tk.Label(frame_hasil,text="")
label_hasilfiks.pack(pady=5)

labe_prediksi = tk.Label(frame_hasil,text="")
labe_prediksi.pack()

#menjalankan app
'''perintah untuk  menjalankan aplikasi yang telah di rancang'''

top.mainloop()
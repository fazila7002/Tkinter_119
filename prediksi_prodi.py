# Tugas Praktikum Pemrograman Multiplatform - Formatting GUI dengan Tkinter
# Nama  : Fazilatun Nisa Muslimah
# NIM   : 20250140119
# Kelas : C

import tkinter as tk

# Daftar 10 mata pelajaran yang nilainya diinput
MATA_PELAJARAN = [
    "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
    "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika",
]

WARNA_BG = "#F4F6FB"
WARNA_HEADER = "#1F3A93"
WARNA_HASIL = "#0B7A3E"


def hasil_prediksi():
    # Apapun nilai yang diinput, hasil prediksinya selalu Teknologi Informasi
    hasil_var.set("Prodi pilihan kamu: Teknologi Informasi")


root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.configure(bg=WARNA_BG, padx=20, pady=20)
root.resizable(False, False)

# 1 label judul
judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan",
                 font=("Segoe UI", 18, "bold"), fg="white", bg=WARNA_HEADER,
                 padx=20, pady=10)
judul.grid(row=0, column=0, sticky="ew", pady=(0, 15))

# Frame berlabel berisi 10 input nilai (2 kolom x 5 baris)
frame_nilai = tk.LabelFrame(root, text=" Masukkan Nilai Mata Pelajaran ",
                            font=("Segoe UI", 10, "bold"), bg=WARNA_BG,
                            padx=15, pady=10)
frame_nilai.grid(row=1, column=0, sticky="ew")

entries = []
for i, mapel in enumerate(MATA_PELAJARAN):
    baris = i % 5
    kolom = (i // 5) * 2  # kolom 0-1 untuk 5 mapel pertama, kolom 2-3 untuk sisanya

    label = tk.Label(frame_nilai, text=mapel, font=("Segoe UI", 10),
                     bg=WARNA_BG, anchor="w", width=16)
    label.grid(row=baris, column=kolom, sticky="w", padx=(10, 5), pady=5)

    entry = tk.Entry(frame_nilai, width=10, bd=2, justify="center",
                     font=("Segoe UI", 10))
    entry.grid(row=baris, column=kolom + 1, padx=(0, 15), pady=5)
    entries.append(entry)

# 1 button Hasil Prediksi
tombol = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi,
                   font=("Segoe UI", 11, "bold"), bg=WARNA_HEADER, fg="white",
                   activebackground="#2C4FBF", activeforeground="white",
                   padx=20, pady=5, cursor="hand2")
tombol.grid(row=2, column=0, pady=15)

# 1 label luaran hasil prediksi
hasil_var = tk.StringVar(value="Hasil prediksi akan tampil di sini")
hasil = tk.Label(root, textvariable=hasil_var, font=("Segoe UI", 12, "bold"),
                 fg=WARNA_HASIL, bg="white", relief=tk.GROOVE, padx=10, pady=10)
hasil.grid(row=3, column=0, sticky="ew")

root.mainloop()

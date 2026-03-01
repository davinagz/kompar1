# Parallel Computing – Matrix Example

Di project ini saya mencoba mengimplementasikan 4 jenis arsitektur 
parallel computing berdasarkan Flynn’s Taxonomy, yaitu:
1. SISD
2. SIMD
3. MISD
4. MIMD

Contoh yang digunakan berbasis operasi matrix supaya lebih mudah dipahami.

1. SISD (Single Instruction Single Data)
Pada bagian ini matrix ditambahkan secara serial (satu per satu).
Program berjalan menggunakan satu processor saja.
Konsepnya sederhana:
Loop baris dan kolom, lalu jumlahkan setiap elemen.
File: sisd_serial.py

2. SIMD (Single Instruction Multiple Data)
Pada bagian ini penjumlahan matrix dilakukan secara paralel.
Baris matrix dibagi dan diproses oleh beberapa core secara bersamaan.
Instruksi yang dijalankan tetap sama (penjumlahan),
tetapi datanya berbeda-beda.
File: simd_parallel.py


3. MISD (Multiple Instruction Single Data)
Pada bagian ini satu data (matrix yang sama)
diproses oleh beberapa algoritma yang berbeda.
Hasilnya kemudian dibandingkan menggunakan sistem voting.
Tujuannya bukan untuk mempercepat,
tetapi untuk memastikan hasilnya benar.
File: misd_voting.py


4. MIMD (Multiple Instruction Multiple Data)
Pada bagian ini beberapa task berbeda dijalankan secara paralel,
seperti:
- Menghitung total
- Mencari nilai maksimum
- Menghitung angka genap
- Melakukan transpose matrix
Setiap task memiliki instruksi berbeda dan berjalan bersamaan.
File: mimd_tasks.py

5. Comparison (Serial vs Parallel)
File: comparison.py
File ini digunakan untuk membandingkan waktu eksekusi 
antara serial dan parallel matrix addition.
Dari hasil pengujian terlihat bahwa untuk ukuran matrix besar,
parallel memiliki performa yang lebih baik.

Kesimpulan:
Dari percobaan ini terlihat bahwa:
- Serial lebih sederhana tapi lebih lambat untuk data besar.
- Parallel lebih cepat jika ukuran matrix besar.
- MISD lebih fokus ke keandalan daripada kecepatan.
- MIMD paling fleksibel dan umum digunakan.
Semakin besar ukuran matrix, semakin terasa perbedaan waktu eksekusinya.
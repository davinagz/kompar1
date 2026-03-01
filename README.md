# Parallel Computing – Matrix Example

Project ini mengimplementasikan 4 jenis arsitektur parallel computing berdasarkan Flynn’s Taxonomy:

1. SISD – Matrix dijumlahkan secara serial (satu per satu).
   File: sisd_serial.py

2. SIMD – Penjumlahan matrix dilakukan secara paralel dengan membagi baris ke beberapa core.
   File: simd_parallel.py

3. MISD – Matrix yang sama diproses dengan beberapa algoritma berbeda lalu dibandingkan (voting).
   File: misd_voting.py

4. MIMD – Beberapa task berbeda dijalankan secara paralel (sum, max, count even, transpose).
   File: mimd_tasks.py

5. Comparison – Membandingkan waktu eksekusi serial dan parallel.
   File: comparison.py

Kesimpulan:
Serial lebih sederhana, tetapi untuk matrix besar parallel lebih efisien.
MISD fokus pada keandalan, sedangkan MIMD lebih fleksibel.

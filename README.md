Nama : Nathanael Orrick Hatmoko

NPM : 2506592125

Kelas : PBP D

alasan penggunaan AI dalam pengerjaan website portofolio:
Saya menggunakan AI dalam pengerjaan website portofolio sebagai alat bantu, bukan sebagai pengganti proses berpikir dan pengambilan keputusan. AI membantu saya mencari penyebab masalah teknis, seperti CSS yang tidak terhubung, gambar yang tidak muncul, tata letak yang terlalu renggang, serta tampilan yang belum responsif. Selain itu, AI membantu memberikan alternatif struktur HTML, ide desain navigasi, dan penjelasan mengenai konsep CSS seperti flexbox, media query, position: fixed, serta clamp(). Penggunaan AI dalam pengerjaan HTML & CSS membantu saya untuk membentuk struktur coding yang lebih rapih dan readable. Di luar teknis, penggunaan AI mempermudah saya dalam merealisasikan desain web yang telah saya rancang sebelumnya di Figma, sehingga tampilan web menjadi lebih rapih dan sesuai dengan harapan.


### Menjawab pertanyaan refleksi Tugas 1:
1. Dalam merancang struktur HTML, saya menggunakan beberapa elemen semantik HTML5, seperti `<header>`, `<nav>`, `<section>`, dan `<footer>`. Saya belum menggunakan elemen `<article>` atau `<aside>` karena isi portofolio saya tidak terdiri atas beberapa artikel terpisah atau informasi sampingan. Elemen `<header>` digunakan untuk bagian navigasi, sedangkan `<section>` digunakan untuk mengelompokkan bagian utama seperti hero, profil, minat, dan pendidikan. Elemen `<footer>` digunakan untuk menampilkan informasi kontak dan alamat. Penggunaan elemen semantik membuat struktur halaman lebih mudah dipahami, baik oleh pengembang maupun oleh browser dan teknologi pembaca layar. Selain itu, pembagian struktur tersebut membantu saya mengatur CSS dan mengembangkan halaman secara lebih terarah.

2. Tantangan utama saat membuat tampilan responsif adalah menyesuaikan susunan elemen dari tampilan desktop ke tampilan tablet dan ponsel. Pada desktop, teks perkenalan dan foto dapat ditempatkan berdampingan. Namun, pada layar yang lebih kecil, keduanya perlu disusun secara vertikal agar tetap nyaman dibaca. Saya juga perlu menyesuaikan ukuran judul, jarak antarbagian, ukuran foto, serta navigasi agar tidak saling bertumpuk. Untuk mengevaluasinya, saya menguji halaman pada beberapa ukuran layar menggunakan mode responsif di browser. Saya memeriksa apakah teks tetap terbaca, gambar tidak terpotong, tombol dapat ditekan dengan mudah, dan navigasi tetap dapat digunakan. Berdasarkan hasil pengujian tersebut, saya menggunakan media query pada ukuran layar tertentu untuk mengubah arah tata letak dan mengecilkan jarak yang terlalu lebar.

3. Karena portofolio ini masih berfokus pada penyajian informasi statis, sebagian besar isi halaman harus ditulis langsung di dalam HTML. Hal ini membatasi kemampuan saya untuk memperbarui data secara otomatis, menyimpan masukan dari pengunjung, dan mengelola proyek dalam jumlah banyak. Fitur pencarian yang tersedia juga masih berupa tampilan dan belum benar-benar mencari isi portofolio. Pada pengembangan berikutnya, saya ingin menambahkan halaman proyek yang datanya diambil dari basis data, fitur pencarian yang berfungsi, serta formulir kontak yang dapat mengirim dan menyimpan pesan. Dengan begitu, portofolio tidak hanya menampilkan informasi, tetapi juga dapat berinteraksi dengan pengunjung dan lebih mudah diperbarui.

-------------------------------------------------------------------------------------------------------------

### Pengerjaan tugas 2 individu:
Alasan penggunaan AI dalam pengerjaan tugas 2 individu
Saya menggunakan AI sebagai alat bantu belajar dalam mengerjakan Tugas 2 individu untuk memahami konsep Django, seperti model, view, URL routing, template, dan migrasi database. AI membantu saya menjelaskan materi yang belum saya pahami, memberikan contoh penerapan, serta membantu menemukan dan memperbaiki kesalahan dalam kode. Namun, saya tetap mengerjakan dan memahami proses implementasi secara mandiri, serta memeriksa kembali setiap saran AI agar sesuai dengan kebutuhan tugas. Dengan demikian, AI digunakan sebagai pendamping pembelajaran, bukan sebagai pengganti usaha dan pemahaman saya sendiri.

1. Alur ketika pengguna membuka halaman portofolio baru

   Ketika pengguna membuka halaman portofolio baru, permintaan dari browser pertama kali diterima oleh `urls.py` proyek. File ini mengarahkan permintaan ke `urls.py` aplikasi yang sesuai. Selanjutnya, `urls.py` aplikasi menghubungkan URL tersebut dengan fungsi `view`.

   View bertugas mengambil data portofolio dari `model` melalui database. Setelah data diperoleh, view mengirimkannya ke `template` untuk ditampilkan dalam bentuk halaman HTML. Hasil akhirnya dikirim kembali ke browser sehingga pengguna dapat melihat portofolio baru.

   Secara sederhana, alurnya adalah:

   **Browser → urls.py proyek → urls.py aplikasi → View → Model/Database → Template → Browser**

2. Mengapa data sebaiknya disimpan pada model?

   Data portofolio sebaiknya disimpan pada model karena model mengatur struktur dan penyimpanan data dalam database. Template cukup bertugas menampilkan data yang diberikan oleh view.

   Jika data ditulis langsung di template, setiap perubahan harus dilakukan secara manual pada kode HTML. Hal ini membuat pemeliharaan lebih sulit dan berisiko menimbulkan kesalahan.

   Dengan menggunakan model, data dapat diperbarui melalui database tanpa harus mengubah template. Cara ini membuat aplikasi lebih rapi, mudah dirawat, dan lebih mudah dikembangkan ketika jumlah data portofolio bertambah.

3. Perbedaan `makemigrations` dan `migrate`

   `makemigrations` digunakan untuk membuat file migrasi berdasarkan perubahan pada model. File ini berisi catatan mengenai perubahan struktur database yang perlu dilakukan.

   `migrate` digunakan untuk menerapkan file migrasi tersebut ke database sehingga struktur database sesuai dengan model terbaru.

   Contohnya, ketika menambahkan field `description` pada model `Portfolio`, kita menjalankan:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

   Perintah pertama membuat catatan perubahan, sedangkan perintah kedua menerapkan perubahan tersebut ke database.

   ----------------------------------------------------------------
### Tugas 3
Alasan penggunaan AI dalam pengerjaan tugas individu 3:
Proses pengerjaan tugas individu 3 menyerupai tutorial 3, sehingga pengunaan AI dalam tugas ini tidak begitu signifikan. Saya menggunakan AI sebagai alat bantu dalam renaming classes pada html yang berulang, serta memilihkan class dengan css yang ingin saya gunakan, sehingga desain User Interface dapat dipakai dengan efisien. 

1. **Kenapa pakai `ModelForm`, dan kenapa perlu `{% csrf_token %}`?**

   `ModelForm` membuat form langsung dari model. Di proyek ini, `ExperienceForm` otomatis tahu bahwa ada field `title`, `description`, `category`, `started_at`, dan seterusnya, lengkap dengan tipe datanya. Kalau membuat form HTML manual, semua field itu harus ditulis satu per satu, dan validasinya (misalnya kategori harus salah satu dari pilihan yang ada, atau thumbnail harus berupa URL yang valid) harus dibuat sendiri. Dengan `ModelForm`, validasi sudah ikut terbawa dari model, dan datanya bisa langsung disimpan dengan `form.save()`. Kodenya jadi lebih singkat, lebih rapi, dan kecil kemungkinan ada field yang terlewat atau tidak sinkron dengan model.

   `{% csrf_token %}` wajib ada untuk melindungi dari serangan CSRF (Cross-Site Request Forgery). Bayangkan kamu sedang login di websiteku, lalu membuka website jahat di tab lain. Website jahat itu bisa diam-diam mengirim request POST ke websiteku atas nama kamu, misalnya untuk menghapus data, karena browser otomatis menyertakan cookie login. Django menangkal ini dengan memberi setiap form token rahasia yang unik. Saat form dikirim, Django mengecek token tersebut. Website jahat tidak punya token itu, jadi request-nya ditolak dengan error 403.

2. **Kenapa JSON lebih disukai daripada XML?**

   JSON lebih ringkas dan lebih mudah dibaca. XML harus membuka dan menutup tag untuk setiap data, sedangkan JSON cukup pakai pasangan `key: value`, sehingga ukuran datanya lebih kecil dan transfernya lebih cepat. JSON juga terlihat seperti object di JavaScript, sehingga bisa langsung diubah jadi object dengan `JSON.parse()`. Di Python, hasilnya langsung menjadi dictionary dan list. Selain itu, hampir semua API modern dan framework frontend memakai JSON, jadi tools dan dokumentasinya lengkap. XML masih dipakai di beberapa kasus tertentu, tapi untuk pengembangan web sehari-hari JSON jauh lebih praktis.

3. **Alur view yang mengembalikan data portofolio dalam bentuk JSON, dan kenapa perlu serialization?**

   Alurnya seperti ini:
   1. Browser atau client mengakses URL `/api/experience/`.
   2. `urls.py` meneruskan request itu ke view `get_experience_json`.
   3. View mengambil data dari database lewat `Experience.objects.all()`. Kalau ada pencarian, hasilnya difilter berdasarkan judul.
   4. Data tersebut diubah menjadi teks JSON dengan `serializers.serialize("json", experience)`.
   5. Teks JSON dikirim lewat `HttpResponse` dengan `content_type="application/json"`, supaya penerimanya tahu bahwa isinya JSON.

   Serialization dibutuhkan karena data dari database masih berupa object Python (QuerySet berisi object model), sedangkan HTTP hanya bisa mengirim teks atau bytes. Object Python tidak bisa dikirim begitu saja lewat jaringan dan tidak dimengerti oleh client, apalagi kalau client-nya bukan Python. Serialization mengubah object itu menjadi format standar (JSON) yang bisa dikirim dan dibaca oleh siapa pun. Proses ini juga menangani tipe data yang tidak ada di JSON, seperti UUID dan tanggal, dengan mengubahnya menjadi teks.

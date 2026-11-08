# MyPortofolio

## Instalasi dan Menjalankan Proyek

Ikuti langkah berikut untuk menjalankan proyek MyPortofolio secara lokal.

### Prasyarat
- Git
- Python yang sesuai dengan versi Django pada proyek
- `pip`

### 1. Clone repository
```bash
git clone https://github.com/Vindicatree/myportofolio.git
cd myportofolio
```

### 2. Buat dan aktifkan virtual environment

**macOS/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (Command Prompt)**
```bat
py -m venv .venv
.venv\\Scripts\\activate
```

### 3. Install dependencies

Jika repository menyediakan `requirements.txt`, install dependency dari file tersebut:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Jika `requirements.txt` tidak tersedia, install Django dan Django REST Framework sesuai versi yang digunakan proyek. Hindari memasang versi terbaru secara sembarang apabila proyek memiliki batasan versi.

### 4. Jalankan migrasi database
```bash
python manage.py migrate
```

### 5. (Opsional) Buat akun administrator
```bash
python manage.py createsuperuser
```

Ikuti prompt untuk mengisi username, email (jika diminta), dan password.

### 6. Jalankan development server
```bash
python manage.py runserver
```

Buka http://127.0.0.1:8000/ di browser. Untuk menghentikan server, tekan `Ctrl+C` di terminal.

> Catatan: `runserver` ditujukan untuk development lokal, bukan deployment production. Dokumentasi instalasi Django menyarankan penggunaan virtual environment dan pemasangan package melalui pip.

---

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


### Tugas 4 - AI Disclosure
Pengerjaan tugas 4 saya menggunakan bantuan AI untuk memandu penambahan group editor dan penambahan user untuk group editor. Dengan menggunakan AI, prosedur pengerjaan saya menjadi lebih terstruktur dan jelas sehingga memperoleh hasil kode yang human readable. Selain itu, AI membantu saya dalam css untuk memperoleh UX yang lebih professional dan seamless.

### Tugas 5
## AI DISCLOSURE 
Pengerjaan tugas 5 saya menggunakan bantuan AI untuk memandu perbaikan script pada achievements.html sehingga mampu mempergunakan function pada views dengan baik tanpa error yang mengganggu kinerja web. Selain itu, penggunaan AI membantu memperjelas definisi yang saya sampaikan sebagai jawaban dari pertanyaan tugas 5 yang diberikan.

1. **Debouncing** adalah teknik menunda eksekusi sebuah fungsi sampai pengguna berhenti memicu event dalam jeda waktu tertentu:, dimana setiap event baru membatalkan timer sebelumnya dan memulai hitungan dari awal. Di proyek ini, event `input` pada kolom pencarian Experience memakai `setTimeout` 300 ms yang dibatalkan dengan `clearTimeout`, sehingga `fetchExperiences()` hanya dipanggil sekali setelah pengguna selesai mengetik (mengetik "dosen" menghasilkan satu request, bukan lima). Teknik ini penting pada pencarian AJAX karena tanpa debouncing setiap ketukan tombol mengirim request ke server dan memicu query ke database. Akibatnya bandwidth dan sumber daya server terbuang, tampilan berkedip karena terus berganti ke kondisi *loading*, dan hasil bisa salah ketika respons lama tiba setelah respons yang lebih baru (*race condition*). Sebagai lapisan tambahan, request sebelumnya juga dibatalkan dengan `AbortController`.

2. `await` membuat fungsi `async` berhenti sementara sampai Promise yang dikembalikan `fetch()` selesai, lalu memberikan nilai hasilnya (objek `Response`). Dengan begitu `response.ok` dan `await response.json()` baru dijalankan ketika data benar-benar sudah tersedia, tanpa callback `.then()` bersarang. Tanpa `await`, `fetch()` langsung mengembalikan Promise yang masih *pending*. Pada kode ini `response.ok` bernilai `undefined`, sehingga kondisi `!response.ok` selalu benar dan halaman selalu menampilkan kondisi error walaupun server membalas 200. Kalau `await` pada `response.json()` yang dihilangkan, `experienceData` berupa Promise, `.length` bernilai `undefined`, dan `.forEach` menimbulkan `TypeError`. Selain itu, kegagalan jaringan tidak tertangkap oleh `try/catch` karena Promise ditolak setelah blok `try` selesai, sehingga menjadi *unhandled promise rejection*.

3. **XSS (Cross-Site Scripting)** adalah serangan ketika penyerang menyisipkan kode JavaScript ke halaman web yang kemudian dijalankan di browser pengguna lain. Pada *stored XSS*, kode tersebut disimpan di database (misalnya sebagai judul experience) lalu ikut dieksekusi setiap data itu ditampilkan. Template Django melakukan *auto-escaping* pada `{{ variabel }}`, sehingga karakter seperti `<` diubah menjadi `&lt;` dan tampil sebagai teks biasa. Pada AJAX, data JSON dirakit oleh JavaScript menjadi string HTML lalu dipasang lewat `innerHTML`. Tidak ada lagi Django yang melakukan *escaping*, sehingga browser mem-parsing tag dan atribut di dalam data (misalnya `<img src="x" onerror="...">`) sebagai HTML sungguhan dan menjalankan *event handler*-nya. Karena itu setiap nilai teks dari JSON harus dibungkus `escapeHtml()` (atau dipasang lewat `textContent`), dan input dibersihkan di sisi server dengan `strip_tags` pada `clean_<field>` di `ModelForm`. Dampaknya juga lebih serius karena kode yang disisipkan dapat membaca cookie `csrftoken` dan mengirim request `POST` atas nama korban, sehingga perlindungan CSRF tidak lagi efektif.

### Tugas 6 — Pertanyaan Reflektif

1. **Apa itu REST, mengapa JSON saja belum cukup untuk menyebut API RESTful, dan apa perbedaan PUT dengan PATCH?**

   REST (*Representational State Transfer*) adalah gaya arsitektur untuk sistem berbasis jaringan. REST tidak ditentukan oleh format data yang dikirim saja, melainkan oleh sejumlah batasan arsitektur, seperti pemisahan client dan server, komunikasi stateless, penggunaan cache, uniform interface, serta layered system. Dalam uniform interface, resource diidentifikasi melalui URI dan dimanipulasi melalui representasinya; pesan juga perlu bersifat self-descriptive dan mendukung hypermedia sebagai bagian dari navigasi aplikasi.

   Karena itu, API yang hanya mengembalikan JSON belum otomatis RESTful. JSON adalah format representasi data, sedangkan REST mengatur cara komponen berinteraksi. API perlu dirancang mengikuti batasan REST, bukan sekadar mengubah respons menjadi JSON.

   `PUT` digunakan ketika client mengirim representasi untuk mengganti keadaan resource secara keseluruhan. Contohnya, ketika ingin memperbarui seluruh data sebuah achievement, client mengirim semua field yang diperlukan. Sementara itu, `PATCH` digunakan untuk menerapkan perubahan sebagian pada resource. Contohnya, ketika hanya ingin mengubah `issuer` tanpa mengirim ulang `title`, `description`, atau field lainnya. Dalam implementasi ini, `PATCH` lebih tepat untuk perubahan satu atau beberapa field, sedangkan `PUT` untuk penggantian representasi secara lengkap. (Rujukan: [Fielding, REST Architectural Style](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm), [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), [RFC 5789](https://www.rfc-editor.org/rfc/rfc5789.html).)

2. **Apa peran serializer di Django REST Framework, dan apa keuntungannya dibandingkan membuat dictionary manual dengan `JsonResponse`?**

   Serializer menjadi perantara antara object model Django dengan format data yang dapat dikirim melalui API. Serializer dapat mengubah QuerySet atau instance model menjadi tipe data Python yang kemudian dirender sebagai JSON. Serializer juga melakukan proses sebaliknya: menerima data dari request, mengubahnya menjadi data yang sesuai dengan model, dan memvalidasi data sebelum disimpan.

   Pada proyek ini, `AchievementsSerializer` menggunakan `ModelSerializer`. Dengan pendekatan tersebut, field yang berasal dari model dapat didefinisikan secara terstruktur, sementara validasi khusus—misalnya membersihkan tag HTML pada field teks—dapat ditambahkan melalui method `validate_<field>`. Serializer juga menyediakan mekanisme `is_valid()` dan `save()`.

   Jika menggunakan dictionary manual dengan `JsonResponse`, developer harus menyusun field respons satu per satu dan membuat validasi input secara terpisah. Cara itu masih bisa digunakan untuk respons sederhana, tetapi akan lebih mudah terjadi pengulangan kode atau ketidaksesuaian antara model dan API. Serializer membuat proses representasi dan validasi lebih konsisten serta lebih mudah dirawat. (Rujukan: [DRF — Serializers](https://www.django-rest-framework.org/api-guide/serializers/).)

3. **Apa perbedaan autentikasi dan otorisasi? Mengapa permission harus diperiksa di server, bukan hanya dengan menyembunyikan tombol pada template?**

   Autentikasi (*authentication*) adalah proses menentukan siapa yang mengirim request, misalnya mengenali user melalui session login. Otorisasi (*authorization*) adalah proses menentukan tindakan apa yang boleh dilakukan oleh user tersebut, misalnya apakah user boleh membuat, mengubah, atau menghapus achievement.

   Dalam Django REST Framework, autentikasi menyediakan identitas request, sedangkan permission class memutuskan apakah request tersebut diizinkan. Permission harus diperiksa di server karena tampilan frontend bukan batas keamanan. Pengunjung masih dapat mengirim request langsung ke endpoint API, meskipun tombol `Edit` atau `Delete` disembunyikan di template. Jika server tidak memeriksa permission, request tersebut tetap berpotensi mengubah data.

   Oleh sebab itu, aturan akses visitor, user, editor, dan superuser diterapkan pada permission class di sisi server. Menyembunyikan tombol hanya membantu pengalaman pengguna; itu tidak menggantikan kontrol akses. (Rujukan: [DRF — Authentication](https://www.django-rest-framework.org/api-guide/authentication/), [DRF — Permissions](https://www.django-rest-framework.org/api-guide/permissions/).)

4. **Mengapa request yang mengubah data tetap membutuhkan CSRF token ketika API memakai SessionAuthentication? Mengapa force_authenticate saja tidak membuktikan CSRF berjalan?**

   `SessionAuthentication` menggunakan session Django yang biasanya disimpan melalui cookie browser. Browser dapat menyertakan cookie session secara otomatis saat mengirim request. Hal ini menimbulkan risiko CSRF: situs lain dapat mencoba membuat browser yang sedang login mengirim request yang tidak diinginkan ke aplikasi. Karena itu, request yang mengubah data seperti `POST`, `PUT`, `PATCH`, dan `DELETE` perlu menyertakan token CSRF yang valid saat menggunakan session authentication.

   `force_authenticate()` pada DRF test tools secara langsung menetapkan user pada request untuk mempermudah pengujian autentikasi dan permission. Mekanisme ini melewati alur autentikasi normal berbasis session, sehingga pengujian yang hanya menggunakan `force_authenticate()` tidak membuktikan bahwa validasi CSRF benar-benar aktif.

   Untuk menguji CSRF, test perlu menjalankan request melalui client dengan pemeriksaan CSRF diaktifkan, misalnya `APIClient(enforce_csrf_checks=True)`, lalu menguji request session-authenticated tanpa token dan dengan token yang valid. Dengan begitu, pengujian memeriksa mekanisme CSRF itu sendiri, bukan hanya status login user. (Rujukan: [DRF — Authentication](https://www.django-rest-framework.org/api-guide/authentication/), [DRF — Testing](https://www.django-rest-framework.org/api-guide/testing/), [Django — CSRF protection](https://docs.djangoproject.com/en/5.2/howto/csrf/).)


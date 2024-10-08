Nama : Naurah Iradya Kurniawan

NPM : 2306245900

Kelas : PBP B

Tugas 2
1) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

Jawaban:

Pada saat pertama kita harus mengetahui bahwa main berupa direktori aplikasi dan mamio merupakan direktori project.

Langkah 1: tahapan pertama yang perlu kita lakukan adalah membuat proyek djanggo baru, pada bagian ini direktori utama yang bernama mamio harus dihubungkan dengan repository yang berada pada github mamio. Tahap ini berfungsi untuk membuat kerangka awal aplikasi django dan menyimpan project yang telah kita buat di GitHub. Jadi nanti kalo semisal ada perubahan kita dapat mengatur dan melacak dengan mudah.

Langkah 2: setelah kita sudah membuat project django, selanjutnya kita harus membuat aplikasi baru. aplikasi ini kita namakan main. aplikasi ini berada di dalam project utama yang bernama mamio. Aplikasi main bertujuan untuk menjadi tempat dimana fitur-fitur khusus dari project mamio dibuat.

Langkah 3: Selanjutnya kita harus mendaftarkan aplikasi main ke dalam project mamio. langkah ini bertujuan untuk memberitahu django bahwa ada aplikasi main dan bisa menjalanannya bersama dengan aplikasi lainnya di proyek ini.

Langkah 4: Setelah itu, kita harus membuat product models.py yang berada di dalam aplikasi main dengan class bernama item. model ini nantinya akan menyimpan data produk ke dalam database. Adapun tujuan dari model sendiri adalah seperti template yang menentukan apa saja yang akan disimpan ke dalam databse. pada model yang saya buat saya menginisiasi beberapa data yang diperlukan diantaranya atribut wajib yaitu nama barang (name), harga barang (price), deskripsi barang (description). selain atribut wajib saya juga menambahkan atribut tambahan seperti stok barang (stock), kategori barang (category), rating dalam suatu barang (rating), tanggal barang ditambahkan (date_added), dan terakhir saya juga memberikan discount barang.

Langkah 5: Langkah ke 5 yaitu membuat direktori template yang berada di dalam aplikasi main. lalu di dalam direktori template tersebut saya buat satu file template yang saya namakan main.html. file ini akan berguna untuk menampilkan datav dari program mamio. pada tahap ini aplikasi belum memiliki data apapun di dalam database.

Langkah 6: Selanjutnya saya membuat suatu fungsi pada file views.py yang terdapat dalam aplikasi main. Hal ini bertujuan untuk menghubungkan data yang terdapat pada model dengan template main.html. Fungsi ini nantinya bertugas untuk mengambil data dari database dan mengirimkannya ke file HTML. tujuannya adalah agar data yang sudah di input dapat terlihat pada website.

Langkah 7: Pada langkah ini saya membuat file urls.py yang berada di aplikasi main. Fungsi dari langkah ini adalah untuk mengatur URL di aplikasi main dan memetakan fungsi yang sudah dibuat di views.py. Fitur ini juga mengatur URL yang bisa diakses pengguna dan setiap URL akan diarahkan ke fungsi tertentu di views.py.

Langkah 8: Selanjutnya saya menambahkan routing pada urls.py pada project mamio. Langkah ini bertujuan untuk memastikan bahwa URL dari project utama dan bisa diarahkan ke aplikasi main yang sebelumnya sudah dibuat.

Langkah 9: Langkah terakhir yang saya lakukan adalah melakukan deployment project mamio ke platform web service (PWS). Hal ini bertujuan untuk membuat project diunggah ke server PWS agar bisa diakses orang lain melalui internet.
Setelah ini tampilan platform yang kita buat dapat dilihat pada link yang tertera.


2) Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawaban:
![bagan pbp](https://github.com/user-attachments/assets/1069b46a-54fc-4d15-a524-e30d0edbc7eb)

Pada bagan yang saya buat terdapat alur yang memproses jalannya pengolahanan request dari berupa request client hingga menghasilkan suatu output sesuai dengan kemauan client. adapun tahapannya adalah sebagai berikut:

Langkah 1: User membuat request dari internet. Saat user mengakses website, mereka mengirimkan HTTP request ke server.

Langkah 2: Setelah request dikirim web server menerima request tersebut. dan web server bertanggung jawab untuk memproses request HTTP dari internet dan meneruskannya ke aplikasi django.

Langkah 3: Django menerima request dari web server dan memulai siklus request-response. Disini django memeriksa file urls.py untuk mencocokkan URL yang diminta dengan pola URL yang terdaftar.

Langkah 4: Ketika URL cocok, django mengirimkan request ke fungsi atau class view pada views.py. Django mengekstraksi argumen dari request dan meneruskannya ke view.

Langkah 5: Setelah argumen diekstraksi dan view dipanggil langkah berikutnya adalah views.py berkomunikasi dengan models.py untuk mendapatkan data yang relevan dari database.

Langkah 6: Setelah data yang dibutuhkan telah ditemukan pada models.py, data tersebut akan dikembalikan ke view dan kemudian diteruskan ke template HTML untuk ditampilkan kepada user.

Langkah 7: Setelah template sudah sesuai dengan data, django akan mengirimkan HTTP response kembali ke user. Response ini berupa HTML yang ditampilkan di browser user. Pada akhirnya user dapat melihat request yang mereka inginkan.

3) Jelaskan fungsi git dalam pengembangan perangkat lunak!

Jawaban:

Git merupakan sebuah sistem kontrol versi yang sering digunakan dalam pengembangan perangkat lunak. Git berfungsi untuk mengelola perubahan kode secara efisien dan mendukung kolaborasi tim. Dengan git, pengembang dapat melacak setiap perubahan, memulihkan versi sebelumnya, serta bekerja bersama-sama pada proyek dengan lebih terstruktur.

Pertama, git berfungsi sebagai tempat pengelolaan repositori, baik secara lokal di komputer maupun di server github. Pengembang dapat menyimpan dan mengatur proyek mereka di dalam repositori yang dapat diakses kembali kapan saja.

Kedua, git juga berfungsi untuk melacak perubahan kode yang dilakukan. Setiap kali perubahan disimpan dalam commit, git mencatat versi baru proyek beserta informasi seperti siapa yang melakukan perubahan, kapan, dan deskripsi perubahan tersebut.

Ketiga, git juga mendukung kolaborasi tim dengan kemungkinan banyak pengembang dapat bekerja pada salinan lokal proyek, membuat perubahan, dan menggabungkannya kembali ke repositori untama secara terorganisir.

4) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Jawaban:

Framework pada django seringkali dijadikan sebagai permulaan dalam proses pembelajaran pengembangan perangkat lunak karena relatif mudah dipahami. Django menyediakan dokumentasi yang lengkap dan komunitas yang aktif sehingga pemula dapat dengan cepat memahami konsep dasar pengembangan web.

Djang juga terstruktur dengan baik, sehingga memudahkan pengembang untuk mengatur dan mengelola proyek secara efisien. Struktur yang jelas membantu pemula membangun fondasi pengembangan perangkat lunak yang rapi dan sistematis.

Pendekatan berbasis Model-View-Template (MVT) yang digunakan pada django banyak diterapkan dalam pengembangan perangkat lunak. Dengan mempelajari MTV pemula dapat memahami konsep pemisahan tanggung jawab dalam aplikasi yang sangat penting untuk pengembangan perangkat lunak skala besar.

Selain itu, django memiliki popularitas yang tinggi dan telah digunakan oleh banyak perusahaan besar seperti instagram, pinterest, dan mozilla. Penggunaan django di industri skala besar memberikan keuntungan bagi pemula yang ingin mempelajari teknologi yang banyak diterapkan di dunia kerja.

5) mengapa model pada Django disebut sebagai ORM?

Jawaban:

Model dalam Django disebut ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara objek dalam kode Python dan tabel di database relasional. ORM memungkinkan pengembang untuk mengelola dan bekerja dengan data menggunakan objek Python, tanpa perlu menulis query SQL secara manual.

Dengan menggunakan ORM, pengembang bisa melakukan berbagai operasi pada data, seperti menambah, mengubah, atau menghapus data, hanya dengan menggunakan metode dan atribut objek di Python. Ini membuat pengembangan lebih efisien karena pengembang tidak perlu menulis perintah SQL yang rumit. Sebaliknya, ORM secara otomatis menerjemahkan operasi yang dilakukan pada objek Python menjadi perintah SQL yang sesuai dan menjalankannya di database.

Dengan cara ini, ORM menyederhanakan interaksi dengan database dan memungkinkan pengembang untuk fokus pada pengembangan logika aplikasi tanpa harus memikirkan detail teknis dari SQL dan struktur database.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tugas 3

1)  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Jawaban:

Data delivery memiliki peran yang sangat penting dalam memastikan bahwa data yang disimpan di server maupun database pusat dapat diakses oleh pengguna di berbagai lokasi secara efisien. Dalam proses pengembangan sebuah platform, data delivery menjadi elemen utama karena platform sering kali harus terhubung dan berinteraksi dengan berbagai layanan lain, seperti layanan basis data, cloud storage, atau sistem autentikasi dapat berfungsi dengan baik. selain itu, proses transfer dan penerimaan data melalui data delivery ini memastikan bahwa data yang diperlukan dapat dikirim dalam format yang tepat dan sesuai dengan kebutuhan spesifik.

Dengan adanya data delivery yang efektif, sistem yang berbeda dapat berkomunikasi secara lebih jelas dan terstruktur, sehingga mereka mampu bekerja sama secara optimal. Selain itu, data delivery yang andal berperan penting dalam menjaga keamanan dan memastikan akurasi data selama proses pertukaran antarplatform. Tanpa mekanisme data delivery yang efisien, komunikasi antar sistem bisa terganggu dan berpotensi menyebabkan kesalahan atau keterlambatan dalam penyampaian informasi. Dengan demikian, data delivery tidak hanya mendukung kinerja platform secara keseluruhan, tetapi juga meningkatkan kolaborasi antar layanan serta memastikan bahwa data tetap aman dan dapat diakses dengan akurat di seluruh sistem.

2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML

Jawaban:

Baik XML (eXtensible Markup Language) maupun JSON (JavaScript Object Notation) memiliki kegunaan dan kelebihan masing-masing, tetapi JSON lebih populer dalam banyak kasus karena beberapa alasan utama. 

Pertama, JSON memiliki sintaksis yang lebih sederhana dan lebih mudah dibaca dibandingkan XML. JSON menggunakan format objek JavaScript yang langsung dikenali oleh banyak bahasa pemrograman, sedangkan XML memerlukan banyak tag dan atribut yang dapat membuat struktur data menjadi lebih rumit.

Kedua, JSON biasanya menghasilkan ukuran data yang lebih kecil dibandingkan XML. Ini disebabkan oleh fakta bahwa JSON tidak memerlukan tag penutup dan atribut tambahan yang ada di XML, sehingga lebih efisien dalam hal bandwidth dan penyimpanan.

Ketiga, parsing dan penanganan JSON umumnya lebih cepat dibandingkan XML. Format JSON yang lebih sederhana dan tidak memerlukan parsing tag memungkinkan pemrosesan data yang lebih cepat. Selain itu, banyak bahasa pemrograman modern memiliki dukungan bawaan untuk parsing JSON yang memudahkan penggunaannya dalam aplikasi web dan API.

Keempat, JSON secara langsung kompatibel dengan JavaScript yang membuatnya sangat populer dalam pengembangan web. Data JSON dapat dengan mudah diubah menjadi objek JavaScript sehingga memudahkan integrasi dengan aplikasi web. Selain itu, JSON lebih baik dalam menangani struktur data yang kompleks dan mendalam berkat kemampuannya untuk menyimpan data dalam bentuk array dan objek.

Namun, XML juga memiliki kelebihan tersendiri. XML mendukung namespace, validasi skema, dan kemampuan untuk mendokumentasikan metadata secara lebih detail. Hal ini menjadikannya lebih cocok untuk beberapa aplikasi di mana struktur data dan validasi yang ketat diperlukan.

Secara keseluruhan, pemilihan antara XML dan JSON bergantung pada kebutuhan spesifik proyek dan preferensi teknis. Meskipun XML memiliki kelebihan dalam hal struktur dan validasi, JSON sering dipilih karena kemudahan penggunaan dan efisiensi yang lebih baik dalam konteks pengembangan web dan API modern.


3) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Jawaban:

Method is_valid() pada form djanggo berfungsi untuk memeriksa apakah data yang dikirim melalui form valid atau tidak. Saat pengguna mengisi form dan mengirimkan data, method is_valid() akan otomatis memeriksa data tersebut untuk memastikan semuanya sesuai dengan aturan yang telah ditetapkan dalam form. Hal ini mencakup pengecekan tipe data seperti angka, email, atau URL untuk memastikan semuanya benar sesuai dengan format yang telah ditetapkan. Jika data yang diterima valid maka method ini akan mengembalikan nilai true. Sebaliknya, jika tidak valid maka method ini akan mengembalikan nilai false. Dengan menggunakan method is_valid() pengembang tidak perlu membuat validasi secara manual untuk setiap input. Hal ini disebabkan karena pada method is_valid() sudah menangani semua bentuk validasi secara otomatis. Ini dapat mempermudah proses validasi dan mengurangi kemungkinan kesalahan dalam memeriksa data dari pengguna.

4) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Jawaban:

csrf_token digunakan untuk meningkatkan keamanan pada aplikasi djanggo. csrf_token memiliki bentuk nilai yang acak dan bersifat unik. Fungsi dari token ini adalah untuk memastikan bahwa setiap permintaan yang dikirim ke server benar-benar berasal dari pengguna yang sah (pengguna sebenarnya) bukan dari pihak yang mencoba memanfaatkan sesi yang sudah aktif untuk melakukan penyerangan. Token ini berfungsi sebagai lapisan perlindungan tambahan terhadap serangan Cross-Site Resquest Forgery (CSRF). 

Melalui token ini, server dapat melakukan validasi token. Pada saat server menerima data, Server akan melalukan pemeriksaan terhadap token. Server akan mengecek apakah token dalam form sesuai dengan token yang disimpan dalam sesi pengguna. Jika token tidak valid atau tidak ada maka server akan menolak permintaan tersebut. Hal ini dilakukan untuk melindungi aplikasi dari potensi serangan. 

csrf_token memiliki peranan penting dalam menjaga keamanan aplikasi. Tanpa adanya csrf_token aplikasi bisa menjadi target serangan CSRF, dimana penyerang dapat menyalahgunakan sesi yang sah untuk melakukan tindakan yang tidak diinginkan atas nama pengguna yang terautentikasi. 

Contoh penyerangan yang terjadi adalah penyerang bisa menyisipkan form berbahaya di situs mereka. Lalu pada saat pengguna yang sudah login mengunjungi situs tersebut form tersebut akan mengirimkan permintaan berbahaya tanpa sepengetahuan pengguna. Hal ini dapat mengakibatkan perubahan data atau pengambilan informasi pribadi.

5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban:

Langkah 1: Membuat direktori templates dan file HTML
Langkah ini berfungsi untuk menyiapkan struktur dasar tampilan aplikasi web. Dengan membuat direktori templates pada folder utama proyek dan file base.html dapat membangun kerangka umum yang akan digunakan untuk menyusun halaman-halaman web lainnya. Ini memastikan bahwa elemen-elemen seperti header, footer, dan layout konsisten pada seluruh aplikasi.

Langkah 2: Melakukan konfigurasi pengaturan pada settings.py dan menyusun main.html
Pada langkah ini, saya mengatur django untuk mengenali direktori templates dengan memperbarui settings.py khususnya pada bagian DIRS. Hal ini memastikan django dapat menemukan dan menggunakan template HTML yang telah dibuat. Kemudian saya juga menambahkan {% extends 'base.html' %} dan {% block content %} pada main.html.Hal ini berguna untuk menghubungkan template dengan base.html dan menentukan area dimana konten spesifik ditampilkan.

Langkah 3: Menyiapkan model dan melakukan migrasi
Pada langkah ini saya melibatkan penambahan import uuid dalam models.py dan mendefinisikan model data, seperti item produk yang akan disimpan dalam database. Setelah mendefinisikan model saya melakukan migrasi untuk memperbarui skema database dengan perintah python manage.py makemigrations dan python manage.py migrate. hal ini memudahkan saya untuk menyimpan dan mengelola data produk dengan benar di database.

Langkah 4: Membuat form input data dan menampilkan item entry pada html
Pada langkah ini, saya membuat sebuah form input dengan membuat berkas forms.py yang berisi ItemForm untuk model Item. Di sini, saya mendefinisikan field yang akan digunakan dalam form, seperti name, price, description, stock, category, rating, dan discount yang nantinya digunakan untuk menangkap input data dari pengguna. Form ini memungkinkan saya untuk memproses dan menyimpan data baru ke dalam database dengan mudah. Selanjutnya, saya mengintegrasikan form tersebut dalam fungsi create_item pada views.py untuk menampilkan form dan menangani penyimpanan data. Setelah itu, saya memodifikasi template create_item.html agar form bisa diakses dan menambahkan fungsi validasi untuk memastikan data yang diinput valid sebelum disimpan ke database. Hal ini penting agar aplikasi dapat menerima entri baru dan menampilkannya dengan baik di halaman utama. Setelah itu, saya melakukan perintah python manage.py runserver dan membuka http://localhost:8000/ Fungsi dari langkah ini adalah untuk menjalankan aplikasi Django di server lokal dan memastikan bahwa data yang ditambahkan melalui form dapat terlihat di halaman utama aplikasi saat diakses melalui browser.

Langkah 5: Mengembalikan data dalam bentuk XML
Pada langkah ini, saya menambahkan fungsi baru dalam views.py yang mengubah data dari model Item menjadi format XML menggunakan serializers. Fungsi ini mengembalikan data yang sudah diserialisasi sebagai HttpResponse dengan tipe konten "application/xml". Saya kemudian mengupdate urls.py untuk mengarahkan URL tertentu ke fungsi ini, memungkinkan akses data XML melalui browser. Setelah konfigurasi, saya menjalankan proyek dan memverifikasi hasilnya di browser untuk memastikan data ditampilkan dalam format XML.

Langkah 6: Mengembalikan data dalam bentuk JSON
Pada langkah ini, saya membuat fungsi show_json di views.py untuk mengubah data dari model Item menjadi format JSON menggunakan serializers. Fungsi ini mengembalikan data yang telah diserialisasi sebagai HttpResponse dengan tipe konten "application/json". Setelah itu, saya memperbarui urls.py untuk menambahkan path URL yang mengarah ke fungsi show_json, memungkinkan akses data JSON melalui browser. Terakhir, saya menjalankan proyek dan memeriksa hasilnya di browser untuk memastikan data ditampilkan dalam format JSON.

Langkah 7: Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON
Pada langkah ini, saya menambahkan dua fungsi di views.py, yaitu show_xml_by_id dan show_json_by_id, yang mengambil data berdasarkan ID dari model Item dan mengembalikannya dalam format XML atau JSON. Fungsi-fungsi ini menggunakan metode untuk mengubah data menjadi format XML atau JSON dan mengirimkannya sebagai HttpResponse dengan tipe konten yang sesuai. Saya kemudian memperbarui urls.py untuk menambahkan path URL yang mengarah ke kedua fungsi tersebut, sehingga data dapat diakses melalui browser dengan menyesuaikan ID pada URL. Setelah itu, saya menjalankan proyek untuk memeriksa hasilnya di browser.

Langkah 8: Menggunakan postman debagai data viewer
Pada langkah ini, saya menjalankan server dengan perintah python manage.py runserver dan menggunakan Postman untuk menguji API. Saya membuat request GET di Postman dengan URL seperti http://localhost:8000/xml/ atau http://localhost:8000/json/ untuk memastikan data dikirim dengan benar. Saya juga dapat mengubah URL untuk menguji pengambilan data berdasarkan ID, seperti http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id]. Hasil response dapat dilihat di bagian bawah Postman untuk memverifikasi bahwa data yang diinginkan muncul sesuai dengan format yang diharapkan.

Langkah 9: Melakukan Push Ke PWS Secara Otomatis Menggunakan GitHub Actions
Pada langkah ini, saya membuat otomatisasi untuk deployment ke PWS menggunakan GitHub Actions. Saya membuat file konfigurasi deploy.yml di dalam subdirektori .github/workflows yang mengatur GitHub Actions untuk secara otomatis melakukan push ke PWS setiap kali saya melakukan push ke branch main di GitHub. Selain itu, saya menambahkan URL PWS sebagai secret di pengaturan repositori GitHub untuk otentikasi, dan memperbarui settings.py proyek dengan URL PWS. Setelah melakukan commit dan push, GitHub Actions akan memproses deployment secara otomatis, memudahkan manajemen deployment ke PWS. Setelah itu, saya melakukan add, commit, dan push ke repositori GitHub menggunakan perintah git add ., git commit -m "<pesan_commit>", dan git push -u origin <branch_utama>, dengan menyesuaikan pesan commit dan nama branch utama sesuai kebutuhan. Ini memastikan bahwa perubahan terbaru di direktori lokal saya diperbarui ke repositori GitHub.

Hasil akses url pada postmane:

![alt text](postman-1.png)

![alt text](postman-2.png)

![alt text](postman-3.png)

![alt text](postman-4.png)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Tugas 4
1) Apa perbedaan antara HttpResponseRedirect() dan redirect()

Jawab:

HttpResponseRedirect() dan redirect() di Django adalah dua metode yang digunakan untuk mengarahkan pengguna ke halaman lain, tetapi masing-masing memiliki cara kerja yang berbeda. HttpResponseRedirect() hanya menerima URL sebagai argumennya dan digunakan untuk membuat respons HTTP dengan status 302, yang memberi tahu browser untuk mengarahkan pengguna ke URL tertentu. Ini membuat HttpResponseRedirect() kurang fleksibel karena hanya dapat bekerja dengan URL yang ditentukan secara eksplisit. 

Di sisi lain, redirect() adalah fungsi yang lebih fleksibel dan serbaguna. Selain bisa menerima URL langsung, redirect() juga dapat menerima nama view Django atau parameter yang diperlukan untuk mengarahkan pengguna. Ini memungkinkan pengalihan tanpa harus menentukan URL secara manual, sehingga lebih efisien dalam berbagai situasi. Meskipun lebih fleksibel, pada akhirnya redirect() tetap menghasilkan HttpResponseRedirect di latar belakang untuk menyelesaikan pengalihan. Oleh karena itu, redirect() sering kali lebih disukai dalam pengembangan aplikasi Django karena memberikan lebih banyak kemudahan dan fleksibilitas dibandingkan dengan HttpResponseRedirect().

2) Jelaskan cara kerja penghubungan model MoodEntry dengan User!

Jawab: 

Penghubungan model MoodEntry dengan User di Django bisa dilakukan dengan cara kerja penghubungan model Product dan User. Dalam hal ini, kita menggunakan ForeignKey untuk mengaitkan setiap entri mood dengan pengguna yang membuatnya. Dengan menambahkan ForeignKey di model MoodEntry yang merujuk pada model User, kita dapat memastikan bahwa setiap entri mood terkait dengan satu pengguna tertentu.

Cara kerja ini memungkinkan kita untuk mengelola dan melacak semua entri mood yang dibuat oleh setiap pengguna secara efisien. Setiap kali pengguna membuat entri mood baru, data pengguna tersebut akan disimpan dalam field ForeignKey, sehingga kita bisa dengan mudah mengambil semua entri mood yang terkait dengan pengguna tersebut di masa mendatang. Dengan demikian, Django memudahkan untuk mengelola data, menampilkan, atau memproses entri mood berdasarkan pengguna yang bersangkutan.

Secara keseluruhan, penghubungan antara MoodEntry dan User dengan ForeignKey memungkinkan kita untuk memiliki struktur data yang terorganisir, di mana setiap pengguna dapat memiliki banyak entri mood, namun setiap entri mood hanya dimiliki oleh satu pengguna. Hal ini memastikan relasi yang jelas dan terstruktur antara entri mood dan pengguna di dalam aplikasi Django.


3) Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Jawab:

Authentication dan authorization adalah dua konsep penting dalam keamanan aplikasi, tetapi keduanya memiliki makna yang berbeda. 

Authentication adalah proses untuk memverifikasi identitas pengguna. Ini adalah langkah awal yang memastikan bahwa pengguna adalah siapa yang mereka klaim. Biasanya, ini dilakukan melalui kombinasi nama pengguna dan kata sandi. Saat pengguna melakukan login, aplikasi akan memeriksa kredensial yang diberikan dengan informasi yang ada di basis data untuk menentukan apakah pengguna tersebut valid. Di sisi lain, authorization adalah proses untuk menentukan apakah pengguna yang telah terautentikasi memiliki izin untuk mengakses sumber daya tertentu atau melakukan tindakan tertentu dalam aplikasi. Setelah pengguna berhasil login, aplikasi akan memeriksa hak akses pengguna tersebut untuk memastikan bahwa mereka memiliki izin untuk melihat halaman, mengedit data, atau menjalankan fungsi tertentu.

Dalam implementasi Django, kedua konsep ini ditangani dengan baik. Django menyediakan sistem authentication yang built-in yang memungkinkan developer untuk dengan mudah mengelola pengguna dan kredensial mereka. Ketika pengguna melakukan login, Django menggunakan authenticate() untuk memverifikasi kredensial dan login() untuk menyimpan informasi pengguna ke dalam sesi.  Untuk authorization, Django memiliki sistem permission yang memungkinkan developer untuk menetapkan izin tertentu kepada pengguna atau grup pengguna. Kita dapat menggunakan decorators seperti @login_required untuk melindungi view tertentu dari pengguna yang belum login, dan @permission_required untuk memastikan bahwa pengguna memiliki izin yang diperlukan untuk mengakses fitur tertentu. Secara keseluruhan, authentication dan authorization adalah dua aspek yang saling melengkapi dalam pengelolaan akses pengguna dalam aplikasi, dan Django menyediakan alat yang kuat untuk menangani keduanya dengan efisien.

4) Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Jawab: 

Django mengingat pengguna yang sudah login dengan menggunakan session. Setelah pengguna login, Django membuat sesi khusus yang menyimpan informasi tentang pengguna tersebut. Sesi ini disimpan di server, dan Django mengirimkan cookie ke browser pengguna, yang berisi ID sesi. Cookie ini membantu Django mengenali pengguna saat mereka berpindah halaman di aplikasi, sehingga mereka tidak perlu login ulang setiap kali membuka halaman baru. Dengan begitu, Django tahu siapa yang sedang menggunakan aplikasinya.

Selain untuk mengingat pengguna yang sudah login, cookies juga punya kegunaan lain. Cookies bisa menyimpan preferensi pengguna, seperti pilihan bahasa atau pengaturan tampilan. Ini membuat pengalaman menggunakan aplikasi jadi lebih personal. Cookies juga bisa dipakai untuk melacak aktivitas pengguna, seperti halaman apa yang sering dikunjungi. Informasi ini berguna bagi pengembang untuk memperbaiki fitur dan tampilan situs web.

Namun, tidak semua cookies aman digunakan. Ada risiko keamanan seperti serangan XSS atau pencurian sesi, di mana penjahat siber bisa mencuri informasi dari cookie dan masuk ke akun pengguna. Oleh karena itu, penting untuk memastikan cookies disimpan dengan aman. Misalnya, dengan menggunakan pengaturan HttpOnly dan Secure pada cookie agar cookie tidak bisa diakses oleh orang lain. Selain itu, pengguna juga perlu berhati-hati dengan cookie dari situs yang tidak terpercaya dan bisa mengatur privasi di browser agar lebih aman.

5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:

Langkah 1: Membuat Fungsi dan form registrasi
Pada tahap ini saya memulai dengan mengaktifkan virtual environment dan membuka views.py untuk menambahkan UserCreationForm dan messages. UserCreationForm memudahkan pembuatan formulir registrasi pengguna tanpa menulis kode dari awal, sementara messages digunakan untuk memberikan feedback kepada pengguna setelah mereka berhasil membuat akun. Kemudian, saya membuat fungsi register yang menghasilkan formulir registrasi. Jika pengguna mengisi formulir dan inputnya valid, datanya akan disimpan dan pesan sukses akan muncul. Setelah itu, saya membuat berkas register.html untuk menampilkan formulir ini dengan menggunakan template HTML yang mempermudah proses input. lalu saya menambahkan path URL di urls.py untuk memastikan bahwa halaman registrasi dapat diakses dari browser, sehingga pengguna bisa mendaftar akun sebelum mengakses halaman utama.

Langkah 2: Membuat fungsi login
Pada tahap ini saya membuka file views.py dan menambahkan kode untuk mengimpor authenticate, login, dan AuthenticationForm yang digunakan untuk memverifikasi username dan password, dan login jika valid. Setelah itu, saya membuat fungsi login_user yang menampilkan form login dan memproses data pengguna. Jika input benar, pengguna akan masuk dan diarahkan ke halaman utama. Selanjutnya, saya membuat file login.html untuk menampilkan form login, lengkap dengan tombol login dan link ke halaman registrasi. Terakhir, saya menambahkan path URL di urls.py agar halaman login bisa diakses. Setelah ini, pengguna bisa login sebelum mengakses halaman utama, dan selanjutnya akan ditambahkan fitur logout beserta tombolnya di halaman utama.

Langkah 3: Membuat fungsi logout
Pada tahap ini saya menambahkan impor logout untuk menangani proses keluar dari akun. Lalu, saya membuat fungsi logout_user yang berfungsi untuk menghapus sesi pengguna yang sedang login dan mengarahkan mereka kembali ke halaman login. Setelah itu, saya membuka file main.html dan menambahkan tombol logout dengan menggunakan tag {% url 'main:logout' %} untuk mengarahkan pengguna ke fungsi logout secara dinamis. Terakhir, saya menambahkan path URL untuk fungsi logout di urls.py, sehingga halaman logout bisa diakses. Dengan langkah ini, sistem autentikasi pada proyek selesai dan sekarang user dapat login dan logout dengan mudah.

Langkah 4: Merestriksi Akses Halaman Main
Saya membuka file views.py dan menambahkan impor login_required, yang berfungsi untuk membatasi akses halaman hanya untuk pengguna yang sudah login. Selanjutnya, saya menambahkan decorator @login_required(login_url='/login') di atas fungsi show_main, sehingga pengguna harus login terlebih dahulu sebelum bisa mengakses halaman utama. Setelah menambahkan pembatasan ini, saya menjalankan proyek menggunakan perintah python manage.py runserver, dan ketika membuka halaman utama di browser, pengguna yang belum login akan otomatis diarahkan ke halaman login.

Langkah 5: Membuat 2 akun pengguna dengan masing-masing 3 dummy data.
Pada tahap ini saya melakukan registrasi user dengan memasukkan username serta password. Setelah berhasil registrasi, saya melakukan login dan membuat order makanan yang diinginkan oleh saya sebagai user. Saya melakukan 3 kali order untuk tiap 1 account sehingga terciptalah 3 dummy data. Hal ini juga saya lakukan pada account ke dua yang saya buat.

Langkah 6: Menggunakan Data Dari Cookies
Pada tahap ini saya menambahkan fungsionalitas penggunaan cookies pada aplikasi Django dengan menampilkan data last login di halaman utama. Setelah logout, saya membuka kembali file views.py dan mengimpor HttpResponseRedirect, reverse, dan datetime. Pada fungsi login_user, saya menambahkan cookie last_login menggunakan response.set_cookie('last_login', str(datetime.datetime.now())) setelah login berhasil. Kemudian, di fungsi show_main, saya menambahkan cookie last_login ke dalam konteks yang akan ditampilkan. Pada fungsi logout_user, saya menambahkan perintah untuk menghapus cookie menggunakan response.delete_cookie('last_login'). Terakhir, saya mengubah template main.html untuk menampilkan informasi login terakhir dengan menambahkan <h5>Sesi terakhir login: {{ last_login }}</h5>. Saat proyek dijalankan, data last login akan muncul di halaman utama, dan saya bisa melihat cookie yang dihasilkan pada browser melalui fitur inspect element di bagian cookies.

Langkah 7: Menghubungkan Model Item dengan User
Pada tahap ini saya menghubungkan model Item dengan user yang membuatnya sehingga pengguna hanya bisa melihat item yang mereka buat sendiri. Dimulai dengan membuka models.py, saya menambahkan from django.contrib.auth.models import User untuk mengimpor model User, lalu menambahkan field user sebagai ForeignKey di model Item untuk menghubungkannya dengan user. Setelah itu, saya membuka views.py dan memperbarui fungsi create_item dengan commit=False agar objek tidak langsung disimpan ke database, hal ini memungkinkan saya untuk menambahkan data user dari request.user. Di fungsi show_main, saya mengubah value item_entries untuk hanya menampilkan item yang terkait dengan pengguna yang login. Selanjutnya, saya melakukan migrasi model dengan perintah python manage.py makemigrations dan migrate, dan memilih opsi default value untuk menghindari error saat migrasi. Terakhir, saya mengatur environment production dengan mengubah variabel DEBUG di settings.py, dan ketika dijalankan, hanya item yang dibuat oleh user yang sedang login akan ditampilkan di halaman utama.

Langkah 8: Membuat readme dan melakukan push ke pws
Pada tahap ini saya menjawab pertanyaan yang diminta pada soal ke dalam readme. Setelah saya selesai menjawab saya melakukan add, commit, dan push ke repositori GitHub menggunakan perintah git add ., git commit -m "<pesan_commit>", dan git push -u origin <branch_utama>. karena sebelumnya saya sudah membuat deploy.yml maka setiap kali melakukan add, commit, dan push ke github program juga akan otomatis di push ke pws. Setelah ini tampilan program dapat diakses orang lain melalui internet.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Tugas 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Jawab:

Dalam CSS, ketika beberapa selector digunakan untuk menargetkan elemen yang sama, browser akan menentukan prioritas berdasarkan aturan specificity. Prioritas tertinggi dimiliki oleh inline style, yaitu gaya yang ditetapkan langsung pada elemen HTML menggunakan atribut style. Setelah itu, ID selector memiliki prioritas yang lebih tinggi daripada selector lainnya seperti class, tag, atau attribute selector. Class selector, attribute selector, dan pseudo-class seperti :hover atau :focus berada di bawah ID selector, tetapi lebih tinggi daripada selector berdasarkan tag atau pseudo-element seperti ::before dan ::after. Selector berdasarkan tag HTML dan pseudo-element berada di urutan berikutnya, dengan prioritas lebih rendah dari class dan ID. Di tingkat yang paling rendah adalah universal selector (`*`) serta gaya yang diwarisi dari elemen induk, serta gaya bawaan dari browser. Selain itu, aturan yang menggunakan !important dapat mengesampingkan semua aturan di atas, termasuk selector dengan specificity lebih tinggi, kecuali jika ada aturan lain yang juga menggunakan !important, dalam hal ini prioritas tetap ditentukan oleh specificity. Singkatnya, urutan prioritas CSS selector adalah: inline style, ID selector, class selector, tag selector, universal selector, dan diakhiri oleh aturan !important, yang bisa mengesampingkan semua aturan lainnya.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Jawab:

Responsive design telah menjadi elemen penting dalam pengembangan aplikasi web modern karena perilaku pengguna yang semakin beragam dalam mengakses internet dari berbagai perangkat. Mulai dari smartphone, tablet, laptop, hingga desktop, setiap perangkat memiliki ukuran layar dan resolusi yang berbeda-beda. Tanpa desain yang responsif, situs web mungkin akan terlihat tidak rapi atau sulit diakses di perangkat tertentu, terutama pada layar yang lebih kecil seperti ponsel. Dengan menerapkan responsive design, tata letak, gambar, teks, dan elemen lainnya akan menyesuaikan ukuran layar pengguna secara otomatis. Hal ini memastikan bahwa situs web tetap mudah dibaca dan navigasi tetap berjalan mulus tanpa memerlukan tindakan tambahan dari pengguna seperti memperbesar tampilan atau melakukan scroll secara horizontal. Pentingnya desain responsif juga berkaitan erat dengan ekspektasi pengguna saat ini yang menginginkan pengalaman online yang konsisten, terlepas dari perangkat yang digunakan.

Selain meningkatkan pengalaman pengguna, responsive design juga memberikan dampak positif pada performa situs web dalam hal optimasi mesin pencari (SEO). Situs yang dirancang untuk responsif lebih disukai oleh mesin pencari seperti Google, karena Google mengutamakan situs yang ramah seluler dalam peringkat pencariannya. Hal ini berarti bahwa situs web yang memiliki desain responsif memiliki peluang lebih besar untuk mendapatkan peringkat yang lebih tinggi dalam hasil pencarian, meningkatkan jumlah pengunjung organik, dan memperkuat kehadiran digital secara keseluruhan. Dengan semakin banyaknya pengguna yang mengakses internet melalui perangkat mobile, responsivitas bukan hanya menjadi pilihan tambahan, tetapi kebutuhan penting dalam menciptakan aplikasi web yang kompetitif. Desain yang tidak responsif dapat membuat pengguna meninggalkan situs dengan cepat karena merasa tidak nyaman, yang pada akhirnya dapat menurunkan engagement dan conversion rate dari situs tersebut.

Sebagai contoh, aplikasi seperti YouTube telah menerapkan responsive design dengan sangat baik. Ketika diakses dari perangkat apapun baik itu desktop, tablet, atau smartphone konten video, teks, serta elemen interaktif seperti tombol dan menu, semuanya akan secara otomatis menyesuaikan ukuran layar tanpa mengorbankan fungsionalitas atau estetika. Pengguna tidak perlu khawatir tentang bagaimana tampilan YouTube di perangkat mereka karena tata letaknya sudah dirancang untuk fleksibel dan intuitif. Di sisi lain, beberapa situs web lama, seperti beberapa situs pemerintahan, belum sepenuhnya mengadopsi konsep responsive design. Akibatnya, ketika diakses dari smartphone, situs-situs ini tampak terpotong atau memaksa pengguna untuk melakukan zoom dan scroll secara horizontal, yang sangat mengganggu pengalaman pengguna. Masalah ini menunjukkan betapa pentingnya penerapan responsive design dalam memastikan aksesibilitas dan kenyamanan pengguna di era digital ini.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Jawab:

Margin, border, dan padding adalah tiga properti CSS yang digunakan untuk mengatur tata letak dan spasi elemen dalam halaman web, namun masing-masing memiliki fungsi yang berbeda. Margin merupakan ruang di luar elemen yang memisahkannya dari elemen lain. Margin digunakan untuk menciptakan jarak antara elemen-elemen yang berdekatan tanpa mempengaruhi ukuran elemen itu sendiri. Misalnya, jika suatu paragraf diberi margin, maka ruang tersebut akan memisahkan paragraf dengan elemen di sekitarnya. Margin dapat diatur secara individual untuk setiap sisi (atas, kanan, bawah, dan kiri) atau secara seragam untuk keempat sisinya sekaligus.

Sementara itu, border adalah garis yang mengelilingi elemen dan terletak di antara margin dan padding. Border berfungsi untuk memberikan visualisasi batas elemen dan dapat disesuaikan ketebalan, warna, serta gaya garisnya. Border sering digunakan untuk memperjelas tepi elemen, serta dapat menambah estetika dalam desain sebuah halaman web. Anda bisa mengatur border untuk setiap sisi secara terpisah atau mengaturnya sekaligus untuk keempat sisi.

Di sisi lain, padding adalah ruang di dalam elemen, yang terletak antara konten elemen dan border. Padding memberikan jarak antara isi elemen (seperti teks atau gambar) dengan border, sehingga konten tidak menempel langsung pada tepi elemen tersebut. Padding hanya memengaruhi jarak dalam elemen itu sendiri dan tidak memengaruhi jarak antar elemen. Seperti margin dan border, padding juga bisa diatur secara keseluruhan atau untuk tiap sisi secara individual. Ketiga properti ini sering digunakan bersama-sama untuk memastikan tata letak elemen terlihat rapi dan memberikan pengalaman visual yang lebih baik bagi pengguna.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Jawab:

Flexbox dan Grid Layout adalah dua metode tata letak dalam CSS yang sangat berguna untuk mengatur elemen-elemen pada halaman web secara responsif dan fleksibel, masing-masing dengan keunggulan tersendiri tergantung pada kebutuhan tata letak. Flexbox, atau Flexible Box Layout, dirancang untuk mengelola elemen dalam satu dimensi, baik secara horizontal maupun vertikal. Flexbox sangat cocok untuk menyusun elemen-elemen yang harus beradaptasi dengan berbagai ukuran layar atau kontainer, seperti bar navigasi, deretan tombol, atau komponen dalam satu baris atau kolom. Dengan Flexbox, pengembang dapat dengan mudah mengontrol perataan (alignment), distribusi (distribution), dan pengaturan ulang elemen-elemen. Flexbox juga memungkinkan pengaturan elemen secara dinamis menggunakan properti seperti flex-grow dan flex-shrink untuk mengatur seberapa besar atau kecil elemen dapat menyesuaikan diri dengan ruang yang tersedia.

Di sisi lain, Grid Layout adalah model tata letak yang bekerja dalam dua dimensi, yaitu baris dan kolom secara bersamaan. Grid lebih cocok digunakan ketika pengembang membutuhkan tata letak yang lebih terstruktur dan kompleks, seperti galeri gambar, halaman beranda, atau dashboard yang memiliki banyak elemen yang harus ditempatkan dalam baris dan kolom tertentu. Dengan properti seperti grid-template-rows dan grid-template-columns, pengembang dapat dengan mudah mendefinisikan jumlah dan ukuran baris serta kolom dalam grid, memberikan kontrol penuh atas penempatan elemen dalam tata letak yang lebih teratur dan presisi. Grid Layout juga menyediakan cara yang lebih efektif untuk mengelola elemen-elemen dengan berbagai ukuran dan menata halaman yang membutuhkan tata letak yang kompleks.

Secara umum, Flexbox lebih ideal untuk tata letak satu dimensi, seperti menyusun elemen-elemen dalam satu baris atau kolom, sedangkan Grid Layout lebih cocok untuk tata letak dua dimensi yang lebih rumit, seperti halaman yang membutuhkan pengaturan elemen di berbagai baris dan kolom. Keduanya memberikan fleksibilitas yang luar biasa dalam menciptakan tata letak halaman web yang responsif, memastikan elemen-elemen terlihat rapi dan berfungsi dengan baik di berbagai perangkat.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Jawab:

Langkah 1: Mengatur Static Files di Django
Static files adalah file pendukung yang diperlukan untuk memberikan tampilan dan interaksi pada halaman web dalam proyek Django, seperti CSS, JavaScript, dan gambar. Untuk mengatur static files, saya melakukan konfigurasi di file settings.py. Di dalamnya, terdapat dua pengaturan penting yang perlu diperhatikan yaitu STATIC_URL dan STATIC_ROOT. STATIC_URL adalah URL yang digunakan untuk mengakses file statis, misalnya `http://localhost:8000/static/image/example-image.png`, sedangkan STATIC_ROOT menentukan path absolut ke direktori di mana semua file statis akan dikumpulkan saat menjalankan perintah collectstatic. Dengan pengaturan ini, saya dapat dengan mudah mengelola dan mengakses file statis dalam aplikasi Django saya.

Laangkah 2: Menambahkan Tailwind ke Aplikasi
Pada tahap ini, saya menambahkan Tailwind untuk styling aplikasi Django. Pertama, saya membuka proyek Django saya (mamio) dan mengakses file base.html yang terletak di folder templates di root proyek. Di dalam file templates/base.html, saya menambahkan tag `<meta name="viewport">` agar halaman web dapat menyesuaikan ukuran dan perilaku perangkat mobile. Tag ini penting karena membantu browser mengatur skala halaman sehingga tampilan web menjadi responsif dan mudah dibaca pada berbagai ukuran layar. Setelah itu, saya menghubungkan template Django dengan Tailwind menggunakan script CDN (Content Delivery Network) dari Tailwind, yang saya letakkan di dalam tag `<head>` di file base.html. Penggunaan CDN memungkinkan saya untuk mengakses library Tailwind secara langsung tanpa perlu mengunduh dan menyimpannya di server, sehingga mempermudah proses pengembangan. Dengan langkah-langkah ini, saya telah berhasil menyiapkan Tailwind untuk digunakan dalam aplikasi Django saya, sehingga dapat meningkatkan kualitas tampilan dan responsivitas aplikasi.

Langkah3: Menambahkan Fitur Edit Item pada Aplikasi
Pada tutorial ini, saya akan menambahkan fitur untuk mengubah data item dalam aplikasi Django. Pertama, saya membuka file views.py di subdirektori main dan membuat fungsi baru bernama edit_ite, yang menerima parameter request dan id. Fungsi ini bertugas untuk mengambil entri item berdasarkan id, mengatur entri item sebagai instance dari form, serta memvalidasi dan menyimpan form jika permintaan adalah metode POST. Dengan adanya fungsi ini, pengguna dapat memperbarui informasi item yang telah ada di database. Selanjutnya, saya menambahkan impor yang diperlukan di file views.py, termasuk fungsi render, reverse, dan HttpResponseRedirect. Setelah itu, saya membuat berkas HTML baru bernama edit_item.html di subdirektori main/templates, yang akan menampilkan form untuk mengedit item. Form ini memungkinkan pengguna untuk memasukkan data baru yang ingin diubah. Kemudian, saya membuka file urls.py di direktori main, mengimpor fungsi edit_item, dan menambahkan path URL untuk mengakses fungsi ini ke dalam urlpatterns. Ini memungkinkan pengguna untuk mengakses fitur edit dengan menggunakan URL yang sesuai. Selanjutnya, saya membuka main.html di subdirektori main/templates dan menambahkan potongan kode untuk menampilkan tombol edit di setiap baris tabel dengan membangun URL untuk tombol edit berdasarkan primary key (`pk`) dari objek item_entry. Dengan menambahkan tombol edit, pengguna dapat dengan mudah mengakses halaman edit untuk setiap item. Terakhir, saya menjalankan proyek Django menggunakan perintah python manage.py runserver dan membuka [http://localhost:8000] di browser. Setelah login, saya mencoba mengklik tombol edit pada suatu item dan mengubah datanya. Jika perubahan tersimpan dan tampil di halaman utama aplikasi tanpa error, maka saya berhasil menambahkan fitur edit! Fitur ini sangat penting karena memberikan fleksibilitas kepada pengguna untuk mengelola data mereka dengan lebih baik, memastikan bahwa informasi yang ditampilkan selalu akurat dan terkini.

Langkah 4: Tutorial: Menambahkan Fitur Hapus Item pada Aplikasi
Pada langkah ini, saya akan menambahkan fitur untuk menghapus data item dalam aplikasi Django. Pertama, saya membuat fungsi baru bernama delete_item dalam file views.py di folder main. Fungsi ini bertugas untuk mengambil item berdasarkan id, menghapus entri tersebut dari database, dan mengarahkan pengguna kembali ke halaman utama setelah penghapusan berhasil. Kode yang digunakan untuk fungsi ini adalah sederhana dan efektif dalam menjalankan fungsinya.
Selanjutnya, saya membuka file urls.py di folder main untuk mengimpor fungsi delete_item yang baru saja dibuat. Saya kemudian menambahkan path URL dalam urlpatterns, yang memungkinkan pengguna mengakses fungsi ini menggunakan URL yang sesuai, seperti `delete/<id>`. Penting untuk memastikan tipe data dari id sesuai dengan atribut id di model item. Setelah itu, saya membuka berkas main.html di folder main/templates dan mengubah kode untuk menambahkan tombol hapus di setiap baris tabel. Dengan menambahkan tombol delete, pengguna dapat dengan mudah menghapus entri yang tidak diinginkan. Tombol ini menggunakan URL yang dibangun berdasarkan primary key (`pk`) dari objek item, sehingga mengarahkan pengguna ke fungsi delete_item yang tepat. Selanjutnya, saya menjalankan proyek Django dengan perintah python manage.py runserver dan membuka [http://localhost:8000] di browser. Setelah login, saya mencoba menghapus salah satu item dan kemudian melakukan refresh pada halaman. Jika item tersebut hilang dari halaman utama tanpa adanya error, maka saya berhasil menambahkan fitur hapus! Fitur ini sangat penting karena memberikan pengguna kemampuan untuk mengelola data mereka dengan lebih baik, menghapus informasi yang tidak lagi diperlukan dan menjaga agar aplikasi tetap bersih dan relevan.

Langkah 5: Menambahkan Navigation Bar pada Aplikasi 
Untuk menambahkan Navigation Bar (navbar) pada aplikasi saya, langkah pertama adalah membuat berkas HTML baru dengan nama navbar.html di dalam folder templates/ pada direktori root proyek. Navbar ini akan berfungsi sebagai elemen navigasi yang memudahkan pengguna untuk berpindah antara berbagai halaman atau fitur dalam aplikasi web saya. Saya akan mengisi navbar.html dengan template yang telah disediakan, di mana navbar ini memiliki latar belakang gradasi warna pink dan elemen-elemen yang responsif untuk tampilan desktop dan mobile. Dalam tampilan desktop, navbar akan menampilkan judul aplikasi "🍽️Welcome to MAMIO🍽️", serta tautan navigasi untuk halaman seperti Home, Create Item, Cart, Categories, dan Products. Selain itu, navbar ini juga akan menyambut pengguna yang sudah login dengan menampilkan nama pengguna mereka dan memberikan opsi untuk logout. Bagi pengguna yang belum login, terdapat tombol untuk login dan registrasi. Navbar ini juga dilengkapi dengan menu mobile yang akan ditampilkan ketika tampilan pada perangkat lebih kecil. Tombol menu mobile akan membuka dan menutup menu yang berisi tautan navigasi yang sama. Untuk mengaktifkan fungsi ini, terdapat skrip sederhana yang menangani klik pada tombol menu, mengubah kelas CSS dari elemen menu mobile untuk menampilkannya atau menyembunyikannya. Setelah berkas navbar.html selesai saya buat, langkah selanjutnya adalah menghubungkan navbar tersebut dengan berkas-berkas lain dalam aplikasi saya, seperti main.html, create_item.htm, dan edit_item.html, yang berada di subdirektori main/templates/. Saya perlu menambahkan tag `{% include 'navbar.html' %}` di dalam blok konten setiap berkas tersebut untuk menyertakan navbar di bagian atas halaman. Pastikan untuk menempatkan tag include di dalam blok yang sudah ada. Dengan cara ini, setiap halaman yang menggunakan navbar.html akan memiliki navigasi yang konsisten, memudahkan pengguna untuk menjelajahi aplikasi dengan lebih baik. Dengan menambahkan navbar, saya memberikan pengalaman pengguna yang lebih baik, membantu mereka menemukan fitur yang mereka butuhkan dengan lebih cepat dan efisien.

Langkah 6: Konfigurasi Static Files pada Aplikasi
Untuk mengonfigurasi static files pada aplikasi saya, langkah pertama yang perlu dilakukan adalah menambahkan middleware WhiteNoise pada berkas settings.py. Saya akan menambahkan baris whitenoise.middleware.WhiteNoiseMiddleware tepat di bawah SecurityMiddleware dalam daftar MIDDLEWARE. Dengan menambahkan middleware WhiteNoise pada settings.py, Django akan dapat mengelola file statis secara otomatis dalam mode produksi (dengan `DEBUG=False`) tanpa memerlukan konfigurasi yang kompleks. Hal ini sangat berguna agar file statis tersebut dapat diakses saat melakukan deployment, karena secara default, ketika `DEBUG=False`, Django tidak menyediakan akses ke file statis. Selanjutnya, saya perlu memastikan bahwa variabel STATIC_URL, STATICFILES_DIRS, dan STATIC_ROOT sudah dikonfigurasi dengan benar. Jika belum ada, saya akan menambahkannya. Variabel STATIC_URL akan diatur ke `'/static/'`, dan untuk mode pengembangan, STATICFILES_DIRS akan merujuk ke folder `/static` di root project. Sementara itu, untuk mode produksi, STATIC_ROOT akan dirujuk ke folder yang sama. Dengan pengaturan ini, saya memastikan bahwa aplikasi saya dapat mengelola dan menyajikan file statis dengan baik, baik dalam mode pengembangan maupun produksi, sehingga pengguna dapat mengakses file statis seperti CSS, JavaScript, dan gambar dengan lancar di aplikasi saya.

Langkah 7: Menambahkan Styles pada Aplikasi dengan Tailwind dan External CSS
Untuk menambahkan styles pada aplikasi saya dengan menggunakan Tailwind dan CSS eksternal, saya dapat mengikuti langkah-langkah opsional ini. Pertama, saya akan membuat file global.css di direktori `/static/css` pada root directory. Di dalam file ini, saya bisa menambahkan kelas custom atau style CSS yang telah saya definisikan sendiri. Selanjutnya, untuk menghubungkan global.css dan script Tailwind ke dalam template Django, saya perlu menambahkan file tersebut ke dalam base.html. Saya akan memodifikasi base.html dengan menambahkan `{% load static %}` di bagian atas, menyertakan script Tailwind melalui CDN, serta mengaitkan file global.css dengan menambahkan tag `<link>`. Dengan melakukan langkah-langkah ini, saya dapat memastikan bahwa style CSS yang ditambahkan dalam `global.css` dapat digunakan dalam template Django saya, sehingga tampilan aplikasi menjadi lebih menarik dan sesuai dengan kreasi saya.

Langkah 8: Menambahkan custom styling ke global.css
Pada langkah ini, saya akan menambahkan custom styling ke dalam file global.css yang terletak di static/css/ Saya akan mengatur tampilan elemen form, termasuk input, textarea, dan select, agar memiliki lebar 100%, padding, serta border yang rapi. Selain itu, saya juga akan menambahkan efek fokus untuk meningkatkan interaksi pengguna. Di samping itu, saya akan membuat animasi bernama shine yang memberikan efek kilau pada elemen dengan kelas .animate-shine, sehingga tampilan aplikasi menjadi lebih menarik dan dinamis. Modifikasi ini bertujuan untuk meningkatkan pengalaman visual pengguna pada aplikasi.

Langkah 9: Styling Halaman Login
Pada langkah ini, saya akan memodifikasi berkas login.html di subdirektori main/templates/ untuk mempercantik tampilan halaman login aplikasi. Dengan menggunakan Tailwind CSS, saya akan menambahkan latar belakang gradien, teks yang menarik, serta formulir login yang berisi input untuk username dan password. Selain itu, saya akan menyertakan logika untuk menampilkan pesan sukses atau kesalahan setelah upaya login, serta tautan untuk pendaftaran bagi pengguna baru. Tujuan dari modifikasi ini adalah untuk meningkatkan pengalaman pengguna dan membuat proses login menjadi lebih intuitif dan menarik.

Langkah 10: Styling Halaman Register
Pada langkah ini, saya akan memodifikasi berkas register.html di subdirektori main/templates/ untuk meningkatkan tampilan halaman pendaftaran aplikasi. Dengan menggunakan Tailwind CSS, saya akan menambahkan latar belakang gradien yang menarik, judul yang mencolok, serta formulir pendaftaran yang dinamis berdasarkan objek form yang diterima. Setiap input akan menampilkan label yang sesuai dan dapat memberikan umpan balik kesalahan jika ada. Selain itu, saya juga akan menyertakan tombol untuk mengirim formulir dan tautan untuk pengguna yang sudah memiliki akun agar dapat dengan mudah beralih ke halaman login. Tujuan dari modifikasi ini adalah untuk memberikan pengalaman pendaftaran yang intuitif dan estetis bagi pengguna baru.

Langkah 11: Styling Halaman Register
Dalam proyek ini, saya telah membuat halaman utama untuk aplikasi Mamio yang menggunakan template HTML untuk menampilkan informasi pengguna dan item entri. Saya membuat dua file template yaitu card_info.html dan item_card.html, yang berfungsi untuk menampilkan informasi pengguna seperti NPM, nama, dan kelas, serta item entri yang berisi detail tentang pesanan pengguna. Jika tidak ada item entri yang tersedia, kita menampilkan gambar untuk memberi tahu pengguna bahwa belum ada data item. Selain itu, tampilan halaman utama dimodifikasi agar lebih responsif dan menarik, dengan fitur untuk menambahkan item entri baru, sehingga pengguna dapat lebih mudah melacak kondisi pesanan mereka.

Langkah 12: Styling Halaman Create Item
Pada halaman create_item.html, saya mendesain form untuk membuat entri pesanan baru dalam aplikasi Mamio. Halaman ini menggunakan struktur HTML yang responsif dan menarik, termasuk elemen seperti judul yang jelas dan area untuk menginput data terkait pesanan pengguna. Form ini mengintegrasikan token CSRF untuk keamanan, serta menyediakan umpan balik untuk setiap field, seperti help text dan pesan kesalahan, agar pengguna dapat lebih mudah mengisi data. Tombol "Create Item Entry" yang terletak di bagian bawah form memungkinkan pengguna untuk mengirimkan data yang telah diisi. Dengan demikian, halaman ini berfungsi sebagai antarmuka pengguna untuk mencatat entri pesanan yang membantu melacak pesanan mereka di aplikasi Mamio.

Langkah 13: Styling Halaman Edit Item
Pada halaman edit_item.html, styling digunakan untuk meningkatkan tampilan dan kemudahan penggunaan saat mengedit item di aplikasi Mamio. Dengan latar belakang gradien dan teks berwarna menarik, halaman ini terlihat modern dan lebih jelas. Formulir ditempatkan dalam kotak dengan desain bersih, dan tombol interaktif memberikan respons visual yang memperkuat pengalaman pengguna secara keseluruhan.

Langkah 14: Membuat readme dan melakukan push ke pws
Pada tahap ini saya menjawab pertanyaan yang diminta pada soal ke dalam readme. Setelah saya selesai menjawab saya melakukan add, commit, dan push ke repositori GitHub menggunakan perintah git add ., git commit -m "<pesan_commit>", dan git push -u origin <branch_utama>. karena sebelumnya saya sudah membuat deploy.yml maka setiap kali melakukan add, commit, dan push ke github program juga akan otomatis di push ke pws. Setelah ini tampilan program dapat diakses orang lain melalui internet.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Tugas 6
1) Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

Jawab:

Penggunaan JavaScript dalam pengembangan aplikasi web memberikan berbagai manfaat yang signifikan. Sebagai bahasa pemrograman yang berjalan di sisi klien, JavaScript memungkinkan interaksi dinamis langsung pada halaman web tanpa perlu memuat ulang seluruh halaman, sehingga menciptakan pengalaman pengguna yang lebih responsif dan cepat. Dengan JavaScript, pengembang dapat mengimplementasikan berbagai fitur interaktif seperti validasi form, manipulasi elemen DOM, animasi, serta komunikasi asinkron melalui AJAX untuk memperbarui konten secara real-time tanpa mengganggu pengguna. JavaScript juga mendukung pengembangan aplikasi web berbasis komponen melalui framework dan pustaka seperti React, Vue, dan Angular, yang memudahkan pengelolaan kode secara modular dan scalable. Selain itu, JavaScript dapat dijalankan di server melalui Node.js, memberikan fleksibilitas pengembangan aplikasi full-stack dengan satu bahasa pemrograman yang seragam. Penggunaan JavaScript secara keseluruhan meningkatkan efisiensi pengembangan, memperkaya pengalaman pengguna, dan memungkinkan terciptanya aplikasi web yang lebih interaktif, dinamis, dan user-friendly.

2) Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

Jawab:

Penggunaan await dalam fungsi fetch() bertujuan untuk menunggu hingga proses pengambilan data dari server selesai sebelum kode berikutnya dieksekusi. Saat menggunakan await, eksekusi kode akan berhenti sementara pada titik tersebut sampai respons dari server diterima sepenuhnya, lalu hasilnya dapat langsung digunakan atau diproses lebih lanjut. Ini sangat bermanfaat dalam konteks penulisan kode asinkron, karena await menyederhanakan alur kontrol dengan menghilangkan kebutuhan untuk menangani Promise secara manual, sehingga membuat kode menjadi lebih mudah dipahami dan dikelola. Jika tidak menggunakan await, fungsi fetch() akan mengembalikan sebuah Promise yang masih dalam keadaan belum terselesaikan (pending), dan program akan terus melanjutkan eksekusi kode berikutnya tanpa menunggu hingga data dari server benar-benar diterima. Akibatnya, jika kode berikutnya membutuhkan data yang diambil melalui fetch(), ini bisa menyebabkan masalah, seperti error atau hasil yang tidak diinginkan, karena data yang diperlukan mungkin belum tersedia saat eksekusi dilanjutkan.

Selain itu, tanpa await, pengelolaan Promise memerlukan penggunaan metode .then() dan .catch() untuk menangani hasil yang diterima maupun kemungkinan error. Walaupun metode ini tetap berfungsi dengan baik, pendekatan ini dapat membuat kode lebih kompleks, terutama jika terdapat banyak operasi asinkron yang perlu dijalankan secara berurutan atau bergantung satu sama lain. Penanganan seperti itu bisa mengakibatkan kode yang berantakan dan lebih sulit dipelihara, karena semakin banyak .then() yang ditambahkan, semakin dalam struktur kode (yang sering disebut sebagai callback hell). Dengan await, kita dapat menulis kode seolah-olah bersifat sinkron, meskipun di balik layar tetap terjadi proses asinkron. Ini meningkatkan keterbacaan kode dan mengurangi potensi kesalahan yang mungkin muncul akibat manajemen Promise yang tidak tepat. Singkatnya, await membantu kita menulis kode yang lebih rapi, terstruktur, dan efisien, serta mengurangi kemungkinan munculnya error yang berhubungan dengan timing atau ketergantungan pada data yang belum sepenuhnya tersedia.

3) Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Jawab: 

Penggunaan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST dalam Django berfungsi untuk menonaktifkan perlindungan Cross-Site Request Forgery (CSRF) pada view tersebut. Secara default, Django menyediakan perlindungan CSRF untuk mencegah serangan berbahaya di mana seorang penyerang dapat mengelabui pengguna agar tanpa sadar mengirimkan permintaan yang tidak sah ke server. Serangan ini biasanya melibatkan eksploitasi sesi pengguna yang sudah terautentikasi untuk melakukan tindakan yang tidak diinginkan seperti mengubah data atau mengirimkan formulir atas nama pengguna tanpa sepengetahuan mereka. Dalam proses pengembangan aplikasi web, AJAX (Asynchronous JavaScript and XML) sering digunakan untuk mengirim permintaan POST secara dinamis ke server tanpa memuat ulang halaman. Namun, masalah umum yang terjadi adalah bahwa permintaan AJAX ini mungkin tidak secara otomatis menyertakan token CSRF yang dibutuhkan oleh Django untuk memvalidasi keabsahan permintaan. Jika permintaan tidak menyertakan token CSRF yang valid, Django secara default akan menolak permintaan tersebut dan memberikan respons berupa error "403 Forbidden."

Dengan menambahkan decorator csrf_exempt, Django akan melewati pemeriksaan token CSRF pada view tertentu. Hal ini memungkinkan permintaan AJAX POST untuk diproses tanpa memerlukan token CSRF. Hal ini juga memudahkan pengembangan ketika permintaan AJAX dilakukan, terutama jika token CSRF tidak ditambahkan secara manual dalam permintaan tersebut. Namun, penting untuk dicatat bahwa menonaktifkan perlindungan CSRF meningkatkan risiko keamanan, karena membuka pintu bagi potensi serangan CSRF. Oleh karena itu, penggunaan csrf_exempt harus dipertimbangkan dengan hati-hati. Idealnya, daripada menonaktifkan perlindungan CSRF, pengembang harus berusaha untuk mengirim token CSRF secara aman bersama dengan permintaan AJAX POST. Token ini dapat disertakan dalam header permintaan atau melalui input tersembunyi dalam formulir untuk memastikan keamanan tetap terjaga tanpa harus mengorbankan fungsionalitas.

4) Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Jawab:

Pembersihan data input pengguna yang dilakukan di belakang (backend) pada tutorial PBP minggu ini memiliki beberapa alasan penting terkait dengan keamanan, keandalan, dan integritas data aplikasi. Meskipun pembersihan data bisa dilakukan di frontend melalui JavaScript, CSS, atau HTML, praktik tersebut tidak cukup untuk menjamin keamanan aplikasi secara menyeluruh. Hal ini dikarenakan proses di frontend hanya berjalan di sisi pengguna (client-side), yang berarti kode dapat dengan mudah dimodifikasi atau diabaikan oleh pengguna atau pihak ketiga yang berniat jahat. Frontend adalah area yang lebih rentan terhadap serangan karena kode yang dieksekusi di browser dapat diakses dan dimanipulasi dengan mudah. Sebagai contoh, seorang penyerang dapat menghapus atau memodifikasi validasi dan pembersihan yang dilakukan di frontend menggunakan alat pengembang di browser atau dengan mengirimkan langsung permintaan HTTP melalui tools seperti Postman. Jika aplikasi hanya bergantung pada pembersihan dan validasi di frontend, maka input data berbahaya, seperti script injeksi, kode HTML, atau SQL injection, dapat masuk ke dalam sistem dan membahayakan integritas aplikasi.

Sementara itu, melakukan pembersihan data di backend memberikan kontrol penuh kepada pengembang untuk memastikan bahwa data yang diterima adalah bersih dan aman sebelum diproses atau disimpan di dalam database. Backend tidak dapat diakses langsung oleh pengguna, sehingga lebih aman dan terpercaya untuk memverifikasi dan memvalidasi semua data yang diterima dari pengguna. Misalnya, dengan menggunakan fungsi seperti strip_tags() di Django, data dapat dibersihkan dari potensi ancaman seperti injeksi kode HTML atau JavaScript yang bisa digunakan untuk melakukan serangan Cross-Site Scripting (XSS). Selain itu, pembersihan data di backend juga membantu menjaga konsistensi dan keandalan aplikasi. Data yang dimasukkan oleh pengguna bisa datang dari berbagai sumber dengan format yang berbeda, atau mungkin mengandung karakter yang tidak diinginkan. Oleh karena itu, backend memastikan bahwa data yang disimpan di database memenuhi format yang diharapkan, menghindari data yang korup atau tidak valid yang dapat mengakibatkan bug atau error di masa depan.

Kesimpulannya, meskipun pembersihan data di frontend memiliki manfaat dalam meningkatkan pengalaman pengguna dengan memberikan feedback cepat mengenai kesalahan input, pembersihan di backend tetap merupakan langkah krusial yang harus dilakukan untuk menjaga keamanan aplikasi, memastikan integritas data, dan melindungi dari potensi serangan berbahaya. Implementasi validasi dan pembersihan di kedua sisi, frontend dan backend, adalah praktik yang paling aman dan efektif dalam pengembangan aplikasi web.

5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Jawab:

Langkah 1: Menambahkan Pesan Error Pada Proses Login
Tahapan pertama yang perlu dilakukan adalah menambahkan pesan error untuk memudahkan pengguna saat proses login. Pada tahap ini, kita menambahkan conditional pada view login_user di file views.py. Sistem akan memeriksa apakah form yang diisi oleh pengguna valid menggunakan metode form.is_valid(). Jika valid, pengguna dapat login dengan sukses dan waktu login terakhir akan disimpan sebagai cookie. Namun, jika data yang dimasukkan tidak valid, seperti username atau password yang salah, kita perlu menampilkan pesan error agar pengguna memahami kesalahan yang terjadi dan dapat mencoba lagi. Pesan error ini akan ditambahkan ke dalam request dan ditampilkan di halaman login, sehingga memberikan informasi yang jelas kepada pengguna tentang kesalahan yang perlu diperbaiki. Dengan langkah ini, proses login menjadi lebih informatif dan ramah pengguna.

Langkah 2: Membuat Fungsi untuk Menambahkan Mood dengan AJAX
Langkah selanjutnya adalah membuat fungsi baru pada file views.py dengan nama add_item_entry_ajax. Fungsi ini bertujuan untuk menambahkan entri item baru ke dalam basis data melalui AJAX. Fungsi ini menerima parameter request, dan kita akan menggunakan data yang dikirimkan melalui POST request untuk membuat entri item baru. Pertama, kita akan mengambil data name, price, description, stock, category, dan rating dari request. Data tersebut kemudian akan diproses dan dikonversi sesuai dengan tipe datanya, seperti price dan stock yang dikonversi menjadi integer, serta rating menjadi float. Setelah itu, kita membuat objek Item baru berdasarkan data yang telah diterima, lalu menyimpannya ke dalam basis data dengan memanggil metode save(). Fungsi ini akan mengembalikan status HTTP 201 jika entri item berhasil dibuat.

Langkah 3: Menambahkan Routing Untuk Fungsi add_mood_entry_ajax
Setelah fungsi add_item_entry_ajax berhasil dibuat, langkah selanjutnya adalah menambahkan routing agar fungsi tersebut dapat diakses melalui URL. Buka file urls.py yang berada di dalam subdirektori main dan impor fungsi add_item_entry_ajax yang telah dibuat. Kemudian, tambahkan path URL baru ke dalam urlpatterns, sehingga pengguna dapat mengakses fungsi tersebut melalui URL yang ditentukan. Misalnya, dengan menambahkan path create-item-entry-ajax, pengguna dapat mengakses fungsi ini melalui URL tersebut, dan kita juga memberikan nama add_item_entry_ajax untuk path tersebut agar lebih mudah diidentifikasi dalam proyek.

Langkah 4: Menampilkan Data Mood Entry dengan fetch() API
Pada tahap ini, kita menghapus dua baris kode di file views.py yang mengambil objek item entry berdasarkan pengguna aktif. Langkah ini penting karena kita akan mendapatkan data item entry dari endpoint JSON, sehingga kode tersebut tidak lagi diperlukan. Selanjutnya, kita mengubah baris pertama di fungsi show_json dan show_xml untuk memastikan bahwa kita mendapatkan data item entry yang sesuai dengan pengguna yang sedang aktif, menjamin bahwa data yang ditampilkan relevan dan hanya untuk pengguna tersebut. Setelah itu, kita menghapus blok kondisi di main.html yang memeriksa apakah item entry kosong. Dengan menghapus bagian ini, tampilan yang tidak perlu ketika tidak ada data dapat dihindari, sehingga kita dapat beralih langsung untuk menampilkan data melalui fetch() API. Kita juga menambahkan elemen div baru yang berfungsi sebagai tempat untuk menampung semua kartu item entry yang akan dihasilkan berdasarkan data yang diambil dari API.

Selanjutnya, kita membuat fungsi getItemEntries untuk mengambil data item entry secara asinkron menggunakan fetch() API. Fungsi ini memungkinkan kita untuk mendapatkan data dari server tanpa perlu memuat ulang halaman, serta memberikan pengalaman pengguna yang lebih baik. Selain itu, kita membuat fungsi refreshItemEntries yang bertugas menyegarkan tampilan item entry secara asinkron. Dengan memanggil fungsi ini, kita dapat mengosongkan konten div dan memeriksa apakah ada data item entry yang tersedia. Jika tidak ada data, kita menampilkan pesan yang sesuai. jika ada, kita membuat tampilan kartu untuk setiap item entry yang ada. Pada tahap terakhir, kita memanggil fungsi refreshItemEntries saat halaman dimuat untuk memastikan data item entry ditampilkan secara otomatis. Dengan langkah-langkah ini, kita dapat menampilkan data item entry secara dinamis menggunakan fetch() API, memberikan interaksi yang lebih baik bagi pengguna.

Langkah 5: Membuat Modal Sebagai Form untuk Menambahkan Mood
Untuk membuat modal sebagai form untuk menambahkan produk, langkah pertama adalah menambahkan kode form yang diimplementasikan dengan menggunakan Tailwind CSS di bawah elemen div dengan ID item_entry_cards yang telah ditambahkan sebelumnya. Kode form ini akan menjadi antarmuka bagi pengguna untuk memasukkan detail produk yang ingin ditambahkan. Selanjutnya, agar modal berfungsi dengan baik, perlu ditambahkan dua fungsi JavaScript: showModal() untuk menampilkan modal ketika pengguna ingin menambahkan produk, dan hideModal() untuk menyembunyikan modal saat pengguna selesai atau membatalkan penambahan. Terakhir, tambahkan tombol baru yang akan memicu penambahan data menggunakan AJAX. Tombol ini memungkinkan pengguna untuk mengirimkan data form ke server tanpa perlu memuat ulang halaman, sehingga memberikan pengalaman pengguna yang lebih interaktif dan efisien. Dengan langkah-langkah ini, pengguna dapat dengan mudah menambahkan produk ke dalam aplikasi secara langsung melalui modal yang responsif.

Langkah 6: Menambahkan Data Item dengan AJAX
Modal dengan form yang telah dibuat sebelumnya belum bisa digunakan untuk menambahkan data item. Oleh karena itu, perlu dibuat fungsi JavaScript baru untuk menambahkan data berdasarkan input ke basis data secara AJAX. Pertama, buat fungsi baru dalam blok script dengan nama addItemEntry. Di dalam fungsi ini, gunakan new FormData(document.querySelector('#itemEntryForm')) untuk membuat objek FormData baru yang datanya diambil dari form pada modal. Objek FormData ini memungkinkan pengiriman data form ke server dengan mudah tanpa perlu melakukan reload halaman. Selain itu, gunakan document.getElementById("itemEntryForm").reset() untuk mengosongkan isi field form modal setelah data berhasil disubmit, sehingga form siap untuk digunakan lagi oleh pengguna.Selanjutnya, tambahkan sebuah event listener pada form yang ada di modal untuk menjalankan fungsi addItemEntry() saat form disubmit. Dengan langkah-langkah ini, pengguna dapat menambahkan item secara efisien ke dalam basis data melalui modal yang interaktif. Fungsi addItemEntry tidak hanya mempermudah proses penambahan data, tetapi juga meningkatkan pengalaman pengguna dengan memberikan feedback langsung tanpa mengganggu alur navigasi aplikasi.

Langkah 7: Melindungi Aplikasi dari Cross Site Scripting (XSS)
Untuk melindungi aplikasi dari serangan Cross Site Scripting (XSS), langkah pertama yang perlu dilakukan adalah menambahkan strip_tags untuk "membersihkan" data baru. Pertama, buka berkas views.py dan forms.py, kemudian tambahkan impor berikut: from django.utils.html import strip_tags. Pada fungsi add_item_entry_ajax, kita mendapatkan data dari request POST dan menggunakan strip_tags untuk membersihkan HTML tags dari setiap elemen data yang diterima. Ini termasuk data name, price, description, stock, category, dan rating. Dengan melakukan ini, kita memastikan bahwa tidak ada tag HTML yang berbahaya yang dapat menyebabkan masalah keamanan saat data tersebut disimpan ke dalam basis data. Sebagai contoh, untuk name, kita menggunakan name = strip_tags(request.POST.get("name")) agar hanya mengambil teks yang bersih dari tag HTML, sehingga mengurangi risiko injeksi skrip. Selain itu, dalam forms.py, kita harus menambahkan beberapa method untuk validasi data. Method clean_name(), clean_price(), clean_description(), clean_stock(), clean_category(), dan clean_rating() digunakan untuk memvalidasi dan membersihkan data sebelum diproses lebih lanjut. Setiap method akan dipanggil saat memanggil form.is_valid(). Misalnya, pada clean_price(), kita memastikan bahwa harga yang diterima tidak hanya dibersihkan dari tag HTML, tetapi juga diubah menjadi integer dengan return int(strip_tags(str(price))). Demikian juga untuk clean_stock() dan clean_rating(), kita melakukan konversi ke tipe data yang sesuai setelah membersihkannya. Dengan menerapkan langkah-langkah ini, kita dapat memastikan bahwa data yang diterima dari pengguna aman dan tidak mengandung konten yang dapat membahayakan aplikasi. Ini memberikan perlindungan tambahan terhadap potensi serangan XSS yang dapat merusak data dan integritas pengguna.

Langkah 8: Membersihkan Data dengan DOMPurify
Untuk meningkatkan keamanan aplikasi, kita dapat menggunakan library JavaScript bernama DOMPurify untuk membersihkan data di frontend. Pertama, kita perlu mengimpor DOMPurify ke dalam berkas main.html. Dengan mengimpor library ini, kita dapat membersihkan konten HTML yang berpotensi berbahaya, seperti tag HTML atau karakter yang tidak diinginkan. Selanjutnya, dalam fungsi refreshItemEntries, kita akan menambahkan langkah untuk membersihkan data sebelum ditampilkan. Dengan menggunakan metode dari DOMPurify, kita dapat memastikan bahwa setiap nilai dari nama, deskripsi, dan pairing yang diambil dari data bersih dari tag HTML atau skrip berbahaya. Ini sangat penting untuk mencegah serangan seperti Cross Site Scripting (XSS), di mana penyerang dapat mencoba memasukkan skrip berbahaya melalui input yang tidak terfilter. Setelah melakukan perubahan ini, ketika kita menyegarkan halaman utama aplikasi, jika sebelumnya ada data yang "kotor" yang menyebabkan masalah, seharusnya tidak ada lagi masalah tersebut setelah menerapkan DOMPurify. Dengan demikian, penggunaan DOMPurify tidak hanya meningkatkan keamanan aplikasi, tetapi juga memberikan pengalaman pengguna yang lebih baik dengan memastikan bahwa konten yang ditampilkan selalu aman dan bersih.

Langkah 9: Membuat readme dan melakukan push ke pws
Pada tahap ini saya menjawab pertanyaan yang diminta pada soal ke dalam readme. Setelah saya selesai menjawab saya melakukan add, commit, dan push ke repositori GitHub menggunakan perintah git add ., git commit -m "<pesan_commit>", dan git push -u origin <branch_utama>. karena sebelumnya saya sudah membuat deploy.yml maka setiap kali melakukan add, commit, dan push ke github program juga akan otomatis di push ke pws. Setelah ini tampilan program dapat diakses orang lain melalui internet.

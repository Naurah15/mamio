Nama : Naurah Iradya Kurniawan

NPM : 2306245900

Kelas : PBP B

1)  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Jawaban:

Data delivery memiliki peran yang sangat penting dalam memastikan bahwa data yang disimpan di server maupun database pusat dapat diakses oleh pengguna di berbagai lokasi secara efisien. Dalam proses pengembangan sebuah platform, data delivery menjadi elemen utama karena platform sering kali harus terhubung dan berinteraksi dengan berbagai layanan lain, seperti layanan basis data, cloud storage, atau sistem autentikasi dapat berfungsi dengan baik. selain itu, proses transfer dan penerimaan data melalui data delivery ini memastikan bahwa data yang diperlukan dapat dikirim dalam format yang tepat dan sesuai dengan kebutuhan spesifik.

Dengan adanya data delivery yang efektif, sistem yang berbeda dapat berkomunikasi secara lebih jelas dan terstruktur, sehingga mereka mampu bekerja sama secara optimal. Selain itu, data delivery yang andal berperan penting dalam menjaga keamanan dan memastikan akurasi data selama proses pertukaran antarplatform. Tanpa mekanisme data delivery yang efisien, komunikasi antar sistem bisa terganggu dan berpotensi menyebabkan kesalahan atau keterlambatan dalam penyampaian informasi. Dengan demikian, data delivery tidak hanya mendukung kinerja platform secara keseluruhan, tetapi juga meningkatkan kolaborasi antar layanan serta memastikan bahwa data tetap aman dan dapat diakses dengan akurat di seluruh sistem.

2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML

Jawaban:

Baik XML (eXtensible Markup Language) maupun JSON (JavaScript Object Notation) memiliki kegunaan dan kelebihan masing-masing, tetapi JSON lebih populer dalam banyak kasus karena beberapa alasan utama. 

JSON memiliki sintaksis yang lebih sederhana dan lebih mudah dibaca dibandingkan XML. JSON menggunakan format objek JavaScript yang langsung dikenali oleh banyak bahasa pemrograman, sedangkan XML memerlukan banyak tag dan atribut, yang dapat membuat struktur data menjadi lebih rumit.

Selain itu, JSON biasanya menghasilkan ukuran data yang lebih kecil dibandingkan XML. Ini disebabkan oleh fakta bahwa JSON tidak memerlukan tag penutup dan atribut tambahan yang ada di XML, sehingga lebih efisien dalam hal bandwidth dan penyimpanan.

Lalu, parsing dan penanganan JSON umumnya lebih cepat dibandingkan XML. Format JSON yang lebih sederhana dan tidak memerlukan parsing tag memungkinkan pemrosesan data yang lebih cepat. Selain itu, banyak bahasa pemrograman modern memiliki dukungan bawaan untuk parsing JSON, yang memudahkan penggunaannya dalam aplikasi web dan API.

Dan yang terakhir, JSON secara langsung kompatibel dengan JavaScript, yang membuatnya sangat populer dalam pengembangan web. Data JSON dapat dengan mudah diubah menjadi objek JavaScript, memudahkan integrasi dengan aplikasi web. Selain itu, JSON lebih baik dalam menangani struktur data yang kompleks dan mendalam berkat kemampuannya untuk menyimpan data dalam bentuk array dan objek.

Namun, XML juga memiliki kelebihan tersendiri. XML mendukung namespace, validasi schema, dan kemampuan untuk mendokumentasikan metadata secara lebih detail. Hal ini menjadikannya lebih cocok untuk beberapa aplikasi di mana struktur data dan validasi yang ketat diperlukan.

Secara keseluruhan, pemilihan antara XML dan JSON bergantung pada kebutuhan spesifik proyek dan preferensi teknis. Meskipun XML memiliki kelebihan dalam hal struktur dan validasi, JSON sering dipilih karena kemudahan penggunaan dan efisiensi yang lebih baik dalam konteks pengembangan web dan API modern.


3) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Jawaban:

Method is_valid() pada form djanggo berfungsi untuk memeriksa apakah data yang dikirim melalui form valid atau tidak. Saat pengguna mengisi form dan mengirimkan data method is_valid() akan otomatis memeriksa data tersebut untuk memastikan semuanya sesuai dengan aturan yang telah ditetapkan dalam form. Hal ini mencakup pengecekan tipe data serti angka, email, atau URL untuk memastikan semuanya benar sesuai dengan format yang telah ditetapkan. Jika data yang diterima valid maka method ini akan mengembalikan nilai true. Sebaliknya, jika tidak valid maka method ini akan mengembalikan nilai false. Dengan menggunakan method is_valid() pengembang tidak perlu membuat validasi secara manual untuk setiap input. Hal ini disebabkan karena pada method is_valid() sudah menangani semua bentuk validasi secara otomatis. Ini dapat mempermudah proses validasi dan mengurangi kemungkinan kesalahan dalam memeriksa data dari pengguna.

4) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Jawaban:

csrf_token digunakan untuk meningkatkan keamanan pada aplikasi djanggo. csrf_token memiliki bentuk nilai yang acak dan bersifat unik. Fungsi dari token ini adalah untuk memastikan bahwa setiap permintaan yang dikirim ke server benar-benar berasal dari pengguna yang sah (pengguna sebenarnya) bukan dari pihak yang mencoba memanfaatkan sesi yang sudah aktif untuk melakukan penyerangan. Token ini berfungsi sebagai lapisan perlindungan tambahan terhadap serangan Cross-Site Resquest Forgery (CSRF). 

Melalui token ini, server dapat melakukan validasi token. Pada saat server menerima data. Server akan melalukan pemeriksaan terhadap token. Server akan mengecek apakah token dalam form sesuai dengan token yang disimpan dalam sesi pengguna. Jika token tidak valid atau tidak ada maka server akan menolak permintaan tersebut. Hal ini dilakukan untuk melindungi aplikasi dari potensi serangan. 

csrf_token memiliki peranan penting dalam menjaga keamanan aplikasi. Tanpa adanya csrf_token aplikasi bisa menjadi target serangan CSRF, dimana penyerang dapat menyalahgunakan sesi yang sah untuk melakukan tindakan yang tidak diinginkan atas nama pengguna yang terautentikasi. 

Contoh penyerangan yang terjadi adalah penyerang bisa menyisipkan form berbahaya di situs mereka. Lalu pada saat pengguna yang sudah login mengunjungi situs tersebut form tersebut akan mengirimkan permintaan berbahaya tanpa sepengetahuan pengguna. Hal ini dapat mengakibatkan perubahan data atau pengambilan informasi pribadi.

5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban:

Langkah 1: Membuat direktori templates dan file HTML
Langkah ini berfungsi untuk menyiapkan struktur dasar tampilan aplikasi web. Dengan membuat direktori templates pada folder utama proyek dan file base.html dapat membangun kerangka umum yang akan digunakan untuk menyusun halaman-halaman web lainnya. Ini memastikan bahwa elemen-elemen seperti header, footer, dan layout konsisten pada seluruh aplikasi.

Langkah 2: Melakukan konfigurasi pengaturan pada settings.py dan menyusun main.html
Pada langkah ini, saya mengatur django untuk mengenali direktori templates dengan memperbarui settings.py khususnya pada bagian DIRS. Hal ini memastikan django dapat menemukan dan menggunakan template HTML yang telah dibuat. Kemudian saya juga menambahkan {% extends 'base.html' %} dan {% block content %} pada main.html.Hal ini berguna untuk menghubungkan template dengan base.html dan menentukan area dimana konsten spesifik ditampilkan.

Langkah 3: Menyiapkan model dan melakukan migrasi
Pada langkah ini saya melibatkan penambahan import uuid dalam models.py dan mendefinisikan model data, seperti item produk yang akan disimpan dalam database. Setelah mendefinisikan model saya melakukan migrasi untuk memperbarui skema database dengan perintah python manage.py makemigrations dan python manage.py migrate. hal ini memudahkan saya untuk menyimpan dan mengelola data produk dengan benar di database.

Langkah 4: Membuat form input data dan menampilkan item entry pada html
Pada langkah ini, saya membuat sebuah form input dengan membuat berkas forms.py yang berisi ModelForm untuk model ItemEntry. Di sini, saya mendefinisikan field yang akan digunakan dalam form, seperti name, price, dan description, stock, category, rating, dan discount yang nantinya digunakan untuk menangkap input data dari pengguna. Form ini memungkinkan saya untuk memproses dan menyimpan data baru ke dalam database dengan mudah. Selanjutnya, saya mengintegrasikan form tersebut dalam fungsi create_item pada views.py untuk menampilkan form dan menangani penyimpanan data. Setelah itu, saya memodifikasi template create_item.html agar form bisa diakses dan menambahkan fungsi validasi untuk memastikan data yang diinput valid sebelum disimpan ke database. Hal ini penting agar aplikasi dapat menerima entri baru dan menampilkannya dengan baik di halaman utama. Setlah tu saya melakukan perintah python manage.py runserver dan membuka http://localhost:8000/ Fungsi dari langkah ini adalah untuk menjalankan aplikasi Django di server lokal dan memastikan bahwa data yang ditambahkan melalui form dapat terlihat di halaman utama aplikasi saat diakses melalui browser.

Langkah 5: 







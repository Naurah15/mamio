Nama : Naurah Iradya Kurniawan

NPM : 2306245900

Kelas : PBP B

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

![alt text](<bagan pbp.png>)

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

5) Mengapa model pada Django disebut sebagai ORM?

Jawaban:

Model dalam Django disebut ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara objek dalam kode Python dan tabel di database relasional. ORM memungkinkan pengembang untuk mengelola dan bekerja dengan data menggunakan objek Python, tanpa perlu menulis query SQL secara manual. 

Dengan menggunakan ORM, pengembang bisa melakukan berbagai operasi pada data, seperti menambah, mengubah, atau menghapus data, hanya dengan menggunakan metode dan atribut objek di Python. Ini membuat pengembangan lebih efisien karena pengembang tidak perlu menulis perintah SQL yang rumit. Sebaliknya, ORM secara otomatis menerjemahkan operasi yang dilakukan pada objek Python menjadi perintah SQL yang sesuai dan menjalankannya di database. 

Dengan cara ini, ORM menyederhanakan interaksi dengan database dan memungkinkan pengembang untuk fokus pada pengembangan logika aplikasi tanpa harus memikirkan detail teknis dari SQL dan struktur database.





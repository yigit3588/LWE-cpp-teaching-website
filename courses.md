--1--

Degisken

1. degisken nedir

Değişkenler, programınızın hafızasında bilgileri saklamak için kullanılan adlardır. Programınız çalıştığı sürece, bu değişkenlere değerler atayabilirsiniz.Değişkenler bilgisayar programlarında bilgileri saklamak için kullanılan temel yapı taşlarıdır. Programlarınızın karmaşıklaştıkça, değişkenler daha fazla rol oynar ve programınızın işlevselliğini ve esnekliğini sağlar.

2. veri turleri

Bilgisayar programlarında farklı türde verileri temsil etmek için kullanılan yapısal öğelerdir. C++ gibi programlama dillerinde, çeşitli veri türleri bulunur.

1.Tam Sayılar (integers): Tam sayılar, kesirli olmayan pozitif veya negatif sayıları temsil eder. C++'da int anahtar kelimesiyle tanımlanır. Farklı boyutlarda tam sayılar için farklı türler bulunur: short, int, long. Kullanmak istedigimiz sayi kucuk ise short buyuk ise long kullanmamiz daha uygundur.

int tamSayi = 10;

2.Ondalık Sayılar (floating-point numbers): Ondalık sayılar, virgülle belirtilen sayıları temsil eder. C++'da float veya double anahtar kelimeleri kullanılarak tanımlanır. float daha düşük hassasiyet sunarken, double daha yüksek hassasiyet sunar.

float ondalikSayi = 3.14;

3.Karakterler (characters): Karakterler, tek bir karakteri temsil eder. C++'da char anahtar kelimesi kullanılarak tanımlanır. Tek tırnak içinde tek bir karakter tanımlanır. 

char karakter = 'A';

4.Boolean Değerler (boolean): Boolean değerler, doğru veya yanlış durumlarını temsil eder. C++'da bool anahtar kelimesiyle tanımlanır. Sadece iki değeri olabilir: true veya false. 

bool dogruMu = true;


3. degisken tanimlama ve isimlendirme kurallari 

Bir program içinde değişkenler tanımlanırken belirli kurallara uyulması gerekir.C++ programlama dilinde değişken tanımlama ve isimlendirme kurallarıni kisaca aciklamak gerekirse:

veri_türü değişken_adı = değer;

int sayi = 8;

Burada int, değişkenin veri türünü (integer) temsil eder. sayi, değişkenin adını temsil eder ve 8 değişkenin başlangıç değerini temsil eder.

Değişken İsimlendirme Kuralları:

Değişken isimleri, harf (a-z veya A-Z), rakam (0-9) veya alt çizgi (_) ile başlamalıdır.
Değişken isimleri, yalnızca harf, rakam ve alt çizgi içerebilir.
Değişken isimleri büyük-küçük harfe duyarlıdır. Yani degisken, Degisken ve DEGISKEN farklı değişkenlerdir.
C++ anahtar kelimeleri (örneğin int, float, while, for gibi) değişken adları olarak kullanılamaz.

4. degisken atama

 Bir değişkene değer atama, onun bellekteki değerini belirli bir veri ile değiştirme işlemidir. C++ programlama dilinde değişken atama işlemi birazdan gorulecegi uzere kolaydir.

ORNEK1
int sayi; // Değişken tanımlama
sayi = 10; // Değere atama

Bu örnekte, önce sayi adında bir tam sayı değişkeni tanımlıyoruz. Ardından, sayi değişkenine 10 değerini atıyoruz.

ORNEK2
int sayi = 20; // Değer atanarak değişken tanımlama

Burada, sayi değişkeni tanımlanırken aynı zamanda başlangıç değeri olarak 20 atanmıştır.

ORNEK3
int x = 5;
int y = x; // x'in değerini y'ye atama

Burada, x değişkeninin değeri y değişkenine atanmıştır. Bu işlem sonucunda, y değişkeninin değeri de 5 olacaktır.

Bir değişkenin değeri, başka bir değişkene atanırken veri türleri uyumlu olmalıdır. Mesela int veri tipini char veri tipine atarken donusum yapmak zorundasinizdir.

--2--

Operatorler

1. aritmatik operatorler

Aritmetik operatörler, matematiksel işlemleri gerçekleştirmek için kullanılır

1.Toplama (+): İki değeri toplamak için kullanılır.

int toplam = 5 + 3; // toplam = 8

2.Çıkarma (-): İki değeri birbirinden çıkarmak için kullanılır.

int fark = 7 - 4; // fark = 3

3.Çarpma (*): İki değeri çarpmak için kullanılır.

int carpim = 6 * 2; // carpim = 12

4.Bölme (/): Bir değeri diğerine bölmek için kullanılır. Tam sayı bölmesi yapılırsa, sonuç tam sayı olur.

float bolum = 10 / 3; // bolum = 3.33333 

5.Mod (%): Bir sayının diğerine bölümünden kalanı verir.

int kalan = 10 % 3; // kalan = 1

2. atama operatorleri

1.Basit Atama Operatörü (=): Değişkenin değerini bir ifadeye atamak için kullanılır.

int x = 5; // x'in değeri 5'e atanır

2.Toplama Atama Operatörü (+=): Bir değişkene belirtilen değeri eklemek için kullanılır.

int y = 10;
y += 3; // y'nin değeri 10 + 3 = 13 olur

3.Çıkarma Atama Operatörü (-=): Bir değişkenden belirtilen değeri çıkarmak için kullanılır.

int z = 8;
z -= 2; // z'nin değeri 8 - 2 = 6 olur

4.Çarpma Atama Operatörü (*=): Bir değişkeni belirtilen değerle çarpmak için kullanılır.

int a = 4;
a *= 3; // a'nın değeri 4 * 3 = 12 olur

5.Bölme Atama Operatörü (/=): Bir değişkeni belirtilen değere bölmek için kullanılır.

int b = 16;
b /= 4; // b'nin değeri 16 / 4 = 4 olur

6.Mod Atama Operatörü (%=): Bir değişkeni belirtilen değere bölmek ve kalanı atamak için kullanılır.

int c = 17;
c %= 5; // c'nin değeri 17 % 5 = 2 olur

3. karsilastirma operatorleri

Karşılaştırma operatörleri, iki değeri karşılaştırmak ve sonucuna göre bir koşulu değerlendirmek için kullanılır. Bu operatörler, programlamada oldukça yaygın olarak kullanılır ve birçok durumda işlerinizi kolaylaştırır.

1.Eşitlik (==): İki değer birbirine eşitse, ifade doğrudur

2.Eşit Değil (!=): İki değer birbirine eşit değilse, ifade doğrudur.

3.Büyüktür (>): Sol taraftaki değer, sağ taraftaki değerden büyükse, ifade doğrudur.

4.Küçüktür (<): Sol taraftaki değer, sağ taraftaki değerden küçükse, ifade doğrudur.

5.Büyük Eşit (>=): Sol taraftaki değer, sağ taraftaki değerden büyük veya eşitse, ifade doğrudur. 

Küçük Eşit (<=): Sol taraftaki değer, sağ taraftaki değerden küçük veya eşitse, ifade doğrudur. 




5. arttirma ve azaltma operatorleri

Artırma (++) ve Azaltma (--) Operatörleri: Bir değişkenin değerini bir artırmak veya azaltmak için kullanılır.

int x = 5;
x++; // x'in değeri 6 olur
int y = 10;
y--; // y'nin değeri 9 olur


--3--

1. Getting a value from the user and printing this value to the screen.

1.Kullanıcıdan Değer Alma:
    Kullanıcıdan değer almak için std::cin kullanılır. Bu, C++'ın standart giriş akışıdır ve genellikle klavyeden girdi almak için kullanılır.
    İlk adımda, değeri almak için bir değişken tanımlamamız gerekiyor.
    Daha sonra, kullanıcıdan alınacak değeri istemek için std::cout kullanılır.
    Kullanıcıdan gelen değeri std::cin ile değişkenimize atarız.
2.Ekrana Değer Yazdırma:
    Kullanıcıdan aldığımız değeri ekrana yazdırmak için std::cout kullanılır.
    Değişkenin değeri ekrana yazdırılırken, << operatörü kullanılır.

Bu islemleri yapmak icin <iostream> kutuphanesini eklememiz gerektigini lutfen unutmayalim

örnek bir C++ programı

#include <iostream>

int main() {
    // 1. Kullanıcıdan bir tam sayı değeri almak için
    int sayi;
    std::cout << "Lutfen bir tam sayi giriniz: "; // Kullanıcıdan girdiyi iste
    std::cin >> sayi; // Kullanıcının girdiği değeri 'sayi' değişkenine ata

    // 2. Kullanıcının girdiği değeri ekrana yazdırmak için
    std::cout << "Girdiginiz sayi: " << sayi << std::endl; // 'sayi' değişkeninin değerini ekrana yazdır

    return 0;
}


--4--

Kosullar

1. if else kosulu

C++ programlamasında belirli bir koşulun doğru veya yanlış olmasına bağlı olarak farklı işlemlerin yapılmasını sağlar. Bu yapı, programın akışını kontrol etmek için kullanılır. if-else koşulunun temel yapısı:

if (koşul) {
    // Koşul doğruysa buradaki işlemler yapılır
} else {
    // Koşul yanlışsa buradaki işlemler yapılır
}

if (koşul): İlk olarak, belirli bir koşul belirtilir. Eğer bu koşul doğruysa, if bloğu içindeki işlemler yapılır. Koşul yanlışsa, if bloğu atlanır ve else bloğu kontrol edilir.
else: İf bloğu içindeki koşul yanlışsa, else bloğu içindeki işlemler yapılır. Bu blok opsiyoneldir ve koşul doğruysa atlanır.

#include <iostream>

int main() {
    int sayi;
    std::cout << "Bir sayi giriniz: ";
    std::cin >> sayi;

    if (sayi > 0) {
        std::cout << "Girdiginiz sayi pozitif." << std::endl;
    } else {
        std::cout << "Girdiginiz sayi negatif veya sifir." << std::endl;
    }

    return 0;
}

2. switch case

 bir koşulun farklı değerlere göre dallanmasını sağlayan bir kontrol yapısıdır. switch-case yapısı, bir if-else ifadesinin alternatif bir gösterimidir. Genellikle bir değişkenin farklı değerlerine göre farklı işlemler yapılması gerektiğinde kullanılır.

 switch (ifade) {
    case deger1:
        // ifade deger1'e eşitse bu blok çalışır
        break;
    case deger2:
        // ifade deger2'ye eşitse bu blok çalışır
        break;
    // Diğer case ifadeleri buraya eklenebilir
    default:
        // Yukarıdaki hiçbir case ifadesine uymadığında bu blok çalışır
}


switch (ifade): Kontrol edilecek ifade belirtilir. Bu ifade genellikle bir değişkenin değeridir.
case deger1: ifade deger1'e eşitse, bu blok çalışır.
case deger2: ifade deger2'ye eşitse, bu blok çalışır.
default: Yukarıdaki hiçbir case ifadesine uymadığında, yani ifade herhangi bir değere eşit değilse, bu blok çalışır. default bloku opsiyoneldir.
break: Her case bloğunun sonunda bulunur ve switch-case yapısından çıkışı sağlar. break ifadesi olmadan devam edilirse, altındaki case blokları da çalıştırılır.

#include <iostream>

int main() {
    int sayi;
    std::cout << "Bir sayi giriniz: ";
    std::cin >> sayi;

    switch (sayi) {
        case 1:
            std::cout << "Girdiginiz sayi 1'e esit." << std::endl;
            break;
        case 2:
            std::cout << "Girdiginiz sayi 2'ye esit." << std::endl;
            break;
        case 3:
            std::cout << "Girdiginiz sayi 3'e esit." << std::endl;
            break;
        default:
            std::cout << "Girdiginiz sayi 1, 2 veya 3'e esit degil." << std::endl;
            break;
    }

    return 0;
}



3. mantiksal operetolerin kosullarda kullanimi

Koşulların ve ifadelerin doğruluğunu değerlendirmek için kullanılır. 

1.Ve (&&): Her iki koşul da doğruysa, ifade doğrudur. Aksi halde, ifade yanlıştır.

int x = 5;
int y = 10;
if (x > 0 && y < 20) {
    // Bu koşul doğrudur, çünkü her iki koşul da doğrudur.
}

2.Veya (||): En az bir koşul doğruysa, ifade doğrudur. Her iki koşul yanlışsa, ifade yanlıştır.

int a = 3;
int b = 7;
if (a == 3 || b == 5) {
    // Bu koşul doğrudur, çünkü a'nın değeri 3'tür.
}

3.Değil (!): Koşulun tersini alır. Doğruysa yanlış yapar, yanlışsa doğru yapar.

int c = 8;
if (!(c < 5)) {
    // Bu koşul doğrudur, çünkü c'nin değeri 5'ten küçük değildir.
}

4. ic ice if(nested)

İç içe if ifadeleri veya nested if ifadeleri, bir if bloğunun içinde başka bir if bloğunun kullanılmasıdır. Bu yapı, belirli koşulların birden fazla seviyesini kontrol etmek için kullanılır. İç içe if ifadeleri genellikle daha karmaşık koşulların kontrol edilmesi gereken durumlarda kullanılır. temel yapısı su sekildedir :

if (koşul1) {
    // Koşul1 doğruysa bu blok çalışır
    if (koşul2) {
        // Koşul1 ve Koşul2 doğruysa bu blok çalışır
        // İşlemler
    }
    else {
        // Koşul1 doğru, ancak Koşul2 yanlışsa bu blok çalışır
        // İşlemler
    }
}
else {
    // Koşul1 yanlışsa bu blok çalışır
    // İşlemler
}


Bu yapıda, bir if ifadesi içinde başka bir if ifadesi kullanılmıştır. İlk if bloğu (dıştaki if bloğu) bir koşulu kontrol eder. Eğer bu koşul doğruysa, içteki if bloğu çalıştırılır ve içteki if bloğunda başka bir koşul kontrol edilir. İçteki if bloğu, dıştaki if bloğunun koşuluna bağlı olarak çalışabilir veya çalışmayabilir.

#include <iostream>

int main() {
    int notu;
    std::cout << "Notunuzu giriniz: ";
    std::cin >> notu;

    if (notu >= 0 && notu <= 100) { // Notun geçerli aralıkta olup olmadığını kontrol et
        if (notu >= 90) {
            std::cout << "Notunuz: A" << std::endl;
        } else if (notu >= 80) {
            std::cout << "Notunuz: B" << std::endl;
        } else if (notu >= 70) {
            std::cout << "Notunuz: C" << std::endl;
        } else if (notu >= 60) {
            std::cout << "Notunuz: D" << std::endl;
        } else {
            std::cout << "Notunuz: F" << std::endl;
        }
    } else {
        std::cout << "Geçersiz not girildi." << std::endl;
    }

    return 0;
}


-------------------------- -------------------------------- ------------- -------------------------- --------------------------------

--5--

donguler

1. for dongusu

for döngüsü, belirli bir işlemi belirli bir sayıda veya belirli bir aralıkta tekrarlamak için kullanılan bir döngü yapısıdır. For döngüsü, bir döngü değişkenini başlatmak, bir koşulu kontrol etmek ve bir artırma/azaltma ifadesi kullanarak döngüyü güncellemek için kullanışlı ve okunaklı bir yapının sunulmasını sağlar. Bu, belirli bir işlemi belirli bir sayıda tekrar etmek istediğinizde çok kullanışlı olabilir.temel yapi su sekildedir : 

for (başlangıç değeri; koşul; artırma/azaltma) {
    // Döngü gövdesi: Her iterasyonda yapılacak işlemler
}

for döngüsü, belirli bir işlemi belirli bir sayıda veya belirli bir aralıkta tekrarlamak için kullanılan bir döngü yapısıdır.

başlangıç değeri: Döngünün başlangıç değeridir. Döngü başlamadan önce sadece bir kez çalışır.
koşul: Her iterasyonda kontrol edilen bir koşuldur. Bu koşul doğru olduğu sürece döngü devam eder. Koşul yanlış olduğunda döngü sona erer.
artırma/azaltma: Döngünün her iterasyonunda kullanılan bir artırma veya azaltma ifadesidir. Bu ifade, döngü değişkeninin değerini güncellemek için kullanılır.

#include <iostream>

int main() {
    // 0'dan 4'e kadar olan sayıları ekrana yazdıralım
    for (int i = 0; i < 5; ++i) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}

Bu örnekte, i değişkeni başlangıçta 0 değerini alır. Döngü, i değişkeni 5'ten küçük olduğu sürece çalışır. Her iterasyonda i değişkeni bir artırılır (++i). Döngü gövdesi içinde, her iterasyonda i değeri ekrana yazdırılır. Sonuç olarak, 0'dan 4'e kadar olan sayılar ekrana yazdırılır.

2. while dongusu

While döngüsü, belirli bir koşul doğru olduğu sürece bir işlemi tekrarlamak için kullanılan bir döngü yapısıdır. While döngüsü, başlangıçta koşulu kontrol eder ve koşul doğru olduğu sürece döngü gövdesini tekrar tekrar çalıştırır. While döngüsü, bir döngü gövdesini belirli bir koşula bağlı olarak tekrar etmek istediğinizde kullanışlıdır. Koşul herhangi bir zamanda yanlış olursa, döngü sona erer ve döngüden çıkılır. Bu nedenle, koşulun her zaman doğru olduğundan emin olmalısınız, aksi takdirde sonsuz döngü oluşabilir. Temel yapisi boyledir : 

while (koşul) {
    // Döngü gövdesi: Koşul doğru olduğu sürece çalışacak işlemler
}

#include <iostream>

int main() {
    int sayac = 0;

    // Sayac değeri 5'ten küçük olduğu sürece döngüyü çalıştır
    while (sayac < 5) {
        std::cout << "Sayac degeri: " << sayac << std::endl;
        sayac++; // Her iterasyonda sayac değerini artır
    }

    return 0;
}

Bu örnekte, sayac değişkeni başlangıçta 0 değerini alır. While döngüsü, sayac değişkeni 5'ten küçük olduğu sürece çalışır. Her iterasyonda sayac değeri ekrana yazdırılır ve sonra bir artırılır. Sonuç olarak, döngü 0'dan 4'e kadar olan sayıları ekrana yazdırır.

3. do while dongusu

Do-while döngüsü, while döngüsüne benzer, ancak döngü gövdesi en az bir kez çalıştırılır ve daha sonra koşul kontrol edilir. Bu nedenle, do-while döngüsü, bir işlemi en az bir kez gerçekleştirmek istediğinizde kullanışlıdır. Do-while döngüsü, bir döngü gövdesinin en az bir kez çalışmasını sağlamak istediğinizde kullanışlıdır. Do-while döngüsü, while döngüsünden farklı olarak, koşulun döngü gövdesinden önce kontrol edilmesi gerektiği durumlarda tercih edilir.

do {
    // Döngü gövdesi: Koşul kontrol edilmeden önce çalışacak işlemler
} while (koşul);


#include <iostream>

int main() {
    int sayac = 0;

    // Sayac değeri 5'ten küçük olduğu sürece döngüyü çalıştır
    do {
        std::cout << "Sayac degeri: " << sayac << std::endl;
        sayac++; // Her iterasyonda sayac değerini artır
    } while (sayac < 5);

    return 0;
}

Bu örnekte, sayac değişkeni başlangıçta 0 değerini alır. Do-while döngüsü, döngü gövdesini (burada sadece ekrana bir değer yazdırmak) en az bir kez çalıştırır ve sonra sayac değişkeninin değeri 5'ten küçük olduğu sürece döngüyü tekrarlar. Her iterasyonda sayac değeri ekrana yazdırılır ve sonra bir artırılır. Sonuç olarak, döngü 0'dan 4'e kadar olan sayıları ekrana yazdırır.

--6--

temel veri yapilari

1. dizilerin tanimi ve kullanimi

diziler C++ programlamasında birden fazla veri öğesini saklamak için kullanılan veri yapılarından biridir. Bir dizi, aynı türden birden fazla veriyi tek bir değişkende saklamak için kullanılır. Her bir öğe, dizi içinde bir indis (index) numarasıyla erişilebilir.

Dizilerin Tanımı:
Dizi tanımı, dizi türü, dizi adı ve dizi boyutuyla yapılır. Örneğin, int türünde 5 elemanlık bir dizi şu şekilde tanımlanır:
int dizi[5]; // 5 elemanlık bir tamsayı dizisi, Bu tanım, dizi adında bir dizi oluşturur ve 5 tamsayı değeri saklar.

Dizilerin Kullanımı:
Diziye erişmek için indis kullanılır. İndisler 0'dan başlar ve dizinin boyutu eksi bir birimine kadar olan sayılarla sıralanır. Örneğin, yukarıda tanımlanan diziye erişmek için şu şekilde kullanılır:

dizi[0] = 10; // Dizinin ilk elemanına 10 değerini atar
dizi[1] = 20; // Dizinin ikinci elemanına 20 değerini atar

Dizinin elemanlarına erişmek ve kullanmak için indisler kullanılır. Örneğin, bir döngü kullanarak dizinin elemanlarını ekrana yazdırmak için şu şekilde yapılabilir:

for (int i = 0; i < 5; ++i) {
    std::cout << "dizi[" << i << "] = " << dizi[i] << std::endl;
}

Bu döngü, dizinin her bir elemanını i indisini kullanarak sırayla ekrana yazdırır.

İnitialization:
Dizileri tanımladıktan sonra, aynı anda başlangıç değerleri ile de initialize edebilirsiniz:

int dizi[5] = {10, 20, 30, 40, 50}; // Dizi tanımı ve başlangıç değerleri

Diziler, aynı türde birden fazla veriyi tutmak için kullanışlıdır. Ancak, bir dizi tanımlandıktan sonra boyutu değiştirilemez, yani bir dizi oluşturulduktan sonra eleman sayısı değiştirilemez.



2. string veri turu ve kullanimi


String, metin verilerini temsil etmek için kullanılan bir veri türüdür. C++'ta string veri türü, karakter dizilerini daha kolay ve esnek bir şekilde işlemek için kullanılır. String veri türü, <string> başlık dosyasında tanımlanmıştır.

String'in Tanımı:
String bir dizi gibi düşünülebilir, ancak karakterlerden oluşur. Bir string tanımlamak için, string türü ile bir değişken adı kullanılır.

#include <string>

std::string isim = "Ahmet";

Yukarıdaki örnekte, isim adında bir string değişkeni tanımlanmış ve "Ahmet" değeri ile başlatılmıştır.

String Kullanımı:
String değişkenlerine karakter dizilerini atamak veya diğer string değişkenlerine atamak için basit atama operatörü (=) kullanılabilir. Ayrıca, stringler arasında artırma ve azaltma işlemleri gerçekleştirilebilir.

std::string ad = "Mehmet";
std::string soyad = "Yılmaz";
std::string tamIsim = ad + " " + soyad; // İki stringi birleştirme

String Uzunluğu:
Stringin uzunluğunu öğrenmek için length() veya size() fonksiyonları kullanılabilir.

std::string metin = "Merhaba Dunya";
int uzunluk = metin.length(); // veya metin.size();

String Girişi ve Çıktısı:
Kullanıcıdan string girişi almak için std::cin kullanılır. String çıktısı için ise std::cout kullanılır.

#include <iostream>
#include <string>

int main() {
    std::string ad;
    std::cout << "Adinizi giriniz: ";
    std::cin >> ad;

    std::cout << "Merhaba, " << ad << "!" << std::endl;

    return 0;
}

String, metin verilerini işlemek için çok kullanışlı bir veri türüdür. C++'ta string veri türü sayesinde, metinlerle ilgili birçok işlemi kolayca gerçekleştirebilirsiniz. Stringin bir cok fonksiyonu vardir ve bunlari zamanla ogreniceksiniz. Daha detayli ogrenmek icin c++ in kendi resmi sitesinden bakmaniz onerilir.

3. dizilerde islemler (erisim-ekleme-silme vs )

1.Erişim (Access):
Dizilerde belirli bir indis kullanılarak değerlere erişilir.

int dizi[5] = {10, 20, 30, 40, 50};
int deger = dizi[2]; // dizi[2], 30 değerini içerir

2.Ekleme (Insertion):
Dizilere değer eklemek, mevcut değerlerin üzerine yazmayı gerektirir. Yeni bir eleman eklemek için genellikle yeni bir dizi oluşturulur ve mevcut elemanlar yeni diziye kopyalanır, ardından yeni elemanlar eklenir.

#include <iostream>

int main() {
    int dizi[5] = {10, 20, 30, 40, 50};
    int yeniDizi[6]; // Yeni bir dizi oluştur

    // Mevcut diziyi yeni diziye kopyala
    for (int i = 0; i < 5; ++i) {
        yeniDizi[i] = dizi[i];
    }

    // Yeni elemanı ekle
    yeniDizi[5] = 60;

    // Yeni diziyi ekrana yazdır
    for (int i = 0; i < 6; ++i) {
        std::cout << yeniDizi[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}


3.Silme (Deletion):
Dizilerde belirli bir elemanı silmek, o elemanın diziden çıkarılmasını gerektirir. Bu genellikle yeni bir dizi oluşturarak yapılır; silmek istediğiniz elemanı atlamak suretiyle yeni dizi oluşturulur.

#include <iostream>

int main() {
    int dizi[5] = {10, 20, 30, 40, 50};
    int yeniDizi[4]; // Yeni bir dizi oluştur

    // Mevcut diziyi yeni diziye kopyala (silinecek elemanı atlayarak)
    for (int i = 0, j = 0; i < 5; ++i) {
        if (i != 2) { // 2. indis dışındaki elemanları kopyala
            yeniDizi[j++] = dizi[i];
        }
    }

    // Yeni diziyi ekrana yazdır
    for (int i = 0; i < 4; ++i) {
        std::cout << yeniDizi[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}


4. stringlerde islemler (erisim-ekleme-silme vs )

1.Erişim (Access):
Stringlerde, karakter dizilerinde olduğu gibi, belirli bir indeks kullanılarak karakterlere erişilir.

std::string metin = "Merhaba";
char karakter = metin[2]; // karakter, 'r' değerini içerir


2.Ekleme (Insertion):
Stringlere yeni karakterler eklemek için + operatörü kullanılır veya append() fonksiyonu kullanılabilir.

std::string metin = "Merhaba";
metin += " Dunya"; // metin, "Merhaba Dunya" olur
metin.append("!"); // metin, "Merhaba Dunya!" olur


3.Silme (Deletion):
Stringlerden karakterleri veya bir alt dizesi silmek için erase() fonksiyonu kullanılır.

std::string metin = "Merhaba Dunya!";
metin.erase(3, 3); // 3. indisten başlayarak 3 karakter siler: "haba Dunya!"




--7--

fonksiyonlar

1. fonksiyonun tanimi ve islevi

2. fonksiyon parametreleri ve argumanlar

3. fonksiyon cagirma ve geri donus degeri

















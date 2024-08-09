# NLP - DEVS Teknofest 2024 TDDİ Repository
Bu proje, Technofest 2024 Türkçe Doğal Dil İşleme Yarışması kapsamında NLP-Devs takımı tarafından geliştirilmiştir. Büyük dil modellerini kullanarak ürün yorumlarını analiz etmek ve sınıflandırmak amacıyla oluşturulan bu sistem, dilin yapısını ve anlamını derinlemesine anlayarak verilerden anlamlı bilgiler çıkarmayı amaçlar.

## Genel Bakış
Bu proje, dilin yapısını ve anlamını anlamak için gelişmiş doğal dil işleme (NLP) tekniklerini kullanır. Ürün yorumlarının genel duygularını ve tematik ayrıntılarını analiz ederken, büyük dil modellerinin gücünden faydalanır. Flask ile geliştirilen arka uç, yorum analizi ve sınıflandırma için API uç noktaları sunarken, Streamlit ile geliştirilen ön uç, kullanıcıların yorumları göndermelerini ve analiz sonuçlarını görüntülemelerini sağlar.

## Ana Özellikler
1. Ürün Analizi: Ürün yorumlarının genel duygularını ve tematik ayrımlarını NLP kullanarak analiz eder.
2. Yorum Sınıflandırma: Bireysel yorumları önceden tanımlanmış kategorilere ve duygulara göre sınıflandırır.
3. Etkileşimli Kullanıcı Arayüzü: Streamlit tabanlı kullanıcı arayüzü, analiz araçlarıyla gerçek zamanlı etkileşim sunar.

## Sistem Mimarisi
Sistem, iki ana bileşenden oluşur:

1. Flask API Sunucusu: Modelleri barındırır ve yorum analizi için API isteklerini işler.
2. Streamlit Kullanıcı Arayüzü: Kullanıcılara yorumları girme ve analiz sonuçlarını görüntüleme imkanı sunar.

## Kullanılan Teknolojiler
- Flask - API sunucusu oluşturmak için web çerçevesi.
- Streamlit - Kullanıcı arayüzü oluşturmak için kullanılan çerçeve.
- LangChain - Büyük dil modellerini entegre etmek için kullanılır.
- OpenAI - İsteklerin bulut ortamında işlenmesi için.
- Pydantic - Reinforcement Learning implementasyonu için
- Instructor - Büyük Dil Modellerinin çıktılarını formatlamak için.
- Requests - Streamlit'te HTTP isteklerini yönetmek için kullanılır.

## Kurulum Talimatları
### Gereksinimler
- Python 3.8+
- pip

## Kurulum
### Repo'yu Klonlama
- git clone ayhannbozkurt/NLP-DEVS1
- cd your-project-directory

### Gerekli Bağımlılıkları Kurma
- pip install -r requirements.txt

### FLASK API' Çalıştırma 
- flask run (Dosya yolunuzun içerisinde terminale yazmanız gerekmektedir.)

### Streamlit Arayüzü Çalıştırma
- streamlit run st.py

## Arayüzü Test Etme
Her şeyi doğru şekilde kurduktan ve çalıştırdıktan sonra, web tarayıcınızı kullanarak Flask API ve Streamlit arayüzünün çalışıp çalışmadığını kontrol edebilirsiniz. API ve arayüz düzgün çalışıyorsa, projenizle etkileşime geçebilir ve ürün yorumlarını analiz edebilirsiniz.

import streamlit as st
import requests

# Streamlit App Title
st.title("Product Evaluation")

# Input field for user question
question = 'Ürünle ilgili tüm yorumları analiz et ve ürünün genel bir değerlendirmesini yap.'

review = st.text_area("Ürün linkini giriniz:", "")

# Button to submit the question
if st.button("Evaluate"):
    if review == "https://www.hepsiburada.com/los-ojos-kadin-lavanta-yuksek-bel-jogger-esofman-alti-joggers-p-HBCV00000ZUIPT":
        csv_file_path = "reviews1.csv"  # "bardak" için özel CSV dosyası
    else:
        csv_file_path = "samplereview.csv"  # Diğer sorular için genel CSV dosyası

    try:
        response = requests.post(
            "http://localhost:5000/analyze_product",
            json={"question": question, "csv_file_path": csv_file_path}
        )
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print(data)
            st.subheader("Response:")
            st.write(data.get('response', 'No response received'))
        else:
            st.error(f"Error fetching response from API. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        
        

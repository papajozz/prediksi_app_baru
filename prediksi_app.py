import streamlit as st
import pandas as pd
from joblib import load

# Memuat model
model_rf = load('random_forest_model.joblib')

# Judul aplikasi
st.title("Prediksi Tingkat Keparahan Kecelakaan")

# Pemetaan kategori ke angka untuk fitur kategorikal
kategori_mapping_tipe_tabrakan = {
    'Tabrakan Tunggal': 0,
    'Tabrakan Depan-Depan': 1,
    'Tabrakan Depan Samping': 2,
    'Tabrakan Depan Belakang': 3,
    'Tabrakan Samping Samping': 4,
    'Tabrakan Sudut': 5,
    'Tabrak Manusia': 6,
    'Tabrak Hewan': 7,
    'Tabrak Lari': 8,
    'Lainnya': 9,
    'Belum Diketahui': 10
}

kategori_mapping_klasifikasi_jalan = {
    'Arteri': 0,
    'Kolektor': 1,
    'Lokal': 2,
    'Lingkungan': 3,
    'Belum Diketahui': 4
}

kategori_mapping_kelas_jalan = {
    'I': 0,
    'II': 1,
    'IIIA': 2,
    'IIIB': 3,
    'IIIC': 4,
    'Belum Diketahui': 5
}

kategori_mapping_status_administratif_jalan = {
    'Nasional': 0,
    'Provinsi': 1,
    'Kabupaten': 2,
    'Kota': 3,
    'Desa': 4,
    'Belum Diketahui': 5
}

kategori_mapping_jenis_kawasan = {
    'Perumahan': 0,
    'Pertokoan': 1,
    'Pasar': 2,
    'Hiburan': 3,
    'Daerah Wisata': 4,
    'Lainnya': 5,
    'Belum Diketahui': 6
}

kategori_mapping_bentuk_jalan = {
    'Lurus': 0,
    'X': 1,
    'Y': 2,
    'T': 3,
    'Tikungan': 4,
    'Bundaran': 5,
    'Lintasan KA': 6,
    'Lainnya': 7,
    'Belum Diketahui': 8
}

kategori_mapping_jenis_gangguan_jalan = {
    'Berlubang': 0,
    'Kurang Penerangan': 1,
    'Licin': 2,
    'Marka Rusak': 3,
    'Pandangan Terhalang': 4,
    'Rambu Rusak': 5,
    'Rusak': 6,
    'Tidak Ada Marka': 7,
    'Tidak Ada Rambu': 8,
    'Tikungan Tajam': 9,
    'Lainnya': 10,
    'Belum Diketahui': 11
}

kategori_mapping_kondisi_cuaca = {
    'Cerah': 1,
    'Berawan': 2,
    'Hujan Ringan': 3,
    'Hujan Lebat': 4
}

kategori_mapping_jam_kejadian = {
    '00:00 - 03:00': 0,
    '03:00 - 06:00': 1,
    '06:00 - 09:00': 2,
    '09:00 - 12:00': 3,
    '12:00 - 15:00': 4,
    '15:00 - 18:00': 5,
    '18:00 - 21:00': 6,
    '21:00 - 00:00': 7,
    'Belum Diketahui': 8
}

# Form input untuk fitur-fitur
tipe_tabrakan = st.selectbox(
    'Pilih Tipe Tabrakan',
    ['Tabrakan Tunggal', 'Tabrakan Depan-Depan', 'Tabrakan Depan Samping', 'Tabrakan Depan Belakang', 
     'Tabrakan Samping Samping', 'Tabrakan Sudut', 'Tabrak Manusia', 'Tabrak Hewan', 'Tabrak Lari', 
     'Lainnya', 'Belum Diketahui']
)

klasifikasi_fungsi_jalan = st.selectbox(
    'Pilih Klasifikasi Fungsi Jalan',
    ['Arteri', 'Kolektor', 'Lokal', 'Lingkungan', 'Belum Diketahui']
)

kelas_jalan = st.selectbox(
    'Pilih Kelas Jalan',
    ['I', 'II', 'IIIA', 'IIIB', 'IIIC', 'Belum Diketahui']
)

status_administratif_jalan = st.selectbox(
    'Pilih Status Administratif Jalan',
    ['Nasional', 'Provinsi', 'Kabupaten', 'Kota', 'Desa', 'Belum Diketahui']
)

jenis_kawasan = st.selectbox(
    'Pilih Jenis Kawasan',
    ['Perumahan', 'Pertokoan', 'Pasar', 'Hiburan', 'Daerah Wisata', 'Lainnya', 'Belum Diketahui']
)

# Jam Kejadian sebagai angka numerik
jam_kejadian = st.selectbox(
    'Pilih Jam Kejadian',
    ['00:00 - 03:00', '03:00 - 06:00', '06:00 - 09:00', '09:00 - 12:00', '12:00 - 15:00', 
     '15:00 - 18:00', '18:00 - 21:00', '21:00 - 00:00', 'Belum Diketahui']
)

bentuk_jalan = st.selectbox(
    'Pilih Bentuk Jalan',
    ['Lurus', 'X', 'Y', 'T', 'Tikungan', 'Bundaran', 'Lintasan KA', 'Lainnya', 'Belum Diketahui']
)

jenis_gangguan_jalan = st.selectbox(
    'Pilih Jenis Gangguan Jalan',
    ['Berlubang', 'Kurang Penerangan', 'Licin', 'Marka Rusak', 'Pandangan Terhalang', 'Rambu Rusak', 
     'Rusak', 'Tidak Ada Marka', 'Tidak Ada Rambu', 'Tikungan Tajam', 'Lainnya', 'Belum Diketahui']
)

Jumlah_Sepeda_Motor = st.number_input('Jumlah Sepeda Motor', min_value=0)
Jumlah_Mobil_Penumpang = st.number_input('Jumlah Mobil Penumpang', min_value=0)
Jumlah_Mobil_Bus = st.number_input('Jumlah Mobil Bus', min_value=0)
Jumlah_Mobil_Barang = st.number_input('Jumlah Mobil Barang', min_value=0)
_Kendaraan_Khusus = st.number_input('Jumlah Kendaraan Khusus', min_value=0)
Jumlah_tidak_bermotor = st.number_input('Jumlah Kendaraan Tidak Bermotor', min_value=0)
Luka_Berat = st.number_input('Luka Berat', min_value=0)
Luka_Ringan = st.number_input('Luka Ringan', min_value=0)
Tidak_Luka = st.number_input('Tidak Luka', min_value=0)

kondisi_cuaca = st.selectbox('Pilih Kondisi Cuaca', ['Cerah', 'Berawan', 'Hujan Ringan', 'Hujan Lebat'])
Meninggal_Dunia = st.number_input('Meninggal Dunia', min_value=0)

# Menyusun input data dalam format dictionary
input_data = {
    "Tipe_Tabrakan": kategori_mapping_tipe_tabrakan[tipe_tabrakan],
    "Klasifikasi_Fungsi_Jalan": kategori_mapping_klasifikasi_jalan[klasifikasi_fungsi_jalan],
    "Kelas_Jalan": kategori_mapping_kelas_jalan[kelas_jalan],
    "Status_Administratif_Jalan": kategori_mapping_status_administratif_jalan[status_administratif_jalan],
    "Jenis_Kawasan": kategori_mapping_jenis_kawasan[jenis_kawasan],
    "Jam_Kejadian": kategori_mapping_jam_kejadian[jam_kejadian],  # Jam Kejadian tetap numerik
    "Bentuk_Jalan": kategori_mapping_bentuk_jalan[bentuk_jalan],
    "Jenis_Gangguan_Jalan": kategori_mapping_jenis_gangguan_jalan[jenis_gangguan_jalan],
    "Jumlah_Sepeda_Motor": Jumlah_Sepeda_Motor,
    "Jumlah_Mobil_Penumpang": Jumlah_Mobil_Penumpang,
    "Jumlah_Mobil_Bus": Jumlah_Mobil_Bus,
    "Jumlah_Mobil_Barang": Jumlah_Mobil_Barang,
    "_Kendaraan_Khusus": _Kendaraan_Khusus,
    "Jumlah_tidak_bermotor": Jumlah_tidak_bermotor,
    "Luka_Berat": Luka_Berat,
    "Luka_Ringan": Luka_Ringan,
    "Tidak_Luka": Tidak_Luka,
    "Kondisi_Cuaca": kategori_mapping_kondisi_cuaca[kondisi_cuaca],
    "Meninggal_Dunia": Meninggal_Dunia
}

# Mengonversi input data ke DataFrame dan sesuaikan urutan fitur
input_df = pd.DataFrame([input_data])
input_df = input_df[model_rf.feature_names_in_]

# Menampilkan input data
st.write("Data Input yang Dimasukkan:")
st.write(input_df)

# Prediksi
hasil_prediksi = model_rf.predict(input_df)

# Interpretasi hasil
if hasil_prediksi[0] == 1:
    st.success("Hasil Prediksi: Tingkat Keparahan = Berat")
elif hasil_prediksi[0] == 2:
    st.success("Hasil Prediksi: Tingkat Keparahan = Sedang")
else:
    st.success("Hasil Prediksi: Tingkat Keparahan = Ringan")

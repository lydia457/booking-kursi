import streamlit as st

# Setup halaman
st.set_page_config(page_title="GO AWARDS 2025", layout="wide")

# Konstanta
TOTAL_KURSI = 500

# Inisialisasi session state
if 'kursi' not in st.session_state:
    st.session_state.kursi = ["kosong"] * TOTAL_KURSI
if 'sudah_pilih' not in st.session_state:
    st.session_state.sudah_pilih = False
if 'pilihan_kursi' not in st.session_state:
    st.session_state.pilihan_kursi = None

# Judul
st.markdown("<h1 style='text-align: center;'>🎉 GO AWARDS 2025 - Reservasi Kursi 🎉</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input kode pembayaran
kode = st.text_input("Masukkan kode pembayaran (contoh: LUNAS)")

if kode:
    if kode.upper() == "LUNAS":
        st.success("Kode pembayaran valid! Silakan pilih kursi.")

        kursi_kosong = [i+1 for i, k in enumerate(st.session_state.kursi) if k == "kosong"]

        if not st.session_state.sudah_pilih:
            if kursi_kosong:
                pilihan = st.selectbox("Pilih nomor kursi yang masih kosong:", kursi_kosong)

                if st.button("Reservasi Kursi"):
                    st.session_state.kursi[pilihan-1] = "terisi"
                    st.session_state.sudah_pilih = True
                    st.session_state.pilihan_kursi = pilihan
                    st.success(f"Kursi nomor {pilihan} berhasil dipesan!")
            else:
                st.warning("Semua kursi sudah penuh.")
        else:
            st.info(f"Anda sudah memilih kursi nomor {st.session_state.pilihan_kursi}.")

            if st.button("Reset Pilihan"):
                st.session_state.kursi[st.session_state.pilihan_kursi - 1] = "kosong"
                st.session_state.sudah_pilih = False
                st.session_state.pilihan_kursi = None
                st.success("Pilihan Anda berhasil di-reset. Silakan pilih kursi baru.")

    else:
        st.error("Kode pembayaran salah. Hubungi panitia jika ada masalah.")

# Tampilkan informasi kursi
st.markdown("---")
st.subheader("Informasi Kursi:")

kursi_kosong = [i+1 for i, k in enumerate(st.session_state.kursi) if k == "kosong"]
kursi_terisi = [i+1 for i, k in enumerate(st.session_state.kursi) if k == "terisi"]

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Kursi Kosong:**")
    st.write(kursi_kosong)
    st.info(f"Total kursi kosong: {len(kursi_kosong)}")

with col2:
    st.markdown("**Kursi Terisi:**")
    st.write(kursi_terisi)
    st.success(f"Total kursi terisi: {len(kursi_terisi)}")

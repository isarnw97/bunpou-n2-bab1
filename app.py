import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 7", layout="centered")

# --- DATABASE SOAL ---

if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        {
            "id": 1, "pola": "Pola 1: 〜ということだ ・ 〜とのことだ",
            "kanji": "市のお知らせによれば、この道路は来週から工事が始まるということです。",
            "hiragana": "いちのおしらせによれば、このどうろはらいしゅうからこうじがはじまるということです。",
            "arti": "Berdasarkan pengumuman kota, kabarnya pekerjaan konstruksi jalan ini akan dimulai dari minggu depan.",
            "kunci": ["市", "お知らせ", "に", "よれば", "、",
                      "この", "道路", "は", "来週", "から", "工事",
                      "が", "始まる", "という", "こと", "です", "。"],

            "soal": ["市", "お知らせ", "に", "よれば",
                     "この", "道路", "は", "来週", "から", "工事",
                     "が", "始まる", "という", "こと", "です", "、", "。"]
        }
    ]

# Inisialisasi State

if "index_soal" not in st.session_state:
    st.session_state.index_soal = 0

if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = []

if "bank_kata" not in st.session_state:
    st.session_state.bank_kata = []

if "status_periksa" not in st.session_state:
    st.session_state.status_periksa = False

# State untuk Fitur Tukar Posisi Murni (Swap)

if "idx_kata_dipilih" not in st.session_state:
    st.session_state.idx_kata_dipilih = None

if "mode_tukar" not in st.session_state:
    st.session_state.mode_tukar = False

soal_sekarang = st.session_state.database_soal[
    st.session_state.index_soal
]

if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [
        {"id": i, "teks": kata, "dipakai": False}
        for i, kata in enumerate(soal_sekarang["soal"])
    ]

# --- STYLING CSS ---

st.markdown("""
<style>

    /* Sembunyikan label bawaan st.pills */

    div[data-testid="stStatusWidget"] + div
    div[data-testid="stWidgetLabel"] {
        display: none;
    }

    /* Grid Pilihan Kata di bawah tetap 4 kolom di HP */

    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
    }

    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 22% !important;
        min-width: 70px !important;
    }

    /* KOTAK PILIHAN KATA
       Supaya kosakata panjang tidak menjadi (...) */

    div.stButton > button {
        border-radius: 12px !important;
        font-weight: bold !important;
        padding: 6px 10px !important;

        /* Teks jangan dipotong */
        white-space: nowrap !important;
        overflow: visible !important;
        text-overflow: clip !important;

        /* Kotak menyesuaikan isi */
        min-width: max-content !important;
        width: 100% !important;
    }

    /* Pastikan teks di dalam tombol tidak dipotong */

    div.stButton > button p {
        white-space: nowrap !important;
        overflow: visible !important;
        text-overflow: clip !important;
    }

    /* Kotak Info Soal */

    .info-box {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #1fa2ff;
        margin-bottom: 20px;
    }

    .text-bunpou {
        font-size: 1.05rem;
        font-weight: bold;
        color: #1fa2ff;
        margin: 0 0 6px 0;
    }

    .text-arti {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1a1a1a;
        margin: 0;
    }

    /* Indikator Mode Tukar */

    .swap-indicator {
        background-color: #e6fffa;
        border: 1px dashed #319795;
        padding: 10px;
        border-radius: 8px;
        color: #234e52;
        font-weight: bold;
        margin-bottom: 10px;
        font-size: 0.9rem;
    }

</style>
""", unsafe_allow_html=True)

# Tampilan Atas

st.title("🦉 Bunpou Master (BAB 7)")

st.caption(
    f"Soal {soal_sekarang['id']} dari "
    f"{len(st.session_state.database_soal)}"
)

st.markdown("---")

# Kotak Petunjuk Soal

st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">🇮🇩 {soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- MENU UTAMA INTERAKTIF (FRAGMENT) ---

@st.fragment
def render_kuis_lengkap():

    st.write("### Kalimat Susunanmu:")

    # Pilihan Mode Aksi Sentuhan

    mode = st.radio(
        "Aksi Sentuhan Papan:",
        ["Copot Kata (Normal)", "Tukar Posisi 2 Kata 🔄"],
        horizontal=True,
        label_visibility="collapsed"
    )

    # Tampilkan petunjuk swap jika mode aktif

    if mode == "Tukar Posisi 2 Kata 🔄":

        st.session_state.mode_tukar = True

        if st.session_state.idx_kata_dipilih is not None:

            kata_terpilih = st.session_state.jawaban_user[
                st.session_state.idx_kata_dipilih
            ]["teks"]

            st.markdown(
                f'<div class="swap-indicator">'
                f'📍 Kata [{kata_terpilih}] terpilih. '
                f'Sekarang klik kata tujuan untuk bertukar posisi!'
                f'</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="swap-indicator">'
                '💡 Klik kata pertama yang ingin ditukar posisinya...'
                '</div>',
                unsafe_allow_html=True
            )

    else:

        st.session_state.mode_tukar = False
        st.session_state.idx_kata_dipilih = None

    # 1. PAPAN JAWABAN (ST.PILLS)

    if not st.session_state.jawaban_user:

        st.markdown(
            "<div style='border-bottom: 2px solid #e5e5e5; "
            "padding-bottom: 15px; margin-bottom: 20px; "
            "color:#aaaaaa; font-style:italic;'>"
            "Klik kata di bawah untuk mulai menyusun..."
            "</div>",
            unsafe_allow_html=True
        )

    else:

        # Format indeks agar urutan terdeteksi sempurna

        opsi_papan = [
            f"{idx}. {item['teks']}"
            for idx, item in enumerate(
                st.session_state.jawaban_user
            )
        ]

        format_papan = {
            opt: opt.split(". ", 1)[1]
            for opt in opsi_papan
        }

        klik_papan = st.pills(
            label="Papan Jawaban",
            options=opsi_papan,
            format_func=lambda x: format_papan[x],
            selection_mode="single",
            label_visibility="collapsed"
        )

        st.markdown(
            "<div style='border-bottom: 2px solid #e5e5e5; "
            "margin-top: -10px; margin-bottom: 25px;'></div>",
            unsafe_allow_html=True
        )

        # LOGIKA PROSES KLIK DI PAPAN

        if klik_papan:

            idx_klik = int(klik_papan.split(". ")[0])

            if st.session_state.mode_tukar:

                # JIKA MODE TUKAR (SWAP MURNI) ACTIVE

                if st.session_state.idx_kata_dipilih is None:

                    # Klik Pertama: Simpan posisi kata ke-1

                    st.session_state.idx_kata_dipilih = idx_klik

                    st.rerun()

                else:

                    # Klik Kedua: Tukar langsung isi data kata
                    # ke-1 dan kata ke-2

                    idx1 = st.session_state.idx_kata_dipilih
                    idx2 = idx_klik

                    if idx1 != idx2:

                        # Trik Python untuk menukar isi variabel
                        # secara instan tanpa menggeser tengahnya

                        (
                            st.session_state.jawaban_user[idx1],
                            st.session_state.jawaban_user[idx2]
                        ) = (
                            st.session_state.jawaban_user[idx2],
                            st.session_state.jawaban_user[idx1]
                        )

                    # Reset Klik

                    st.session_state.idx_kata_dipilih = None

                    st.rerun()

            else:

                # JIKA MODE NORMAL (COPOT KE BAWAH)

                kata_dicopot = st.session_state.jawaban_user.pop(
                    idx_klik
                )

                for kata_bank in st.session_state.bank_kata:

                    if kata_bank["id"] == kata_dicopot["id"]:

                        kata_bank["dipakai"] = False

                st.rerun()

    # 2. BANK KATA PILIHAN

    st.write("### Pilihan Kata:")

    cols_pilihan = st.columns(4)

    for idx, item in enumerate(st.session_state.bank_kata):

        posisi_kolom = idx % 4

        with cols_pilihan[posisi_kolom]:

            if item["dipakai"]:

                st.button(
                    " ",
                    key=f"disabled_{item['id']}",
                    disabled=True,
                    use_container_width=True
                )

            else:

                if st.button(
                    item["teks"],
                    key=f"pilih_{item['id']}",
                    use_container_width=True
                ):

                    item["dipakai"] = True

                    st.session_state.jawaban_user.append(item)

                    st.rerun()


# Jalankan Komponen Utama Kuis

render_kuis_lengkap()

st.markdown("<br><hr>", unsafe_allow_html=True)

# 3. TOMBOL NAVIGASI UTAMA

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("Reset 🔄", use_container_width=True):

        st.session_state.jawaban_user = []

        for kata in st.session_state.bank_kata:

            kata["dipakai"] = False

        st.session_state.idx_kata_dipilih = None

        st.session_state.status_periksa = False

        st.rerun()


with col2:

    if st.button(
        "PERIKSA ✅",
        type="primary",
        use_container_width=True
    ):

        st.session_state.status_periksa = True


with col3:

    if st.button(
        "Lanjut ➡️",
        use_container_width=True
    ):

        st.session_state.index_soal = (
            st.session_state.index_soal + 1
        ) % len(st.session_state.database_soal)

        st.session_state.jawaban_user = []

        st.session_state.bank_kata = []

        st.session_state.idx_kata_dipilih = None

        st.session_state.status_periksa = False

        st.rerun()


# VALIDASI JAWABAN

if st.session_state.status_periksa:

    user_strings = [
        x["teks"]
        for x in st.session_state.jawaban_user
    ]

    kunci_strings = soal_sekarang["kunci"]

    user_joined = (
        "".join(user_strings)
        .replace(" ", "")
        .replace("、", "")
        .replace("。", "")
    )

    kunci_joined = (
        "".join(kunci_strings)
        .replace(" ", "")
        .replace("、", "")
        .replace("。", "")
    )

    if user_joined == kunci_joined:

        st.success(
            f"🎉 **正解 (Benar)!** "
            f"Susunan bunpou kamu sudah sempurna!\n\n"
            f"**🇯🇵 Kanji:** {soal_sekarang['kanji']}\n\n"
            f"**💡 Hiragana:** {soal_sekarang['hiragana']}"
        )

    else:

        st.error(
            f"❌ **残念 (Kurang Tepat).**\n\n"
            f"**Susunan yang benar:**\n\n"
            f"`{' '.join(kunci_strings)}`\n\n"
            f"**🇯🇵 Kanji asli:** {soal_sekarang['kanji']}\n\n"
            f"**💡 Hiragana:** {soal_sekarang['hiragana']}"
        )

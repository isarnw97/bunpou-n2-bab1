import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 7", layout="centered")

# --- DATABASE SOAL ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
       # === POLA 1: ～てはじめて ===
        {
            "id": 1,
            "pola": "1 ～てはじめて",
            "kanji": "実際の現地の様子を見てはじめて、今回の地震のひどさを知った。",
            "hiragana": "じっさいのげんちのようすをみてはじめて、こんかいのじしんのひどさをしった。",
            "arti": "Setelah melihat langsung kondisi di lapangan, barulah saya menyadari betapa parahnya gempa kali ini.",
            "kunci": ["実際", "の", "現地", "の", "様子", "を", "見て", "はじめて", "、", "今回", "の", "地震", "の", "ひどさ", "を", "知った", "。"],
            "soal": ["の", "今回", "はじめて", "地震", "ひどさ", "知った", "実際", "現地", "様子", "を", "見て", "の", "を", "、"]
        },
        {
            "id": 2,
            "pola": "1 ～てはじめて",
            "kanji": "人に言われてはじめて、相手の話の途中で話を始める癖があることに気づいた。",
            "hiragana": "ひとにいわれてはじめて、あいてのはなしのとちゅうではなしをはじめるくせがあることにきづいた。",
            "arti": "Setelah diberitahu orang lain, barulah saya menyadari bahwa saya punya kebiasaan mulai berbicara di tengah-tengah pembicaraan orang lain.",
            "kunci": ["人", "に", "言われて", "はじめて", "、", "相手", "の", "話", "の", "途中", "で", "話", "を", "始める", "癖", "が", "ある", "こと", "に", "気づいた", "。"],
            "soal": ["言われて", "癖", "話", "途中", "で", "話", "相手", "始めに", "気づいた", "が", "ある", "と", "人", "に", "はじめて", "の", "、", "を"]
        },
        {
            "id": 3,
            "pola": "1 ～てはじめて",
            "kanji": "山田先生の指導を受けてはじめて、生物の観察が面白いと思うようになった。",
            "hiragana": "やまだせんせいのしどうをうけてはじめて、せいぶつのかんさつがおもしろいとおもうようになった。",
            "arti": "Setelah mendapat bimbingan dari Pak Yamada, barulah saya mulai merasa bahwa mengamati makhluk hidup itu menarik.",
            "kunci": ["山田先生", "の", "指導", "を", "受け", "て", "はじめて", "、", "生物", "の", "観察", "が", "面白い", "と", "思った", "になった", "。"],
            "soal": ["生物", "観察", "生徒", "指導", "山田先生", "面白い", "思った", "はじめて", "受け", "て", "の", "が", "と", "になった", "の", "、"]
        },
        {
            "id": 4,
            "pola": "1 ～てはじめて",
            "kanji": "チャンスがあってはじめて、才能が生きてくるのではないだろうか。",
            "hiragana": "ちゃんすがかってはじめて、さいのうがいきてくるのではないだろうか。",
            "arti": "Bukankah bakat baru akan hidup/terlihat setelah adanya kesempatan?",
            "kunci": ["チャンス", "が", "あって", "はじめて", "、", "才能", "が", "生きてくる", "の", "ではないだろうか", "。"],
            "soal": ["チャンス", "才能", "生きてくる", "はじめて", "が", "の", "あって", "ではないだろうか", "が", "、"]
        },

        # === POLA 2: ～上（で） ===
        {
            "id": 5,
            "pola": "2 ～上（で）",
            "kanji": "文書が保存されていることを確かめた上で、パソコンをシャットダウンしてください。",
            "hiragana": "ぶんしょがほぞんされていることをたしかめたうえで、ぱそこんをしゃっとだうんしてください。",
            "arti": "Setelah memastikan bahwa dokumen telah disimpan, silakan matikan komputer.",
            "kunci": ["文書", "が", "保存されている", "こと", "を", "確かめた", "上で", "、", "パソコン", "を", "シャットダウンして", "ください", "。"],
            "soal": ["保存されている", "上で", "シャットダウンして", "パソコン", "文書", "こと", "確かめた", "を", "を", "ください", "が", "、"]
        },
        {
            "id": 6,
            "pola": "2 ～上（で）",
            "kanji": "経済的なことをよく考えた上で、進路を決める need/必要がある。",
            "hiragana": "けいざいてきなことをよくかんがえたうえで、しんろをきめるひつようがある。",
            "arti": "Setelah memikirkan kondisi keuangan dengan matang, perlu untuk memutuskan jalan/penjurusan ke depan.",
            "kunci": ["経済的な", "こと", "を", "よく", "考えた", "上で", "、", "進路", "を", "決める", "必要", "が", "ある", "。"],
            "soal": ["考えた", "上で", "経済的な", "進路", "決める", "必要", "が", "ある", "こと", "よく", "を", "を", "、"]
        },
        {
            "id": 7,
            "pola": "2 ～上（で）",
            "kanji": "自分一人では決められませんので、家族と相談した上で、お返事いたします。",
            "hiragana": "じぶんひとりではきめられませんので、かぞくとそうだんしたうえで、おへんじいたします。",
            "arti": "Karena tidak bisa saya putuskan sendiri, saya akan memberikan jawaban setelah berdiskusi dengan keluarga.",
            "kunci": ["自分一人", "では", "決められません", "ので", "、", "家族", "と", "相談した", "上で", "、", "お返事", "いたします", "。"],
            "soal": ["相談した", "上で", "自分一人", "お返事", "決められません", "ので", "家族", "と", "を", "いたします", "では", "、", "、"]
        },
        {
            "id": 8,
            "pola": "2 ～上（で）",
            "kanji": "この列車にご乗車には、あらかじめ特急券をお買い求めの上、ご乗車ください。特急券が必要です。",
            "hiragana": "このれっしゃにごじょうしゃには、あらかじめとっきゅうけんをおかいもとめうえ、ごじょうしゃください。とっきゅうけんがひつようです。",
            "arti": "Untuk naik kereta ini, silakan membeli tiket ekspres terlebih dahulu sebelum naik. Tiket ekspres diperlukan.",
            "kunci": ["この", "列車", "に", "ご乗車", "には", "、", "あらかじめ", "特急券", "を", "お買い求め", "上", "、", "ご乗車", "ください", "。", "特急券", "が", "必要です", "。"],
            "soal": ["この", "列車", "あらかじめ", "お買い求め", "上", "ご乗車", "特急券", "が", "必要です", "特急券", "を", "ください", "に", "は", "、", "。"]
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

if "idx_kata_dipilih" not in st.session_state:
    st.session_state.idx_kata_dipilih = None

if "mode_tukar" not in st.session_state:
    st.session_state.mode_tukar = False

soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]

if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

# --- CSS KHUSUS UNTUK TAMPILAN KAPSU/PILL KATA SEPERTI GAMBAR ---
st.markdown("""
<style>
    /* Mengubah Container Tombol Bank Kata menjadi Inline Flex ke samping */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 8px 10px !important;
        align-items: center !important;
    }
    
    div[data-testid="stHorizontalBlock"] > div {
        flex: 0 0 auto !important;
        width: auto !important;
        min-width: 0 !important;
    }

    /* Tampilan Kotak Kapsul / Pill Sesuai Gambar */
    div[data-testid="stHorizontalBlock"] button {
        border-radius: 50px !important;            /* Bulat lonjong sempurna */
        border: 1px solid #cccccc !important;       /* Garis tepi tipis abu-abu */
        background-color: #ffffff !important;      /* Warna dasar putih */
        color: #333333 !important;                 /* Warna teks gelap */
        font-size: 1.1rem !important;
        padding: 6px 18px !important;               /* Jarak dalam yang empuk */
        box-shadow: none !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* Efek saat tombol di-hover / diklik */
    div[data-testid="stHorizontalBlock"] button:hover {
        border-color: #888888 !important;
        background-color: #f7f7f7 !important;
    }

    /* Kotak Info Soal */
    .info-box {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #1fa2ff;
        margin-bottom: 20px;
    }
    .text-bunpou { font-size: 1.05rem; font-weight: bold; color: #1fa2ff; margin: 0 0 6px 0; }
    .text-arti { font-size: 1.2rem; font-weight: bold; color: #1a1a1a; margin: 0; }

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
st.caption(f"Soal {soal_sekarang['id']} dari {len(st.session_state.database_soal)}")
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
    
    mode = st.radio(
        "Aksi Sentuhan Papan:",
        ["Copot Kata (Normal)", "Tukar Posisi 2 Kata 🔄"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    if mode == "Tukar Posisi 2 Kata 🔄":
        st.session_state.mode_tukar = True
        if st.session_state.idx_kata_dipilih is not None:
            kata_terpilih = st.session_state.jawaban_user[st.session_state.idx_kata_dipilih]["teks"]
            st.markdown(f'<div class="swap-indicator">📍 Kata [{kata_terpilih}] terpilih. Klik kata tujuan untuk bertukar posisi!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="swap-indicator">💡 Klik kata pertama yang ingin ditukar posisinya...</div>', unsafe_allow_html=True)
    else:
        st.session_state.mode_tukar = False
        st.session_state.idx_kata_dipilih = None

    # 1. PAPAN JAWABAN (ST.PILLS)
    if not st.session_state.jawaban_user:
        st.markdown("<div style='border-bottom: 2px solid #e5e5e5; padding-bottom: 15px; margin-bottom: 20px; color:#aaaaaa; font-style:italic;'>Klik kata di bawah untuk mulai menyusun...</div>", unsafe_allow_html=True)
    else:
        opsi_papan = [f"{idx}. {item['teks']}" for idx, item in enumerate(st.session_state.jawaban_user)]
        format_papan = {opt: opt.split(". ", 1)[1] for opt in opsi_papan}
        
        klik_papan = st.pills(
            label="Papan Jawaban",
            options=opsi_papan,
            format_func=lambda x: format_papan[x],
            selection_mode="single",
            label_visibility="collapsed"
        )
        
        st.markdown("<div style='border-bottom: 2px solid #e5e5e5; margin-top: -10px; margin-bottom: 25px;'></div>", unsafe_allow_html=True)

        if klik_papan:
            idx_klik = int(klik_papan.split(". ")[0])
            if st.session_state.mode_tukar:
                if st.session_state.idx_kata_dipilih is None:
                    st.session_state.idx_kata_dipilih = idx_klik
                    st.rerun()
                else:
                    idx1 = st.session_state.idx_kata_dipilih
                    idx2 = idx_klik
                    if idx1 != idx2:
                        st.session_state.jawaban_user[idx1], st.session_state.jawaban_user[idx2] = st.session_state.jawaban_user[idx2], st.session_state.jawaban_user[idx1]
                    st.session_state.idx_kata_dipilih = None
                    st.rerun()
            else:
                kata_dicopot = st.session_state.jawaban_user.pop(idx_klik)
                for kata_bank in st.session_state.bank_kata:
                    if kata_bank["id"] == kata_dicopot["id"]:
                        kata_bank["dipakai"] = False
                st.rerun()

    # 2. BANK KATA PILIHAN (Bentuk Kapsul & Berjajar Alami Ke Samping)
    st.write("### Pilihan Kata:")
    
    # Menggunakan st.columns secara merata dalam 1 container horizontal yang diatur CSS Flexbox
    cols = st.columns(len(st.session_state.bank_kata))
    for idx, item in enumerate(st.session_state.bank_kata):
        with cols[idx]:
            if item["dipakai"]:
                st.button(" ", key=f"disabled_{item['id']}", disabled=True)
            else:
                if st.button(item["teks"], key=f"pilih_{item['id']}"):
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
    if st.button("PERIKSA ✅", type="primary", use_container_width=True):
        st.session_state.status_periksa = True

with col3:
    if st.button("Lanjut ➡️", use_container_width=True):
        st.session_state.index_soal = (st.session_state.index_soal + 1) % len(st.session_state.database_soal)
        st.session_state.jawaban_user = []
        st.session_state.bank_kata = []
        st.session_state.idx_kata_dipilih = None
        st.session_state.status_periksa = False
        st.rerun()

# VALIDASI JAWABAN
if st.session_state.status_periksa:
    user_strings = [x["teks"] for x in st.session_state.jawaban_user]
    kunci_strings = soal_sekarang["kunci"]
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "")
    kunci_joined = "".join(kunci_strings).replace(" ", "").replace("、", "").replace("。", "")
    
    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan bunpou kamu sudah sempurna!\n\n**🇯🇵 Kanji:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n**Susunan yang benar:**\n\n`{' '.join(kunci_strings)}`\n\n**🇯🇵 Kanji asli:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")

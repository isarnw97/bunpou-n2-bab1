import random
import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 1", layout="centered")

# --- DATABASE SOAL (BAB 1) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # ==================== POIN 1: ～を通じて・～を通して ====================
        {
            "id": 1,
            "pola": "1. ～を通じて・～を通して",
            "kanji": "この町では、四季を通じて様々な we! お祭りが we! 行われる。",
            "hiragana": "このまちでは、しきをつうじてさまざまなまつりがおこなわれる。",
            "arti": "Di kota ini, sepanjang empat musim diadakan berbagai macam festival.",
            "soal": ["さまざまな", "おまつり が", "しき", "この まち では", "おこなわれる", "をつうじて", "、"],
            "kunci": ["この まち では", "、", "しき", "をつうじて", "さまざまな", "おまつり が", "おこなわれる"]
        },
        {
            "id": 2,
            "pola": "1. ～を通じて・～を通して",
            "kanji": "京都には年間を通して、世界中から観光客が訪れる。",
            "hiragana": "きょうとにはねんかんをとおして、せかいじゅうからかんこうきゃくがおとずれる。",
            "arti": "Di Kyoto, sepanjang tahun datang wisatawan dari seluruh dunia.",
            "soal": ["せかいじゅう から", "ねんかん", "かんこうきゃく が", "をとおして", "きょうと には", "おとずれる", "、"],
            "kunci": ["きょうと には", "ねんかん", "をとおして", "、", "せかいじゅう から", "かんこうきゃく が", "おとずれる"]
        },
        {
            "id": 3,
            "pola": "1. ～を通じて・～を通して",
            "kanji": "ボランティア活動を通して、多くの人と出会うことができた。",
            "hiragana": "ぼらんてぃあかつどうをとおして、おおくのひととであうことができた。",
            "arti": "Melalui kegiatan sukarela, saya bisa bertemu dengan banyak orang.",
            "soal": ["ぼらんてぃあかつどう", "であうこと が できた", "おおくの ひと と", "をとおして", "、"],
            "kunci": ["ぼらんてぃあかつどう", "をとおして", "、", "おおくの ひと と", "であうこと が できた"]
        },

        # ==================== POIN 2: ～をこめて ====================
        {
            "id": 4,
            "pola": "2. ～をこめて",
            "kanji": "愛をこめて、このプレゼントを贈ります。",
            "hiragana": "あいをこめて、このぷれぜんとをおくります。",
            "arti": "Dengan sepenuh rasa cinta, saya memberikan hadiah ini.",
            "soal": ["この ぷれぜんと", "あい", "をこめて", "をおくります", "、"],
            "kunci": ["あい", "をこめて", "、", "この ぷれぜんと", "をおくります"]
        },
        {
            "id": 5,
            "pola": "2. ～をこめて",
            "kanji": "感謝の気持ちをこめて、手紙を書きました。",
            "hiragana": "かんしゃのきもちをこめて、てがみをかきました。",
            "arti": "Dengan perasaan penuh syukur, saya menulis surat.",
            "soal": ["かんしゃ の きもち", "てがみ", "をこめて", "をかきました", "、"],
            "kunci": ["かんしゃ の きもち", "をこめて", "、", "てがみ", "をかきました"]
        },

        # ==================== POIN 3: ～をきっかけに ====================
        {
            "id": 6,
            "pola": "3. ～をきっかけに",
            "kanji": "日本のアニメを見たのをきっかけに、日本語の勉強を始めた。",
            "hiragana": "にほんのあにめをみたのをきっかけに、にほんごのべんきょうをはじめた。",
            "arti": "Berawal dari menonton anime Jepang, saya mulai belajar bahasa Jepang.",
            "soal": ["にほんご の べんきょう", "にほん の あにめ", "をみたの", "をきっかけに", "をはじめた", "、"],
            "kunci": ["にほん の あにめ", "をみたの", "をきっかけに", "、", "にほんご の べんきょう", "をはじめた"]
        },
        {
            "id": 7,
            "pola": "3. ～をきっかけに",
            "kanji": "結婚をきっかけに、車を買うことにした。",
            "hiragana": "けっこんをきっかけに、くるまをかうことにした。",
            "arti": "Berawal dari pernikahan, kami memutuskan untuk membeli mobil.",
            "soal": ["けっこん", "くるま", "をきっかけに", "をかうことにした", "、"],
            "kunci": ["けっこん", "をきっかけに", "、", "くるま", "をかうことにした"]
        },

        # ==================== POIN 4: ～を中心に ====================
        {
            "id": 8,
            "pola": "4. ～を中心に",
            "kanji": "東京を中心に関東地方で強い地震があった。",
            "hiragana": "とうきょうをちゅうしんにかんとうちほうでつよいじしんがあった。",
            "arti": "Terjadi gempa bumi kuat di wilayah Kanto dengan berpusat di Tokyo.",
            "soal": ["とうきょう", "かんとうちほう で", "をつうしんに", "つよいじしん が あった"],
            "kunci": ["とうきょう", "をつうしんに", "かんとうちほう で", "つよいじしん が あった"]
        },
        {
            "id": 9,
            "pola": "4. ～を中心に",
            "kanji": "若い人を中心にして、そのゲームが流行している。",
            "hiragana": "わかいひとをちゅうしんにして、そのげーむがりゅうこうしている。",
            "arti": "Game tersebut populer berpusat pada anak-anak muda.",
            "soal": ["わかい ひと", "その げーむ が", "をちゅうしんにして", "りゅうこうしている", "、"],
            "kunci": ["わかい ひと", "をちゅうしんにして", "、", "その げーむ が", "りゅうこうしている"]
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

# State untuk Fitur Swap
if "idx_kata_dipilih" not in st.session_state:
    st.session_state.idx_kata_dipilih = None
if "mode_tukar" not in st.session_state:
    st.session_state.mode_tukar = False

soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]

if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    soal_acak = list(soal_sekarang["soal"])
    random.seed(42)
    random.shuffle(soal_acak)
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_acak)]

# --- STYLING CSS SOLUSI TEKS TERPOTONG TITIK-TITIK ---
st.markdown("""
<style>
    div[data-testid="stStatusWidget"] + div div[data-testid="stWidgetLabel"] {
        display: none;
    }
    
    /* Menjaga Layout 4 Kolom di HP */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 4px !important;
    }
    
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 22% !important; 
        min-width: 0 !important;
    }
    
    /* Mencegah titik-titik (ellipsis) & Mengizinkan teks berpindah baris secara alami */
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 4px 2px !important;
        font-size: clamp(0.68rem, 2.3vw, 0.9rem) !important;
        line-height: 1.2 !important;
        height: auto !important;
        min-height: 42px !important;
    }

    /* Memaksa elemen p, div, span di dalam tombol untuk wrapping */
    div.stButton > button p, div.stButton > button div, div.stButton > button span {
        white-space: normal !important;
        word-break: break-all !important;
        text-overflow: clip !important;
        overflow: visible !important;
    }

    .info-box {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #1fa2ff;
        margin-bottom: 20px;
    }
    .text-bunpou { font-size: 1.05rem; font-weight: bold; color: #1fa2ff; margin: 0 0 6px 0; }
    .text-arti { font-size: 1.2rem; font-weight: bold; color: #1a1a1a; margin: 0; }
    
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
st.title("🦉 Bunpou Master (BAB 1)")
st.caption(f"Soal {st.session_state.index_soal + 1} dari {len(st.session_state.database_soal)}")
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
            st.markdown(f'<div class="swap-indicator">📍 Kata [{kata_terpilih}] terpilih. Sekarang klik kata tujuan untuk bertukar posisi!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="swap-indicator">💡 Klik kata pertama yang ingin ditukar posisinya...</div>', unsafe_allow_html=True)
    else:
        st.session_state.mode_tukar = False
        st.session_state.idx_kata_dipilih = None

    # 1. PAPAN JAWABAN
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

    # 2. BANK KATA PILIHAN (4 Kolom)
    st.write("### Pilihan Kata:")
    cols_pilihan = st.columns(4)
    for idx, item in enumerate(st.session_state.bank_kata):
        posisi_kolom = idx % 4
        with cols_pilihan[posisi_kolom]:
            if item["dipakai"]:
                st.button(" ", key=f"disabled_{item['id']}", disabled=True, use_container_width=True)
            else:
                if st.button(item["teks"], key=f"pilih_{item['id']}", use_container_width=True):
                    item["dipakai"] = True
                    st.session_state.jawaban_user.append(item)
                    st.rerun()

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
    
    user_joined = "".join(user_strings)
    kunci_joined = "".join(kunci_strings)
    
    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan bunpou kamu sudah sempurna!\n\n**🇯🇵 Kanji:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n**Susunan yang benar:**\n\n`{' '.join(kunci_strings)}`\n\n**🇯🇵 Kanji asli:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")

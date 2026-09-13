import random
import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang", layout="centered")

# --- DATABASE SOAL (TETAP SAMA TANPA DIUBAH SAMA SEKALI) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # ==================== POIN 1 ====================
        {
            "id": 1,
            "pola": "1. ～に際して・～にあたって",
            "kanji": "この際、 | ひつようです | うけとり | しょうひん | の | せいりけん | は",
            "hiragana": "このさい、しょうひんのうけとりにはせいりけんがひつようです。",
            "arti": "Saat ini, tanda terima/kupon diperlukan untuk mengambil barang.",
            "soal": ["この", "さい", "ひつようです", "うけとり", "しょうひん", "の", "せいりけん", "は", "、", "、"],
            "kunci": ["この", "さい", "、", "しょうひん", "の", "うけとり", "には", "せいりけん", "が", "ひつようです"]
        },
        {
            "id": 2,
            "pola": "1. ～に際して・～にあたって",
            "kanji": "ご利用に際してのご記入ください...",
            "hiragana": "ごりよう に さいして の ひつようじこう を こちら で ごきにゅうください、かいぎしつ の ごりよう になる",
            "arti": "Saat akan menggunakan, silakan isi hal-hal yang diperlukan di sini...",
            "soal": ["ひつようじこう", "を", "うけつけ", "かいぎしつ", "に", "こちら", "で", "さい", "の", "ごきにゅうください", "ごりよう", "は", "、", "、", "になる"],
            "kunci": ["かいぎしつ", "の", "ごりよう", "に", "さい", "して", "の", "ひつようじこう", "を", "こちら", "で", "ごきにゅうください"]
        },
        {
            "id": 3,
            "pola": "1. ～に際して・～にあたって",
            "kanji": "アメリカ大統領の来日に際して...",
            "hiragana": "あめりか だいとうりょう の らいにち に さい して、わたしたち の だいがく で すぴーち を おこなった",
            "arti": "Berkenaan dengan kunjungan Presiden AS ke Jepang, beliau berpidato di universitas kami.",
            "soal": ["だいがく", "わたしたち", "だいとうりょう", "で", "すぴーち", "に", "らいにち", "の", "を", "おこなった", "あめりか", "さい", "した", "、"],
            "kunci": ["あめりか", "だいとうりょう", "の", "らいにち", "に", "さい", "した", "、", "わたしたち", "の", "だいがく", "で", "すぴーち", "を", "おこなった"]
        },

        # ==================== POIN 2 ====================
        {
            "id": 4,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "工事を始めるに際して...",
            "hiragana": "こうじ を はじめる にさいして、きんじょ の じゅうみん に あいさつ を して まわった",
            "arti": "Saat memulai konstruksi, kami berkeliling menyapa warga sekitar.",
            "soal": ["こうじ", "こうじかんけいしゃ", "に", "まわった", "あいさつ", "を", "きんじょ", "はじめる", "じゅうみん", "にさいして", "の", "は", "して", "、", "、"],
            "kunci": ["こうじ", "を", "はじめる", "にさいして", "、", "きんじょ", "の", "じゅうみん", "に", "あいさつ", "を", "して", "まわった"]
        },
        {
            "id": 5,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "当ショッピングサイトのご利用に際して...",
            "hiragana": "とうしょっぴんぐさいと の ごりよう にさいして、いかの ごりようじょうけん を よく およみください",
            "arti": "Saat menggunakan situs belanja ini, harap baca syarat dan ketentuan berikut dengan cermat.",
            "soal": ["よく", "いかの", "とうしょっぴんぐさいと", "にさいして", "ごりようじょうけん", "およみください", "を", "の", "ごりよう", "、", "、"],
            "kunci": ["とうしょっぴんぐさいと", "の", "ごりよう", "にさいして", "、", "いかの", "ごりようじょうけん", "を", "よく", "およみください"]
        },
        {
            "id": 6,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "新しく事業を始めるにあたって...",
            "hiragana": "あたらしく じぎょう を はじめる に あたって、しっかり じゅんび を しよう とおもっております",
            "arti": "Saat memulai bisnis baru, saya berniat untuk melakukan persiapan dengan matang.",
            "soal": ["じぎょう", "じゅんび", "しっかり", "を", "あたって", "に", "はじめる", "あたらしく", "とおもっております", "しよう", "、", "、"],
            "kunci": ["あたらしく", "じぎょう", "を", "はじめる", "に", "あたって", "、", "しっかり", "じゅんび", "を", "しよう", "とおもっております"]
        },
        {
            "id": 7,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "お門出にあたりまして...",
            "hiragana": "おふたり の かどで に あたりまして、おいわい の ことば を もうしあげます",
            "arti": "Mengawali lembaran baru Anda berdua, saya ingin menyampaikan sepatah kata ucapan selamat.",
            "soal": ["おふたりの", "もうしあげます", "おいわい", "あたりまして", "かどで", "に", "ことば", "を", "、", "、"],
            "kunci": ["おふたりの", "かどで", "に", "あたりまして", "、", "おいわい", "の", "ことば", "を", "もうしあげます"]
        },
        {
            "id": 8,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "国際会議を開催するにあたり...",
            "hiragana": "こくさいかいぎ を かいさいする に あたり、にほん の かんけいかくほうめん からの きょうりょくをえた",
            "arti": "Saat menyelenggarakan konferensi internasional, kami memperoleh kerja sama dari berbagai pihak terkait di Jepang.",
            "soal": ["こくさいかいぎ", "にほん", "きょうりょくをえた", "あたり", "かいさいする", "で", "からの", "に", "かんけいかくほうめん", "を", "、", "、"],
            "kunci": ["こくさいかいぎ", "を", "かいさいする", "に", "あたり", "、", "にほん", "の", "かんけいかくほうめん", "からの", "きょうりょくをえた"]
        },

        # ==================== POIN 3 ====================
        {
            "id": 9,
            "pola": "3. ～たとたん（に）",
            "kanji": "山頂でワインをひとくち飲んだ途端に...",
            "hiragana": "やま の ちょうじょう で わいん を ひとくち のんだ たとたんに、めまい が した",
            "arti": "Begitu meminum seteguk anggur di puncak gunung, saya langsung merasa pusing.",
            "soal": ["の", "やま", "めまい", "のんだ", "ちょうじょう", "ひとくち", "わいん", "で", "たとたんに", "が", "を", "した", "、"],
            "kunci": ["やま", "の", "ちょうじょう", "で", "わいん", "を", "ひとくち", "のんだ", "たとたんに", "、", "めまい", "が", "した"]
        },
        {
            "id": 10,
            "pola": "3. ～たとたん（に）",
            "kanji": "結婚した途端に...",
            "hiragana": "けっこん する まえ は やさしかった おっと は、けっこん した たとたん に たいど が かわった",
            "arti": "Suami yang dulu ramah sebelum menikah, begitu menikah sikapnya langsung berubah.",
            "soal": ["おっと", "が", "かわった", "たいど", "やさしかった", "たとたん", "けっこん", "は", "が", "、", "、", "に", "けっこん", "した", "まえ", "は"],
            "kunci": ["けっこん", "する", "まえ", "は", "やさしかった", "おっと", "は", "、", "けっこん", "した", "たとたん", "に", "たいど", "が", "かわった"]
        },
        {
            "id": 11,
            "pola": "3. ～たとたん（に）",
            "kanji": "母の声を聴いた途端に...",
            "hiragana": "くに の はは に でんわ を かけた、はは の こえ を きいた たとたん に なみだ が あふれてきた",
            "arti": "Begitu menelpon ibu di kampung halaman dan mendengar suaranya, air mata langsung menetes.",
            "soal": ["でんわ", "はは", "を", "かけた", "たとたん", "の", "あふれてきた", "なみだ", "に", "はは", "くに", "こえ", "きいた", "の", "が", "、", "を", "、"],
            "kunci": ["くに", "の", "はは", "に", "でんわ", "を", "かけた", "、", "はは", "の", "こえ", "を", "きいた", "たとたん", "に", "なみだ", "が", "あふれてきた"]
        },
        {
            "id": 12,
            "pola": "3. ～たとたん（に）",
            "kanji": "「さよなら」と言った途端...",
            "hiragana": "かのじょ は 「さよなら」 と いった たとたん ぼく は はしって いってしまった",
            "arti": "Begitu dia mengucapkan 'selamat tinggal', saya langsung berlari pergi.",
            "soal": ["はしって", "いった", "「 さよなら 」", "かのじょ", "たとたん", "ぼく", "は", "と", "が", "いってしまった", "、", "は"],
            "kunci": ["かのじょ", "は", "「 さよなら 」", "と", "いった", "たとたん", "ぼく", "は", "はしって", "いってしまった"]
        },

        # ==================== POIN 4 ====================
        {
            "id": 13,
            "pola": "4. ～（か）と思うと・～（か）と思ったら",
            "kanji": "部屋に入ってきたかと思うと...",
            "hiragana": "はやしさん は へや に はいってきた とおもうと、いきなり まど を ぜんぶ あけた",
            "arti": "Begitu Hayashi-san masuk ke kamar, dia secara tiba-tiba langsung membuka semua jendela.",
            "soal": ["はいってきた", "あけた", "まど", "はやしさん", "とおもうと", "へや", "いきなり", "は", "を", "に", "ぜんぶ", "、", "、"],
            "kunci": ["はやしさん", "は", "へや", "に", "はいってきた", "とおもうと", "、", "いきなり", "まど", "を", "ぜんぶ", "あけた"]
        },
        {
            "id": 14,
            "pola": "4. ～（か）と思うと・～（か）と思ったら",
            "kanji": "笑っているかと思ったら...",
            "hiragana": "あかちゃん は いま わらっている とおもったら、もう ないた",
            "arti": "Bayi itu baru saja tertawa, tetapi dalam sekejap sudah menangis lagi.",
            "soal": ["わらっている", "いま", "とおもったら", "もう", "あかちゃん", "ないた", "は", "、", "は"],
            "kunci": ["あかちゃん", "は", "いま", "わらっている", "とおもったら", "、", "もう", "ないた"]
        },
        {
            "id": 15,
            "pola": "4. ～（か）と思うと・～（か）と思ったら",
            "kanji": "片付いたかと思ったら...",
            "hiragana": "こどもたち が ちらかした へや が やっと かたづいた とおもったら、また すぐ ちらかした",
            "arti": "Kamar yang berantakan oleh anak-anak baru saja selesai dirapikan, eh langsung berantakan lagi.",
            "soal": ["ちらかした", "へや", "やっと", "が", "こどもたち", "かたづいた", "とおもったら", "すぐ", "が", "また", "か", "、", "、"],
            "kunci": ["こどもたち", "が", "ちらかした", "へや", "が", "やっと", "かたづいた", "か", "とおもったら", "、", "また", "すぐ", "ちらかした"]
        },
        {
            "id": 16,
            "pola": "4. ～（か）と思うと・～（か）と思ったら",
            "kanji": "涼しくなったかと思ったら...",
            "hiragana": "このごろ は きのう は すずしい とおもったら、きょう は きおん の さ が おおきい あつくなった",
            "arti": "Akhir-akhir ini, kalau kemarin terasa sejuk, hari ini malah mendadak panas dengan perbedaan suhu yang besar.",
            "soal": ["きょう", "このごろ", "さ", "おおきい", "すずしい", "きおん", "あつくなった", "きのう", "が", "は", "は", "とおもったら", "か", "、", "。", "は"],
            "kunci": ["このごろ", "は", "きのう", "は", "すずしい", "か", "とおもったら", "、", "きょう", "は", "きおん", "の", "さ", "が", "おおきい", "あつくなった"]
        },

        # ==================== POIN 5 ====================
        {
            "id": 17,
            "pola": "5. ～か～ないかのうちに",
            "kanji": "横になるかないかのうちに...",
            "hiragana": "いちろう は べっど に よこになる か ないかのうちに、ぐっすり ねむってしまった",
            "arti": "Ichiro baru saja berbaring di tempat tidur, langsung tertidur pulas.",
            "soal": ["よこになる", "ねむってしまった", "いちろう", "べっど", "ないかのうちに", "は", "か", "ぐっすり", "に", "、"],
            "kunci": ["いちろう", "は", "べっど", "に", "よこになる", "か", "ないかのうちに", "、", "ぐっすり", "ねむってしまった"]
        },
        {
            "id": 18,
            "pola": "5. ～か～ないかのうちに",
            "kanji": "夜が明けないかないかのうちに...",
            "hiragana": "わたし は よる が あけない か ないかのうちに いえ を でて、くうこう へ むかった",
            "arti": "Saat hari bahkan belum sepenuhnya terang, saya sudah keluar rumah menuju bandara.",
            "soal": ["むかった", "くうこう", "よる", "あけた", "わたし", "いえ", "でて", "ないかのうちに", "へ", "は", "か", "を", "あけない", "、", "が", "、"],
            "kunci": ["わたし", "は", "よる", "が", "あけない", "か", "ないかのうちに", "、", "いえ", "を", "でて", "、", "くうこう", "へ", "むかった"]
        },
        {
            "id": 19,
            "pola": "5. ～か～ないかのうちに",
            "kanji": "話題作を発表したかないかのうちに...",
            "hiragana": "あの うれっこ さっか は いま の わだいさく を はっぴょうした か ないかのうちに、もう つぎ の さくひん に とりかかっている そうだ",
            "arti": "Penulis populer itu kabarnya baru saja merilis karya hangat saat ini, tetapi sudah mulai mengerjakan karya berikutnya.",
            "soal": ["あの", "いま", "とりかかっている", "わだいさく", "うれっこ", "さくひん", "だ", "はっぴょうした", "そうだ", "さっか", "つぎ", "に", "か", "もう", "は", "ないかのうちに", "し", "の", "を", "、", "。"],
            "kunci": ["あの", "うれっこ", "さっか", "は", "いま", "の", "わだいさく", "を", "はっぴょうした", "か", "ないかのうちに", "、", "もう", "つぎ", "の", "さくひん", "に", "とりかかっている", "そうだ"]
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

# Memasukkan kata langsung dari array `soal` tanpa dirubah urutannya
if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

# --- CSS KHUSUS SOLUSI TEKS TERPOTONG TITIK-TITIK (...) DI HP/PERANGKAT LAIN ---
st.markdown("""
<style>
    div[data-testid="stStatusWidget"] + div div[data-testid="stWidgetLabel"] {
        display: none;
    }
    
    /* Papan Kolom Fleksibel */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
    }
    
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 21% !important; 
        min-width: 0 !important;
    }
    
    /* MENGATASI SOLUSI TITIK-TITIK: Teks dipaksa membungkus (wrap) ke bawah */
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 4px 2px !important;
        font-size: clamp(0.65rem, 2.2vw, 0.88rem) !important;
        line-height: 1.25 !important;
        height: auto !important;
        min-height: 42px !important;
        white-space: normal !important;
        word-break: break-all !important;
    }

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

# Tampilan Header
st.title("🦉 Bunpou Master")
st.caption(f"Soal {st.session_state.index_soal + 1} dari {len(st.session_state.database_soal)}")
st.markdown("---")

# Petunjuk Soal
st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">🇮🇩 {soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- RENDERING KUIS UTAMA ---
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
            st.markdown(f'<div class="swap-indicator">📍 Kata [{kata_terpilih}] terpilih. Klik kata tujuan untuk menukar!</div>', unsafe_allow_html=True)
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

    # 2. BANK KATA PILIHAN
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
        st.success(f"🎉 **正解 (Benar)!** Susunan bunpou kamu sudah sempurna!\n\n**🇯🇵 Kanji/Kalimat:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n**Susunan yang benar:**\n\n`{' '.join(kunci_strings)}`\n\n**🇯🇵 Kanji/Kalimat:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")

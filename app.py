import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 2", layout="centered")

# --- DATABASE SOAL (BAB 2: POIN 1 - 6 EXPLICIT MATCH) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # ==================== POIN 1: ～最中だ ====================
        {
            "id": 1,
            "pola": "1. ～最中だ",
            "kanji": "田中さんは今かんがえごとをしている最中だから、じゃましないほうがいい。",
            "hiragana": "たなかさんはいまかんがえごとをしているさいちゅうだから、じゃましないほうがいい。",
            "arti": "Tanaka-san sedang berpikir/melamun sekarang, jadi sebaiknya jangan diganggu.",
            "soal": ["いま", "は", "かんがえごと", "いい", "たなかさん", "ほう が", "から", "じゃましない", "さいちゅうだ", "を している", "、"],
            "kunci": ["たなかさん", "は", "いま", "かんがえごと", "を している", "さいちゅうだ", "から", "、", "じゃましない", "ほう が", "いい"]
        },
        {
            "id": 2,
            "pola": "1. ～最中だ",
            "kanji": "浜辺でバーベキューをやっている最中に、急に雨が降り出した。",
            "hiragana": "はまべでばーべきゅーをやっているさいちゅうに、きゅうにあめがふりだした。",
            "arti": "Di tengah-tengah mengadakan barbekyu di pantai, tiba-tiba hujan mulai turun.",
            "soal": ["きゅうに", "を やっている", "ばーべきゅー", "さいちゅうに", "ふりだした", "あめ が", "はまべ で", "、"],
            "kunci": ["はまべ で", "ばーべきゅー", "を やっている", "さいちゅうに", "、", "きゅうに", "あめ が", "ふりだした"]
        },
        {
            "id": 3,
            "pola": "1. ～最中だ",
            "kanji": "スピーチの最中に、突然電気を消えた。",
            "hiragana": "すぴーちのさいちゅうに、とつぜんでんきがきえた。",
            "arti": "Di tengah-tengah pidato, tiba-tiba lampunya padam.",
            "soal": ["とつぜん", "すぴーち", "きえた", "でんき が", "さいちゅうに", "の", "、"],
            "kunci": ["すぴーち", "の", "さいちゅうに", "、", "とつぜん", "でんき が", "きえた"]
        },

        # ==================== POIN 2: ～うちに ====================
        {
            "id": 4,
            "pola": "2. ～うちに",
            "kanji": "子供が眠っているうちに、家事を全部やってしまった。",
            "hiragana": "こどもがねむっているうちに、かじをぜんぶやってしまった。",
            "arti": "Selagi anak sedang tidur, saya menyelesaikan semua pekerjaan rumah.",
            "soal": ["かじ", "ねむっている", "うちに", "は", "ぜんぶ", "こども が", "やっ てしまった", "、"],
            "kunci": ["こども が", "ねむっている", "うちに", "、", "かじ", "は", "ぜんぶ", "やっ てしまった"]
        },
        {
            "id": 5,
            "pola": "2. ～うちに",
            "kanji": "忘れないうちに、カレンダーにメモしておこう。",
            "hiragana": "わすれないうちに、かれんだーにめもしておこう。",
            "arti": "Mumpung belum lupa, mari kita catat di kalender terlebih dahulu.",
            "soal": ["かれんだー", "めもして おこう", "に", "うちに", "わすれ ない", "、"],
            "kunci": ["わすれ ない", "うちに", "、", "かれんだー", "に", "めもして おこう"]
        },
        {
            "id": 6,
            "pola": "2. ～うちに",
            "kanji": "足が丈夫なうちに、ヒマラヤ登山を計画したい。",
            "hiragana": "あしがじょうぶなうちに、ひまらやとざんをけいかくしたい。",
            "arti": "Mumpung kaki masih kuat, saya ingin merencanakan pendakian gunung Himalaya.",
            "soal": ["けいかくしたい", "うちに", "ひまらやとざん", "じょうぶな", "あし が", "を", "、"],
            "kunci": ["あし が", "じょうぶな", "うちに", "、", "ひまらやとざん", "を", "けいかくしたい"]
        },
        {
            "id": 7,
            "pola": "2. ～うちに",
            "kanji": "学生のうちに、車の運転免許をとろうと思っております。",
            "hiragana": "がくせいのうちに、くるまのうんてんめんきょをとろうとおもっております。",
            "arti": "Selagi masih menjadi mahasiswa, saya berniat untuk mengambil SIM mobil.",
            "soal": ["めんきょ", "くるま", "うんてん", "がくせい", "うちに", "とおもっております", "の", "を", "とろう", "の", "、"],
            "kunci": ["がくせい", "の", "うちに", "、", "くるま", "の", "うんてん", "めんきょ", "を", "とろう", "とおもっております"]
        },
        {
            "id": 8,
            "pola": "2. ～うちに",
            "kanji": "インターネットで調べているうちに、いろいろなことがわかってきた。",
            "hiragana": "いんたーねっとでしらべているうちに、いろいろなことがわかってきた。",
            "arti": "Selagi mencari-cari di internet, saya jadi mengetahui berbagai macam hal.",
            "soal": ["しらべている", "わかってきた", "いろいろな こと", "いんたーねっと", "うちに", "で", "が", "、"],
            "kunci": ["いんたーねっと", "で", "しらべている", "うちに", "、", "いろいろな こと", "が", "わかってきた"]
        },
        {
            "id": 9,
            "pola": "2. ～うちに",
            "kanji": "この携帯電話は長い間使っているうちに、もう自分の体の一部のようなった。",
            "hiragana": "このけいたいでんわはながいあいだつかっているうちに、もうじぶんのからだのいちぶのようなった。",
            "arti": "Ponsel ini seiring makin lama digunakan, rasanya sudah menjadi seperti bagian dari tubuh sendiri.",
            "soal": ["けいたいでんわ", "この", "うちに", "いちぶ", "じぶん", "もう", "ように なった", "の", "ながいあいだ", "つかっている", "は", "からだ の", "、"],
            "kunci": ["この", "けいたいでんわ", "は", "ながいあいだ", "つかっている", "うちに", "、", "もう", "じぶん", "の", "からだ の", "いちぶ", "ように なった"]
        },
        {
            "id": 10,
            "pola": "2. ～うちに",
            "kanji": "知らないうちに、雨が降り始めていた。",
            "hiragana": "しらないうちに、あめがふりはじめていた。",
            "arti": "Tanpa disadari, hujan sudah mulai turun.",
            "soal": ["あめ が", "しらない", "ふりはじめていた", "うちに", "、"],
            "kunci": ["しらない", "うちに", "、", "あめ が", "ふりはじめていた"]
        },

        # ==================== POIN 3: ～ばかりだ・～一方だ ====================
        {
            "id": 11,
            "pola": "3. ～ばかりだ・～一方だ",
            "kanji": "この頃は残業が多くて、仕事が増えるばかりだ。",
            "hiragana": "このごろはざんぎょうがおおくて、しごとがふえるばかりだ。",
            "arti": "Akhir-akhir ini lemburan banyak, dan pekerjaan terus-menerus bertambah.",
            "soal": ["このごろ", "ざんぎょう", "は", "ふえる", "おおくて", "しごと が", "ばかりだ", "、"],
            "kunci": ["このごろ", "は", "ざんぎょう", "が", "おおくて", "、", "しごと が", "ふえる", "ばかりだ"]
        },
        {
            "id": 12,
            "pola": "3. ～ばかりだ・～一方だ",
            "kanji": "東京の交通機関は複雑になるばかりで、わたしはよくわからなくなってきた。",
            "hiragana": "とうきょうのこうつうきかんはふくざつになるばかりで、わたしはよくわからなくなってきた。",
            "arti": "Sistem transportasi Tokyo makin lama makin rumit saja, saya jadi makin tidak paham.",
            "soal": ["とうきょう", "こうつうきかん", "ふくざつになる", "わたし", "は", "わからなくなってきた", "ばかりで", "の", "は", "よく", "、"],
            "kunci": ["とうきょう", "の", "こうつうきかん", "は", "ふくざつになる", "ばかりで", "、", "わたし", "は", "よく", "わからなくなってきた"]
        },
        {
            "id": 13,
            "pola": "3. ～ばかりだ・～一方だ",
            "kanji": "彼との人間関係は一度問題が起きてから、悪くなる一方だ。",
            "hiragana": "かれとのにんげんかんけいはいちどもんだいがおきてから、わるくなるいっぽうだ。",
            "arti": "Hubungan dengannya sejak pernah terjadi masalah sekali, makin lama makin memburuk.",
            "soal": ["かれ", "わるくなる", "いちど", "にんげんかんけい", "もんだい", "は", "いっぽうだ", "から", "と の", "が", "おきて", "、"],
            "kunci": ["かれ", "と の", "にんげんかんけい", "は", "いちど", "もんだい", "が", "おきて", "から", "、", "わるくなる", "いっぽうだ"]
        },
        {
            "id": 14,
            "pola": "3. ～ばかりだ・～一方だ",
            "kanji": "牛の病気が国中広がる一方なので、人や心配している。",
            "hiragana": "うしのびょうきがくにじゅうひろがるいっぽうなので、ひとがしんぱいしている。",
            "arti": "Karena penyakit sapi terus-menerus menyebar ke seluruh negeri, orang-orang menjadi cemas.",
            "soal": ["しんぱいしている", "くにじゅう", "ひろがる", "うし", "びょうき", "いっぽう なので", "の", "や", "ひと が", "が", "、"],
            "kunci": ["うし", "の", "びょうき", "が", "くにじゅう", "ひろがる", "いっぽう なので", "、", "ひと が", "や", "しんぱいしている"]
        },

        # ==================== POIN 4: ～（よ）うとしている ====================
        {
            "id": 15,
            "pola": "4. ～（よ）うとしている",
            "kanji": "さあ、いま決勝戦が始まろう me! としています。みんな緊張しています。",
            "hiragana": "さあ、いまけっしょうせんがはじまろうとしています。みんなきんちょうしています。",
            "arti": "Nah, sebentar lagi babak final akan segera dimulai. Semuanya tampak tegang.",
            "soal": ["いま", "さあ", "きんちょうしています", "はじまろう", "みんな", "けっしょうせん が", "としています", "、", "。"],
            "kunci": ["さあ", "、", "いま", "けっしょうせん が", "はじまろう", "としています", "。", "みんな", "きんちょうしています"]
        },
        {
            "id": 16,
            "pola": "4. ～（よ）うとしている",
            "kanji": "駅前に高級マンションが完成しようとしている。",
            "hiragana": "えきまえにこうきゅうまんしょんがかんせいしようとしている。",
            "arti": "Apartemen mewah di depan stasiun akan segera selesai dibangun.",
            "soal": ["かんせい", "さんじゅうかいだて", "えきまえ", "こうきゅうまんしょん", "に", "しよう", "の", "が", "としている", "。"],
            "kunci": ["えきまえ", "に", "こうきゅうまんしょん", "が", "かんせい", "しよう", "としている", "。"]
        },
        {
            "id": 17,
            "pola": "4. ～（よ）うとしている",
            "kanji": "桜が満開になろうとしているとき、雪が降った。",
            "hiragana": "さくらがまんかいになろうとしているとき、ゆきがふった。",
            "arti": "Saat bunga sakura hendak mekar sempurna, salju malah turun.",
            "soal": ["まんかい に", "ゆき が", "さくら が", "としている とき", "なろう", "ふった", "、"],
            "kunci": ["さくら が", "まんかい に", "なろう", "としている とき", "、", "ゆき が", "ふった"]
        },

        # ==================== POIN 5: ～つつある ====================
        {
            "id": 18,
            "pola": "5. ～つつある",
            "kanji": "次第にあたたかくなりつつあります。春はもうすぐです。",
            "hiragana": "しだいにあたたかくなりつつあります。はるはもうすぐです。",
            "arti": "Perlahan-lahan cuaca makin hangat. Musim semi sudah dekat.",
            "soal": ["はる", "しだい に", "あたたかく", "あり ます", "は", "つつ", "もうすぐです", "、", "。"],
            "kunci": ["しだい に", "あたたかく", "つつ", "あり ます", "、", "はる", "は", "もうすぐです", "。"]
        },
        {
            "id": 19,
            "pola": "5. ～つつある",
            "kanji": "現在この会社は発展しつつあり、将来が期待される。",
            "hiragana": "げんざいこのかいしゃははってんしつつあり、しょうらいがきたいされる。",
            "arti": "Saat ini perusahaan ini sedang berkembang, dan masa depannya sangat diharapkan.",
            "soal": ["きたいされる", "かいしゃ", "げんざい", "しょうらい が", "この", "は", "はってんし", "つつあり", "、"],
            "kunci": ["げんざい", "この", "かいしゃ", "は", "はってんし", "つつあり", "、", "しょうらい が", "きたいされる"]
        },
        {
            "id": 20,
            "pola": "5. ～つつある",
            "kanji": "明治時代のはじめ、日本は急速に近代化しつつあった。",
            "hiragana": "めいじじだいのはじめ、にほんはきゅうそくにきんだいかしつつあった。",
            "arti": "Pada awal zaman Meiji, Jepang sedang dalam proses modernisasi secara pesat.",
            "soal": ["きんだいかし", "にほん", "つつあった", "きゅうそく に", "めいじじだい", "の", "はじめ", "は", "、"],
            "kunci": ["めいじじだい", "の", "はじめ", "、", "にほん", "は", "きゅうそく に", "きんだいかし", "つつあった"]
        },

        # ==================== POIN 6: ～つつ ====================
        {
            "id": 21,
            "pola": "6. ～つつ",
            "kanji": "この空地をどうするかについては、住民と話し合いつつ計画をたてていきたい。",
            "hiragana": "このあきちをどうするかについては、じゅうみんとはなし合いつつけいかくをたてていきたい。",
            "arti": "Mengenai lahan kosong ini hendak dijadikan apa, kami ingin menyusun rencana sambil berdiskusi dengan warga.",
            "soal": ["この", "について は", "じゅうみん", "はなしあい", "どうするか", "けいかく", "あきち", "を", "と", "つつ", "を", "たてていきたい", "、"],
            "kunci": ["この", "あきち", "を", "どうするか", "について は", "、", "じゅうみん", "と", "はなしあい", "つつ", "けいかく", "を", "たてていきたい"]
        },
        {
            "id": 22,
            "pola": "6. ～つつ",
            "kanji": "将来の進路など、仕事のことお金のことつつ考え、を選ばなければならない。",
            "hiragana": "しょうらいのしんろなど、しごとのことおかねのことつつかんがえ、をえらばなければならない。",
            "arti": "Mengenai masa depan seperti jalur karir, kita harus memilih sambil mempertimbangkan hal pekerjaan dan keuangan.",
            "soal": ["しょうらい", "しんろ", "など", "かんがえ", "を", "おかね", "しごと", "の", "を", "えらばなければならない", "の", "こと", "こと", "つつ", "、"],
            "kunci": ["しょうらい", "の", "しんろ", "など", "、", "しごと", "の", "こと", "おかね", "の", "こと", "つつ", "かんがえ", "を", "えらばなければならない"]
        },
        {
            "id": 23,
            "pola": "6. ～つつ",
            "kanji": "いろいろな体験を楽しみつつ、日本の生活になれていった。",
            "hiragana": "いろいろないたいけんをたのしみつつ、にほんのせいかつになれていった。",
            "arti": "Sambil menikmati berbagai pengalaman, saya menjadi terbiasa dengan kehidupan di Jepang.",
            "soal": ["たいけん", "たのしみ", "せいかつ に", "にほん", "いろいろな", "なれていった", "の", "つつ", "、"],
            "kunci": ["いろいろな", "たいけん", "を", "たのしみ", "つつ", "、", "にほん", "の", "せいかつ に", "なれていった"]
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
    import random
    soal_acak = list(soal_sekarang["soal"])
    random.seed(42)
    random.shuffle(soal_acak)
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_acak)]

# --- STYLING CSS TERBAIK UNTUK HP & DESKTOP ---
st.markdown("""
<style>
    div[data-testid="stStatusWidget"] + div div[data-testid="stWidgetLabel"] {
        display: none;
    }
    
    /* Menjaga 4 Kolom di Layar Lebar & HP */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 4px !important;
    }
    
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 23% !important; 
        min-width: 0 !important; /* Mencegah kolom meluber di HP */
    }
    
    /* Tombol Pilihan Kata Otomatis Menyesuaikan Font di HP */
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 4px 2px !important; /* Padding minimalis agar teks panjang muat */
        font-size: clamp(0.7rem, 2.5vw, 0.95rem) !important; /* Ukuran teks dinamis sesuai HP */
        white-space: normal !important; /* Kata panjang berganti baris jika dibutuhkan */
        word-break: break-word !important;
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
st.title("🦉 Bunpou Master (BAB 2)")
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

    # 2. BANK KATA PILIHAN (Layout Normal 4 Kolom Kiri ke Kanan)
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

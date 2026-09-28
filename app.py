import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang", layout="centered")

# --- DATABASE SOAL (DIPERBARUI DENGAN 5 POLA) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # === POLA 1: ～てはじめて ===
        {
            "id": 1,
            "pola": "1. ～てはじめて",
            "kanji": "実際に現地の様子を見てはじめて、今回の地震のひどさを知った。",
            "hiragana": "じっさいに げんちの ようすを みてはじめて、 こんかいの じしんの ひどさを しった。",
            "arti": "Baru setelah melihat langsung kondisi di lokasi, saya menyadari betapa parahnya gempa kali ini.",
            "kunci": ["実際", "に", "現地", "の", "様子", "を", "見て", "はじめて", "、", "今回", "の", "地震", "の", "ひどさ", "を", "知った", "。"],
            "soal": ["じしん", "じっさい", "みて", "こんかい", "の", "げんち", "はじめて", "しった", "ひどさ", "に", "を", "ようす", "の", "の", "を", "、"]
        },
        {
            "id": 2,
            "pola": "1. ～てはじめて",
            "kanji": "相手の話の途中で話を始めるくせがあると、人に言われてはじめて気がついた。",
            "hiragana": "あいての はなしの とちゅうで はなしを はじめる くせが あると、 ひとに いわれて はじめて きがついた。",
            "arti": "Baru setelah diberi tahu orang lain, saya sadar bahwa saya punya kebiasaan memotong pembicaraan orang.",
            "kunci": ["相手", "の", "話", "の", "途中", "で", "話", "を", "始める", "くせ", "が", "ある", "と", "、", "人", "に", "言われて", "はじめて", "気がついた", "。"],
            "soal": ["いわれて", "はなし", "ある", "ひと", "で", "くせ", "はなし", "の", "あいて", "きがついた", "の", "が", "はじめる", "に", "とちゅう", "を", "と", "はじめて", "、"]
        },
        {
            "id": 3,
            "pola": "1. ～てはじめて",
            "kanji": "山田先生の指導を受けてはじめて、生物の観察が面白いと思うようになった。",
            "hiragana": "やまだせんせいの しどうを うけてはじめて、 せいぶつの かんさつが おもしろいと おもうようになった。",
            "arti": "Baru setelah mendapat bimbingan dari Pak/Bu Guru Yamada, saya mulai merasa bahwa mengamati makhluk hidup itu menarik.",
            "kunci": ["山田先生", "の", "指導", "を", "受けて", "はじめて", "、", "生物", "の", "観察", "が", "面白い", "と", "思うようになった", "。"],
            "soal": ["かんさつ", "うけて", "の", "おもしろい", "せいぶつ", "しどう", "と", "やまだ", "を", "おもうようになった", "せんせい", "が", "はじめて", "の", "、"]
        },
        {
            "id": 4,
            "pola": "1. ～てはじめて",
            "kanji": "チャンスがあってはじめて、才能が生きてくるのではないだろうか。",
            "hiragana": "チャンスが あってはじめて、 さいのうが いきてくるのではないだろうか。",
            "arti": "Bukankah bakat baru akan berkembang setelah ada kesempatan?",
            "kunci": ["チャンス", "が", "あって", "はじめて", "、", "才能", "が", "生きてくる", "の", "ではないだろうか", "。"],
            "soal": ["いきてくる", "はじめて", "あって", "ではないだろうか", "チャンス", "が", "さいのう", "の", "が", "、"]
        },

        # === POLA 2: ～上（で） ===
        {
            "id": 5,
            "pola": "2. ～上（で）",
            "kanji": "文書が保存されていることを確かめた上で、パソコンをシャットダウンしてください。",
            "hiragana": "ぶんしょが ほぞんされている ことを たしかめたうえで、 パソコンを シャットダウン してください。",
            "arti": "Harap matikan komputer setelah memastikan dokumen telah disimpan.",
            "kunci": ["文書", "が", "保存されている", "こと", "を", "確かめた", "上", "で", "、", "パソコン", "を", "シャットダウン", "してください", "。"],
            "soal": ["シャットダウン", "パソコン", "ほぞんされている", "うえ", "たしかめた", "ぶんしょ", "を", "で", "してください", "こと", "が", "を", "、"]
        },
        {
            "id": 6,
            "pola": "2. ～上（で）",
            "kanji": "経済的なことをよく考えた上で、進路を決める必要がある。",
            "hiragana": "けいざいてきな ことを よく かんがえたうえで、 しんろを きめる ひつようが ある。",
            "arti": "Perlu memutuskan jalan masa depan setelah memikirkan masalah keuangan dengan matang.",
            "kunci": ["経済的な", "こと", "を", "よく", "考えた", "上", "で", "、", "進路", "を", "決める", "必要", "が", "ある", "。"],
            "soal": ["きめる", "うえ", "けいざいてきな", "ひつよう", "かんがえた", "よく", "を", "しんろ", "が", "で", "こと", "を", "ある", "、"]
        },
        {
            "id": 7,
            "pola": "2. ～上（で）",
            "kanji": "自分一人では決められませんので、家族と相談した上で、お返事をいたします。",
            "hiragana": "じぶん ひとりでは きめられませんので、 かぞくと そうだんしたうえで、 おへんじを いたします。",
            "arti": "Karena tidak bisa memutuskan sendiri, saya akan memberikan jawaban setelah berdiskusi dengan keluarga.",
            "kunci": ["自分", "一人", "では", "決められません", "ので", "、", "家族", "と", "相談した", "上", "で", "、", "お返事", "を", "いたします", "。"],
            "soal": ["そうだんした", "を", "きめられません", "かぞく", "じぶん", "で", "ので", "ひとり", "おへんじ", "うえ", "いたします", "と", "で", "では", "、", "、"]
        },
        {
            "id": 8,
            "pola": "2. ～上（で）",
            "kanji": "この列車には特急券が必要です。あらかじめ特急券をお買い求めの上、ご乗車ください。",
            "hiragana": "この れっしゃには とっきゅうけんが ひつようです。 あらかじめ とっきゅうけんを おかいもとめのうえ、 ごじょうしゃください。",
            "arti": "Kereta ini memerlukan tiket ekspres terbatas. Silakan naik setelah membeli tiket terlebih dahulu.",
            "kunci": ["この", "列車", "には", "特急券", "が", "必要", "です", "。", "あらかじめ", "特急券", "を", "お買い求め", "の", "上", "、", "ご乗車", "ください", "。"],
            "soal": ["ごじょうしゃ", "この", "ひつよう", "とっきゅうけん", "です", "おかいもとめ", "れっしゃ", "を", "あらかじめ", "うえ", "が", "には", "ください", "とっきゅうけん", "の", "、"]
        },

        # === POLA 3: ～次第（しだい） ===
        {
            "id": 9,
            "pola": "3. ～次第（しだい）",
            "kanji": "詳しいことがわかり次第、ご連絡いたします。",
            "hiragana": "くわしい ことが わかりしだい、 ごれんらく いたします。",
            "arti": "Segera setelah informasi detailnya diketahui, kami akan menghubungi Anda.",
            "kunci": ["詳しい", "こと", "が", "わかり", "次第", "、", "ご連絡", "いたします", "。"],
            "soal": ["ごれんらく", "わかり", "じだい", "いたします", "が", "くわしい", "こと", "しだい", "、"]
        },
        {
            "id": 10,
            "pola": "3. ～次第（しだい）",
            "kanji": "定員になり次第、締め切らせていただきます。",
            "hiragana": "ていいんに なりしだい、 しめきらせて いただきます。",
            "arti": "Pendaftaran akan ditutup segera setelah kuota terpenuhi.",
            "kunci": ["定員", "に", "なり", "次第", "、", "締め切らせて", "いただきます", "。"],
            "soal": ["いただきます", "ていいん", "しめきらせて", "に", "なり", "しだい", "、"]
        },
        {
            "id": 11,
            "pola": "3. ～次第（しだい）",
            "kanji": "会場の準備ができ次第、ご案内いたします。もうしばらくお待ちください。",
            "hiragana": "かいじょうの じゅんびが できしだい、 ごあんない いたします。 もう しばらく おまち ください。",
            "arti": "Segera setelah persiapan tempat selesai, kami akan memandu Anda. Mohon tunggu sebentar lagi.",
            "kunci": ["会場", "の", "準備", "が", "でき", "次第", "、", "ご案内", "いたします", "。", "もう", "しばらく", "お待ち", "ください", "。"],
            "soal": ["おまち", "でき", "じゅんび", "いたします", "しだい", "もう", "かいじょう", "ください", "ごあんない", "が", "の", "しばらく", "、"]
        },

        # === POLA 4: ～て以来・・～てこのかた ===
        {
            "id": 12,
            "pola": "4. ～て以来・・～てこのかた",
            "kanji": "1年前にけがをして以来、体の調子がどうも良くない。",
            "hiragana": "いちねんまえに けがを していらい、 からだの ちょうしが どうも よくない。",
            "arti": "Sejak mengalami cedera satu tahun yang lalu, kondisi tubuh saya sepertinya kurang baik.",
            "kunci": ["1年前", "に", "けが", "を", "して", "以来", "、", "体", "の", "調子", "が", "どうも", "良くない", "。"],
            "soal": ["ちょうし", "いちねんまえ", "ない", "を", "して", "の", "いらい", "からだ", "どうも", "よく", "が", "に", "けが", "、"]
        },
        {
            "id": 13,
            "pola": "4. ～て以来・・～てこのかた",
            "kanji": "あの山の写真を見て以来、いつかは登ってみたいとずっと思い続けてきた。",
            "hiragana": "あの やまの しゃしんを みていらい、 いつかは のぼってみたいと ずっと おもいつづけてきた。",
            "arti": "Sejak melihat foto gunung itu, saya terus berpikir dan berharap suatu saat nanti ingin memanjatnya.",
            "kunci": ["あの", "山", "の", "写真", "を", "見て", "以来", "、", "いつか", "は", "登ってみたい", "と", "ずっと", "思い続けてきた", "。"],
            "soal": ["おもい", "のぼって", "しゃしん", "きた", "みて", "いらい", "みたい", "いつか", "の", "やま", "は", "つづけて", "あの", "を", "ずっと", "と", "、"]
        },
        {
            "id": 14,
            "pola": "4. ～て以来・・～てこのかた",
            "kanji": "子供が生まれて以来、外でお酒を飲んでいない。",
            "hiragana": "こどもが うまれていらい、 そとで さけを のんでいない。",
            "arti": "Sejak anak saya lahir, saya tidak pernah minum alkohol di luar rumah.",
            "kunci": ["子供", "が", "生まれて", "以来", "、", "外", "で", "お酒", "を", "飲んでいない", "。"],
            "soal": ["いらい", "で", "のんで", "うまれ", "さけ", "て", "こども", "そと", "が", "いない", "を", "、"]
        },
        {
            "id": 15,
            "pola": "4. ～て以来・・～てこのかた",
            "kanji": "日本から帰国してこのかた、毎日日本のことを思いだしている。",
            "hiragana": "にほんから きこくして このかた、 まいにち にほんの ことを おもいだしている。",
            "arti": "Sejak pulang ke negara asal dari Jepang, setiap hari saya selalu teringat tentang Jepang.",
            "kunci": ["日本", "から", "帰国して", "このかた", "、", "毎日", "日本", "の", "こと", "を", "思いだしている", "。"],
            "soal": ["にほん", "きこく", "おもいだしている", "して", "まいにち", "から", "このかた", "にほん", "の", "こと", "を", "、"]
        },
        {
            "id": 16,
            "pola": "4. ～て以来・・～てこのかた",
            "kanji": "母がいなくなってこのかた、母のことを考えない日はない。",
            "hiragana": "ははが いなくなって このかた、 ははの ことを かんがえない ひは ない。",
            "arti": "Sejak ibu tiada/pergi, tidak ada satu hari pun tanpa memikirkan tentang ibu.",
            "kunci": ["母", "が", "いなくなって", "このかた", "、", "母", "の", "こと", "を", "考えない", "日", "は", "ない", "。"],
            "soal": ["かんがえない", "ひ", "はは", "の", "このかた", "は", "ない", "が", "こと", "いなくなって", "はは", "を", "、"]
        },

        # === POLA 5: ～てからでないと・・～てからでなければ ===
        {
            "id": 17,
            "pola": "5. ～てからでないと・・～てからでなければ",
            "kanji": "この果物は赤くなってからでないと、酸っぱくて食べられません。",
            "hiragana": "この くだものは あかくなって からでないと、 すっぱくて たべられません。",
            "arti": "Buah ini jika belum menjadi merah, rasanya masam dan tidak bisa dimakan.",
            "kunci": ["この", "果物", "は", "赤くなって", "からでないと", "、", "酸っぱくて", "食べられません", "。"],
            "soal": ["あかく", "たべられません", "でないと", "この", "なって", "は", "すっぱくて", "くだもの", "から", "、"]
        },
        {
            "id": 18,
            "pola": "5. ～てからでないと・・～てからでなければ",
            "kanji": "もっと情報を集めてからでないと、その話が本当かどうか判断できない。",
            "hiragana": "もっと じょうほうを あつめて からでないと、 その はなしが ほんとうかどうか はんだん できない。",
            "arti": "Jika belum mengumpulkan lebih banyak informasi, kita tidak bisa menilai apakah cerita itu benar atau tidak.",
            "kunci": ["もっと", "情報", "を", "集めて", "からでないと", "、", "その", "話", "が", "本当", "か", "どうか", "判断", "できない", "。"],
            "soal": ["ほんとう", "を", "その", "はんだん", "か", "どうか", "じょうほう", "から", "もっと", "あつめて", "はなし", "できない", "が", "でないと", "、"]
        },
        {
            "id": 19,
            "pola": "5. ～てからでないと・・～てからでなければ",
            "kanji": "この電車は車内の清掃が済んでからでないと、ご乗車になれません。",
            "hiragana": "この でんしゃは しゃないの せいそうが すんで からでないと、 ごじょうしゃに なれません。",
            "arti": "Kereta ini jika pembersihan dalam gerbongnya belum selesai, penumpang belum bisa naik.",
            "kunci": ["この", "電車", "は", "車内", "の", "清掃", "が", "済んで", "からでないと", "、", "ご乗車", "に", "なれません", "。"],
            "soal": ["ごじょうしゃ", "せいそう", "すんで", "でんしゃ", "は", "この", "しゃない", "が", "に", "なれません", "から", "の", "でないと", "、"]
        },
        {
            "id": 20,
            "pola": "5. ～てからでないと・・～てからでなければ",
            "kanji": "退院したばかりなんですから、十分に体力がついてからでなければ、運動は無理ですよ。",
            "hiragana": "たいいんした ばかりなんですから、 じゅうぶんに たいりょくが ついて からでなければ、 うんどうは むりですよ。",
            "arti": "Karena baru saja keluar dari rumah sakit, jika stamina belum benar-benar pulih, berolahraga itu tidak mungkin (tidak boleh).",
            "kunci": ["退院した", "ばかりなんですから", "、", "十分に", "体力", "が", "ついて", "からでなければ", "、", "運動", "は", "無理ですよ", "。"],
            "soal": ["じゅうぶんに", "うんどう", "なんですか", "ついて", "たいりょく", "むり", "たいいん", "でなければ", "ばかり", "ですよ", "は", "が", "から", "した", "、", "、"]
        }
    ]

# Inisialisasi State
if "pola_terpilih" not in st.session_state:
    st.session_state.pola_terpilih = "Semua Pola"

if "index_soal_lokal" not in st.session_state:
    st.session_state.index_soal_lokal = 0

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

# --- CSS KHUSUS TAMPILAN KAPSU/PILL ---
st.markdown("""
<style>
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

    div[data-testid="stHorizontalBlock"] button {
        border-radius: 50px !important;
        border: 1px solid #cccccc !important;
        background-color: #ffffff !important;
        color: #333333 !important;
        font-size: 1.1rem !important;
        padding: 6px 18px !important;
        box-shadow: none !important;
        transition: all 0.2s ease-in-out !important;
    }

    div[data-testid="stHorizontalBlock"] button:hover {
        border-color: #888888 !important;
        background-color: #f7f7f7 !important;
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
st.title("🦉 Bunpou Master")

# --- DROPDOWN PILIH POLA GRAMMAR ---
daftar_pola_unik = list(dict.fromkeys([item["pola"] for item in st.session_state.database_soal]))
opsi_pola = ["Semua Pola"] + daftar_pola_unik

pola_terpilih = st.selectbox(
    "📖 **Pilih Pola Grammar:**",
    options=opsi_pola,
    index=opsi_pola.index(st.session_state.pola_terpilih) if st.session_state.pola_terpilih in opsi_pola else 0,
    key="select_pola"
)

# Cek jika pengguna mengubah filter Pola Grammar
if pola_terpilih != st.session_state.pola_terpilih:
    st.session_state.pola_terpilih = pola_terpilih
    st.session_state.index_soal_lokal = 0
    st.session_state.jawaban_user = []
    st.session_state.bank_kata = []
    st.session_state.idx_kata_dipilih = None
    st.session_state.status_periksa = False
    st.rerun()

# Filter Soal Berdasarkan Pola yang Dipilih
if st.session_state.pola_terpilih == "Semua Pola":
    soal_terfilter = st.session_state.database_soal
else:
    soal_terfilter = [s for s in st.session_state.database_soal if s["pola"] == st.session_state.pola_terpilih]

# Mencegah index melebihi batas jika filter berubah
if st.session_state.index_soal_lokal >= len(soal_terfilter):
    st.session_state.index_soal_lokal = 0

soal_sekarang = soal_terfilter[st.session_state.index_soal_lokal]

# Inisialisasi Bank Kata
if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

st.markdown("---")

# Tampilkan Informasi Jumlah Soal
st.caption(f"Menampilkan Soal **{st.session_state.index_soal_lokal + 1}** dari **{len(soal_terfilter)}** untuk kategori ini (ID Soal: #{soal_sekarang['id']})")

# Kotak Petunjuk Soal
st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">🇮🇩 {soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- MENU UTAMA INTERAKTIF ---
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

    # 2. BANK KATA PILIHAN
    st.write("### Pilihan Kata:")
    
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
        st.session_state.index_soal_lokal = (st.session_state.index_soal_lokal + 1) % len(soal_terfilter)
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

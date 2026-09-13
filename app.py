import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 7", layout="centered")

# --- DATABASE SOAL ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # --- POLA 1 ---
        {
            "id": 1,
            "pola": "Pola 1: ～際（に）",
            "kanji": "この整理券は、商品受け取りの際、必要です。",
            "hiragana": "このせいりけんは、しょうひんうけとりのおさいい、ひつようです。",
            "arti": "Kupon nomor urut ini diperlukan saat menerima barang.",
            "kunci": ["この", "せいりけん", "は", "、", "しょうひん", "うけとり", "の", "さい", "、", "ひつようです", "。"],
            "soal": ["この", "さい", "ひつようです", "うけとり", "しょうひん", "の", "せいりけん", "は", "、", "、"]
        },
        {
            "id": 2,
            "pola": "Pola 1: ～際（に）",
            "kanji": "こちらの会議室をご利用になる際は、受付で必要事項をご記入ください。",
            "hiragana": "こちらのかいぎしつをごりようになるさいは、うけつけでひつようじこうをごきにゅうください。",
            "arti": "Saat akan menggunakan ruang rapat ini, harap isi data yang diperlukan di resepsionis.",
            "kunci": ["こちら", "の", "かいぎしつ", "を", "ごりよう", "になる", "さい", "は", "、", "うけつけ", "で", "ひつようじこう", "を", "ごきにゅうください", "。"],
            "soal": ["ひつようじこう", "を", "うけつけ", "かいぎしつ", "に", "こちら", "で", "さい", "の", "ごきにゅうください", "ごりよう", "は", "、", "、", "になる"]
        },
        {
            "id": 3,
            "pola": "Pola 1: ～際（に）",
            "kanji": "アメリカの大統領は来日した際に、わたしたちの大学でスピーチを行った。",
            "hiragana": "あめりかのだいとうりょうはらいにちしたさいに、わたしたちのだいがくですぴーちをおこなった。",
            "arti": "Presiden Amerika menyampaikan pidato di universitas kami saat berkunjung ke Jepang.",
            "kunci": ["あめりか", "の", "だいとうりょう", "は", "らいにち", "した", "さい", "に", "、", "わたしたち", "の", "だいがく", "で", "すぴーち", "を", "おこなった", "。"],
            "soal": ["だいがく", "わたしたち", "だいとうりょう", "で", "すぴーち", "に", "らいにち", "の", "を", "おこなった", "あめりか", "さい", "した", "、"]
        },
        # --- POLA 2 ---
        {
            "id": 4,
            "pola": "Pola 2: ～に際して・～にあたって",
            "kanji": "工事関係者は工事を始めるに際して、近所の住民にあいさつをして回った。",
            "hiragana": "こうじかんけいしゃはこうじをはじめるにさいして、きんじょのじゅうみんにあいさつをしてまわった。",
            "arti": "Pihak konstruksi keliling menyapa warga sekitar saat akan memulai pembangunan.",
            "kunci": ["こうじかんけいしゃ", "は", "こうじ", "を", "はじめる", "にさいして", "、", "きんじょ", "の", "じゅうみん", "に", "あいさつ", "を", "して", "まわった", "。"],
            "soal": ["こうじ", "こうじかんけいしゃ", "に", "まわった", "あいさつ", "を", "きんじょ", "はじめる", "じゅうみん", "にさいして", "の", "は", "して", "、", "、"]
        },
        {
            "id": 5,
            "pola": "Pola 2: ～に際して・～にあたって",
            "kanji": "当ショッピングサイトのご利用に際して、以下のご利用条件をよくお読みください。",
            "hiragana": "とうしょっぴんぐさいとのごり方向にさいして、いかのごりようじょうけんをよくおよみください。",
            "arti": "Saat menggunakan situs belanja ini, harap baca syarat dan ketentuan penggunaan di bawah ini dengan cermat.",
            "kunci": ["とうしょっぴんぐさいと", "の", "ごりよう", "にさいして", "、", "いかの", "ごりようじょうけん", "を", "よく", "およみください", "。"],
            "soal": ["よく", "いかの", "とうしょっぴんぐさいと", "にさいして", "ごりようじょうけん", "およみください", "を", "の", "ごりよう", "、", "、"]
        },
        {
            "id": 6,
            "pola": "Pola 2: ～に際して・～にあたって",
            "kanji": "新しく事業を始めるにあたって、しっかりと準備をしようと思っております。",
            "hiragana": "あたらしくじぎょうをはじめるにあたって、しっかりとじゅんびをしようとおもっております。",
            "arti": "Dalam rangka memulai bisnis baru, saya berniat untuk melakukan persiapan dengan matang.",
            "kunci": ["あたらしく", "じぎょう", "を", "はじめる", "にあたって", "、", "しっかり", "と", "じゅんび", "を", "しよう", "と", "おもっております", "。"],
            "soal": ["じぎょう", "じゅんび", "しっかり", "を", "あたって", "に", "はじめる", "あたらしく", "とおもっております", "しよう", "、", "、"]
        },
        {
            "id": 7,
            "pola": "Pola 2: ～に際して・～にあたって",
            "kanji": "お二人の門出にあたりまして、お祝いの言葉を申し上げます。",
            "hiragana": "おふたりのかどであたりまして、おいわいのことばをもうしあげます。",
            "arti": "Menyambut awal lembaran baru kalian berdua, saya menyampaikan ucapan selamat.",
            "kunci": ["おふたりの", "かどで", "に", "あたりまして", "、", "おいわい", "の", "ことば", "を", "もうしあげます", "。"],
            "soal": ["おふたりの", "もうしあげます", "おいわい", "あたりまして", "かどで", "に", "ことば", "を", "、", "、"]
        },
        {
            "id": 8,
            "pola": "Pola 2: ～に際して・～にあたって",
            "kanji": "日本で国際会議を開催するにあたり、関係各方面からの協力を得た。",
            "hiragana": "にほん底こくさいかいぎをかいさいするにあたり、かんけいかくほうめんからのきょうりょくをえた。",
            "arti": "Dalam rangka menyelenggarakan konferensi internasional di Jepang, kami mendapatkan kerja sama dari berbagai pihak terkait.",
            "kunci": ["にほん", "で", "こくさいかいぎ", "を", "かいさいする", "にあたり", "、", "かんけいかくほうめん", "から の", "きょうりょくをえた", "。"],
            "soal": ["こくさいかいぎ", "にほん", "きょうりょくをえた", "あたり", "かいさいする", "で", "からの", "に", "かんけいかくほうめん", "を", "、", "、"]
        },
        # --- POLA 3 ---
        {
            "id": 9,
            "pola": "Pola 3: ～たとたん（に）",
            "kanji": "山の頂上でワインを一口飲んだとたんに、めまいがした。",
            "hiragana": "やまのちょうじょうでわいんをひとくちのんだとたんに、めまいがした。",
            "arti": "Sesaat setelah meminum seteguk anggur di puncak gunung, saya merasa pusing.",
            "kunci": ["やま", "の", "ちょうじょう", "で", "わいん", "を", "ひとくち", "のんだ", "たとたんに", "、", "めまい", "が", "した", "。"],
            "soal": ["の", "やま", "めまい", "のんだ", "ちょうじょう", "ひとくち", "わいん", "で", "たとたんに", "が", "を", "した", "、"]
        },
        {
            "id": 10,
            "pola": "Pola 3: ～たとたん（に）",
            "kanji": "夫は結婚前は優しかったが、結婚したとたんに、態度が変わった。",
            "hiragana": "おっとはけっこんまえはやさしかったが、けっこんしたとたんに、たいどがかわった。",
            "arti": "Suami saya baik sebelum menikah, tetapi begitu kami menikah, sikapnya langsung berubah.",
            "kunci": ["おっと", "は", "けっこん", "まえ", "は", "やさしかった", "が", "、", "けっこん", "した", "たとたん", "に", "、", "たいど", "が", "かわった", "。"],
            "soal": ["おっと", "が", "かわった", "たいど", "やさしかった", "たとたん", "けっこん", "は", "が", "、", "、", "に", "けっこん", "した", "まえ", "は"]
        },
        {
            "id": 11,
            "pola": "Pola 3: ～たとたん（に）",
            "kanji": "国の母に電話をかけた。母の声を聞いたとたん、涙があふれてきた。",
            "hiragana": "くにのははにでんわをかけた。ははのこえをきいたとたん、なみだがあふれてきた。",
            "arti": "Saya menelepon ibu di kampung halaman. Sesaat setelah mendengar suara ibu, air mata saya langsung menetes.",
            "kunci": ["くに", "の", "はは", "に", "でんわ", "を", "かけた", "。", "はは", "の", "こえ", "を", "きいた", "たとたん", "、", "なみだ", "が", "あふれてきた", "。"],
            "soal": ["でんわ", "はは", "を", "かけた", "たとたん", "の", "あふれてきた", "なみだ", "に", "はは", "くに", "こえ", "きいた", "の", "が", "、", "を", "、"]
        },
        {
            "id": 12,
            "pola": "Pola 3: ～たとたん（に）",
            "kanji": "僕が「さよなら」と言ったとたん、彼女は走っていってしまった。",
            "hiragana": "ぼくが「さよなら」といったとたん、かのじょははしっていってしまった。",
            "arti": "Begitu aku mengatakan \"selamat tinggal\", dia langsung berlari pergi.",
            "kunci": ["ぼく", "が", "「 さよなら 」", "と", "いった", "たとたん", "、", "かのじょ", "は", "はしって", "いってしまった", "。"],
            "soal": ["はしって", "いった", "「 さよなら 」", "かのじょ", "たとたん", "ぼく", "は", "と", "が", "いってしまった", "、", "は"]
        },
        # --- POLA 4 ---
        {
            "id": 13,
            "pola": "Pola 4: ～（か）と思うと・～（か）と思ったら",
            "kanji": "林さんは部屋に入ってきたかと思うと、いきなり窓を全部開けた。",
            "hiragana": "はやしさんはへやにはいってきたかとおもうと、いきなりまどをぜんぶあけた。",
            "arti": "Baru saja Hayashi-san masuk ke kamar, dia tiba-tiba membuka semua jendela.",
            "kunci": ["はやしさん", "は", "へや", "に", "はいってきた", "か", "とおもうと", "、", "いきなり", "まど", "を", "ぜんぶ", "あけた", "。"],
            "soal": ["はいってきた", "あけた", "まど", "はやしさん", "とおもうと", "へや", "いきなり", "は", "を", "に", "ぜんぶ", "、", "、"]
        },
        {
            "id": 14,
            "pola": "Pola 4: ～（か）と思うと・～（か）と思ったら",
            "kanji": "赤ちゃんは今泣いたかと思うと、もう笑っている。",
            "hiragana": "あかちゃんはいまないたかとおもうと、もうわらっている。",
            "arti": "Bayi itu baru saja menangis, eh sekarang sudah tertawa lagi.",
            "kunci": ["あかちゃん", "は", "いま", "ないた", "か", "とおもったら", "、", "もう", "わらっている", "。"],
            "soal": ["わらっている", "いま", "とおもったら", "もう", "あかちゃん", "ないた", "は", "、", "は"]
        },
        {
            "id": 15,
            "pola": "Pola 4: ～（か）と思うと・～（か）と思ったら",
            "kanji": "やっと部屋が片付いたかと思ったら、子供たちがすぐまた散らかした。",
            "hiragana": "やっとへやがかたづいたかとおもったら、こどもたちがすぐまたちらかした。",
            "arti": "Baru saja kamar selesai dirapikan, anak-anak langsung mengacak-acaknya lagi.",
            "kunci": ["やっと", "へや", "が", "かたづいた", "か", "とおもったら", "、", "こどもたち", "が", "すぐ", "また", "ちらかした", "。"],
            "soal": ["ちらかした", "へや", "やっと", "が", "こどもたち", "かたづいた", "とおもったら", "すぐ", "が", "また", "か", "、", "、"]
        },
        {
            "id": 16,
            "pola": "Pola 4: ～（か）と思うと・～（か）と思ったら",
            "kanji": "このごろは気温の差が大きい。昨日は暑くなったかと思ったら、今日は涼しい。",
            "hiragana": "このごろはきおんのさがおおきい。きのうはあつくのなったかとおもったら、きょうはすずしい。",
            "arti": "Akhir-akhir ini perbedaan suhunya besar. Kemarin baru saja terasa panas, hari ini sudah sejuk.",
            "kunci": ["このごろ", "は", "きおん", "の", "さ", "が", "おおきい", "。", "きのう", "は", "あつくなった", "か", "とおもったら", "、", "きょう", "は", "すずしい", "。"],
            "soal": ["きょう", "このごろ", "さ", "おおきい", "すずしい", "きおん", "あつくなった", "きのう", "が", "は", "は", "とおもったら", "か", "、", "。", "は"]
        },
        # --- POLA 5 ---
        {
            "id": 17,
            "pola": "Pola 5: ～か～ないかのうちに",
            "kanji": "一郎はベッドに横になるかならないかのうちに、ぐっすり眠ってしまった。",
            "hiragana": "いちろうはべっどによこになるかならないかのうちに、ぐっすりねむってしまった。",
            "arti": "Sesaat setelah Ichiro berbaring di tempat tidur, dia langsung tertidur lelap.",
            "kunci": ["いちろう", "は", "べっど", "に", "よこになる", "か", "ないかのうちに", "、", "ぐっすり", "ねむってしまった", "。"],
            "soal": ["よこになる", "ねむってしまった", "いちろう", "べっど", "ないかのうちに", "は", "か", "ぐっすり", "に", "、"]
        },
        {
            "id": 18,
            "pola": "Pola 5: ～か～ないかのうちに",
            "kanji": "わたしは夜が明けたか明けぬかのうちに家を出て、空港へ向かった。",
            "hiragana": "わたしはよがあけたかあけぬかのうちにいえをでて、くうこうへむかった。",
            "arti": "Begitu fajar menyingsing, saya langsung keluar rumah dan menuju ke bandara.",
            "kunci": ["わたし", "は", "よる", "が", "あけた", "か", "あけない", "ないかのうちに", "、", "いえ", "を", "でて", "、", "くうこう", "へ", "むかった", "。"],
            "soal": ["むかった", "くうこう", "よる", "あけた", "わたし", "いえ", "でて", "ないかのうちに", "へ", "は", "か", "を", "あけない", "、", "が", "、"]
        },
        {
            "id": 19,
            "pola": "Pola 5: ～か～ないかのうちに",
            "kanji": "あの作家は今売れっ子だ。話題作を発表したかしないかのうちに、もう次の作品に取りかかっているそうだ。",
            "hiragana": "あのさっかはいまうれっこだ。わだいさくをはっぴょうしたかしないかのうちに、もうつぎのさくひんにとりかかっているそうだ。",
            "arti": "Penulis itu sedang populer saat ini. Konon begitu menerbitkan karya yang hangat diperbincangkan, beliau langsung mengerjakan karya berikutnya.",
            "kunci": ["あの", "さっか", "は", "いま", "うれっこ", "だ", "。", "わだいさく", "を", "はっぴょうした", "か", "し", "ないかのうちに", "、", "もう", "つぎ", "の", "さくひん", "に", "とりかかっている", "そうだ", "。"],
            "soal": ["あの", "いま", "とりかかっている", "わだいさく", "うれっこ", "さくひん", "だ", "はっぴょうした", "そうだ", "さっか", "つぎ", "に", "か", "もう", "は", "ないかのうちに", "し", "の", "を", "、", "。"]
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

# --- STYLING CSS ---
st.markdown("""
<style>
    /* Styling tombol agar lebih rapi dan empuk saat diklik */
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 4px 8px !important;
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

    # 2. BANK KATA PILIHAN (Dibuat Ke Samping Berjajar Rapi)
    st.write("### Pilihan Kata:")
    
    # MEMBAGI KOLOM KE SAMPING (3 Kolom Per Baris secara dinamis agar muat di HP & Laptop)
    KOLOM_PER_BARIS = 3
    for i in range(0, len(st.session_state.bank_kata), KOLOM_PER_BARIS):
        cols = st.columns(KOLOM_PER_BARIS)
        for j in range(KOLOM_PER_BARIS):
            idx_item = i + j
            if idx_item < len(st.session_state.bank_kata):
                item = st.session_state.bank_kata[idx_item]
                with cols[j]:
                    if item["dipakai"]:
                        st.button("✔️", key=f"disabled_{item['id']}", disabled=True, use_container_width=True)
                    else:
                        if st.button(item["teks"], key=f"pilih_{item['id']}", use_container_width=True):
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

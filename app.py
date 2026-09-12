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
            "kunci": ["```python
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
            "kanji": "東京の交通機関は複雑になるばかりで、わたしはよく

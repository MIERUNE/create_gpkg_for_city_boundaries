import geopandas as gpd

town_gdf = gpd.read_file("../data/boundary.gpkg", layer="town")
necessary_columns = [
    "AREA_CODE",
    "PREF_NAME",
    "CITY_NAME",
    "GST_NAME",
    "CSS_NAME",
    "AREA",
    "X_CODE",
    "Y_CODE",
    "geometry",
]
town_gdf = town_gdf[necessary_columns]

# 1系
town_gdf["system_number"] = None

one_city_list = [
    "奄美市",
    "名瀬市",
    "十島村",
    "笠沙町",
    "里村",
    "上甑村",
    "下甑村",
    "鹿島村",
    "大和村",
    "宇検村",
    "瀬戸内町",
    "住用村",
    "龍郷町",
    "笠利町",
    "喜界町",
    "徳之島町",
    "天城町",
    "伊仙町",
    "和泊町",
    "知名町",
    "与論町",
    "三島村",
]
town_gdf["system_number"].mask(
    (town_gdf["CITY_NAME"].isin(one_city_list)) & (town_gdf["PREF_NAME"] == "鹿児島県"),
    1,
    inplace=True,
)
town_gdf["system_number"].mask(town_gdf["PREF_NAME"] == "長崎県", 1, inplace=True)

# 2系
two_pref_list = [
    "福岡県",
    "佐賀県",
    "熊本県",
    "大分県",
    "宮崎県",
]
town_gdf["system_number"].mask(
    town_gdf["PREF_NAME"].isin(two_pref_list), 2, inplace=True
)
town_gdf["system_number"].mask(
    (~town_gdf["CITY_NAME"].isin(one_city_list)) & (town_gdf["PREF_NAME"] == "鹿児島県"),
    2,
    inplace=True,
)

# 3系
three_pref_list = [
    "山口県",
    "島根県",
    "広島県",
]
town_gdf["system_number"].mask(
    town_gdf["PREF_NAME"].isin(three_pref_list), 3, inplace=True
)

# 4系
four_pref_list = ["香川県", "愛媛県", "徳島県", "高知県"]
town_gdf["system_number"].mask(
    town_gdf["PREF_NAME"].isin(four_pref_list), 4, inplace=True
)

# 5系
five_pref_list = ["兵庫県", "鳥取県", "岡山県"]
town_gdf["system_number"].mask(
    (town_gdf["PREF_NAME"].isin(five_pref_list)), 5, inplace=True
)

# 6系
six_pref_list = ["京都府", "大阪府", "福井県", "滋賀県", "三重県", "奈良県", "和歌山県"]
town_gdf["system_number"].mask(
    town_gdf["PREF_NAME"].isin(six_pref_list), 6, inplace=True
)

# 7系
seven_pref_list = ["石川県", "富山県", "岐阜県", "愛知県"]
town_gdf["system_number"].mask(
    town_gdf["PREF_NAME"].isin(seven_pref_list), 7, inplace=True
)

# 8系
eight_pref_list = ["新潟県", "長野県", "山梨県", "静岡県"]
town_gdf["system_number"].mask(
    town_gdf["PREF_NAME"].isin(eight_pref_list), 8, inplace=True
)

# 9系
nine_pref_list = ["福島県", "栃木県", "茨城県", "埼玉県", "千葉県", "群馬県", "神奈川県"]
nine_city_list = [
    "千代田区",
    "中央区",
    "港区",
    "新宿区",
    "文京区",
    "台東区",
    "墨田区",
    "江東区",
    "品川区",
    "目黒区",
    "大田区",
    "世田谷区",
    "渋谷区",
    "中野区",
    "杉並区",
    "豊島区",
    "北区",
    "荒川区",
    "板橋区",
    "練馬区",
    "足立区",
    "葛飾区",
    "江戸川区",
    "八王子市",
    "立川市",
    "武蔵野市",
    "三鷹市",
    "青梅市",
    "府中市",
    "昭島市",
    "調布市",
    "町田市",
    "小金井市",
    "小平市",
    "日野市",
    "東村山市",
    "国分寺市",
    "国立市",
    "福生市",
    "狛江市",
    "東大和市",
    "清瀬市",
    "東久留米市",
    "武蔵村山市",
    "多摩市",
    "稲城市",
    "羽村市",
    "あきる野市",
    "西東京市",
    "瑞穂町",
    "日の出町",
    "檜原村",
    "奥多摩町",
    "大島町",
    "利島村",
    "新島村",
    "神津島村",
    "三宅村",
    "御蔵島村",
    "八丈町",
    "青ヶ島村",
]
town_gdf["system_number"].mask(
    town_gdf["PREF_NAME"].isin(nine_pref_list), 9, inplace=True
)
town_gdf["system_number"].mask(
    (town_gdf["CITY_NAME"].isin(nine_city_list)) & (town_gdf["PREF_NAME"] == "東京都"),
    9,
    inplace=True,
)

# 10系
ten_pref_list = ["青森県", "秋田県", "山形県", "岩手県", "宮城県"]
town_gdf["system_number"].mask(
    town_gdf["PREF_NAME"].isin(ten_pref_list), 10, inplace=True
)

# 11系
eleven_city_list = [
    "小樽市",
    "島牧村",
    "寿都町",
    "黒松内町",
    "蘭越町",
    "ニセコ町",
    "真狩村",
    "留寿都村",
    "喜茂別町",
    "京極町",
    "倶知安町",
    "共和町",
    "岩内町",
    "泊村",
    "神恵内村",
    "積丹町",
    "古平町",
    "仁木町",
    "余市町",
    "赤井川村",
    "函館市",
    "北斗市",
    "松前町",
    "福島町",
    "知内町",
    "木古内町",
    "七飯町",
    "鹿部町",
    "森町",
    "八雲町",
    "長万部町",
    "江差町",
    "上ノ国町",
    "厚沢部町",
    "乙部町",
    "奥尻町",
    "今金町",
    "せたな町",
    "伊達市",
    "豊浦町",
    "壮瞥町",
    "洞爺湖町",
]
town_gdf["system_number"].mask(
    (town_gdf["CITY_NAME"].isin(eleven_city_list)) & (town_gdf["PREF_NAME"] == "北海道"),
    11,
    inplace=True,
)

# 13系
thirteen_city_list = [
    "音更町",
    "士幌町",
    "上士幌町",
    "鹿追町",
    "新得町",
    "清水町",
    "芽室町",
    "中札内村",
    "更別村",
    "大樹町",
    "広尾町",
    "幕別町",
    "池田町",
    "豊頃町",
    "本別町",
    "足寄町",
    "陸別町",
    "浦幌町",
    "釧路町",
    "厚岸町",
    "浜中町",
    "標茶町",
    "弟子屈町",
    "鶴居村",
    "白糠町",
    "別海町",
    "中標津町",
    "標津町",
    "羅臼町",
    "北見市",
    "帯広市",
    "釧路市",
    "網走市",
    "根室市",
    "美幌町",
    "津別町",
    "斜里町",
    "清里町",
    "小清水町",
    "訓子府町",
    "置戸町",
    "佐呂間町",
    "大空町",
]
town_gdf["system_number"].mask(
    (town_gdf["CITY_NAME"].isin(thirteen_city_list) & (town_gdf["PREF_NAME"] == "北海道")),
    13,
    inplace=True,
)

# 12系
not_twelve_city_list = eleven_city_list + thirteen_city_list
town_gdf["system_number"].mask(
    (town_gdf["PREF_NAME"] == "北海道")
    & (~town_gdf["CITY_NAME"].isin(not_twelve_city_list)),
    12,
    inplace=True,
)

# 14系：聟島列島、父島列島、母島列島、硫黄島
town_gdf["system_number"].mask(
    (town_gdf["CITY_NAME"] == "小笠原村") & (town_gdf["PREF_NAME"] == "東京都"),
    14,
    inplace=True,
)

# 15系
fifteen_city_list = [
    "那覇市",
    "石川市",
    "具志川市",
    "宜野湾市",
    "浦添市",
    "名護市",
    "糸満市",
    "沖繩市",
    "国頭村",
    "大宜味村",
    "東村",
    "今帰仁村",
    "本部町",
    "恩納村",
    "宜野座村",
    "金武町",
    "伊江村",
    "与那城町",
    "勝連町",
    "読谷村",
    "嘉手納町",
    "北谷町",
    "北中城村",
    "中城村",
    "西原町",
    "豊見城村",
    "東風平町",
    "具志頭村",
    "玉城村",
    "知念村",
    "佐敷町",
    "与那原町",
    "大里村",
    "南風原町",
    "仲里村",
    "具志川村",
    "渡嘉敷村",
    "座間味村",
    "粟国村",
    "渡名喜村",
    "伊平屋村",
    "伊是名村",
]
town_gdf["system_number"].mask(
    (town_gdf["CITY_NAME"].isin(fifteen_city_list)) & (town_gdf["PREF_NAME"] == "沖縄県"),
    15,
    inplace=True,
)
town_gdf["system_number"].mask(
    (town_gdf["X_CODE"] > 126)
    & (town_gdf["X_CODE"] < 130)
    & (town_gdf["PREF_NAME"] == "沖縄県"),
    15,
    inplace=True,
)

# 16系
sixteen_city_list = ["平良市", "石垣市", "城辺町", "下地町", "上野村", "伊良部町", "多良間村", "竹富町", "与那国町"]
town_gdf["system_number"].mask(
    (town_gdf["CITY_NAME"].isin(sixteen_city_list)) & (town_gdf["PREF_NAME"] == "沖縄県"),
    16,
    inplace=True,
)
town_gdf["system_number"].mask(
    (town_gdf["X_CODE"] < 126) & (town_gdf["PREF_NAME"] == "沖縄県"), 16, inplace=True
)

# 17系
seventeen_city_list = ["南大東村", "北大東村"]
town_gdf["system_number"].mask(
    (town_gdf["CITY_NAME"].isin(seventeen_city_list))
    & (town_gdf["PREF_NAME"] == "沖縄県"),
    17,
    inplace=True,
)
town_gdf["system_number"].mask(
    (town_gdf["X_CODE"] > 130) & (town_gdf["PREF_NAME"] == "沖縄県"), 17, inplace=True
)

# 18,19系（沖ノ鳥島,南鳥島）は小笠原村のポリゴンに統合されてしまっていたため、現段階で算出できない
# 18系：沖ノ鳥島
town_gdf["system_number"].mask(
    (town_gdf["Y_CODE"] < 28)
    & (town_gdf["X_CODE"] < 140.5)
    & (town_gdf["PREF_NAME"] == "東京都"),
    18,
    inplace=True,
)

# 19系：南鳥島
town_gdf["system_number"].mask(
    (town_gdf["Y_CODE"].astype("float") < 28)
    & (town_gdf["X_CODE"].astype("float") > 143)
    & (town_gdf["PREF_NAME"] == "東京都"),
    19,
    inplace=True,
)

# ファイル書き出し
town_gdf.to_file(
    "../data/merge_boundary.gpkg", layer="add_system_number", driver="GPKG"
)

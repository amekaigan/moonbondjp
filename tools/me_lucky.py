"""一般的なラッキー項目（宿ごと）。きもの・帯の色とは別の、だれにでも分かる内容。
並びは public/full/index.html の M と同じ（昴・畢・觜…胃）。
各行: (色コード, 色en, 色ja, 数字, 方角の角度, 方角en, 方角ja,
        小物en, 小物ja, 小物の絵文字, 食べものen, 食べものja, 絵文字, 場所en, 場所ja, 絵文字)
"""
LUCKY = [
 ("#B7A6D9", "Lavender", "ラベンダー", 3, 90, "East", "東", "Silk scarf", "シルクのスカーフ", "🧣", "Jasmine tea", "ジャスミン茶", "🍵", "A quiet library", "静かな図書館", "📚"),
 ("#3E7B4F", "Forest green", "深い緑", 4, 0, "North", "北", "Wooden pen", "木のペン", "🖊️", "Roasted chestnuts", "焼き栗", "🌰", "A hillside path", "山道の散歩道", "⛰️"),
 ("#6E8FB8", "Dusty blue", "くすんだ青", 7, 270, "West", "西", "Notebook", "ノート", "📓", "Honey toast", "はちみつトースト", "🍯", "A cozy cafe", "落ち着いたカフェ", "☕"),
 ("#E8742A", "Tangerine", "みかん色", 5, 45, "Northeast", "北東", "Sneakers", "スニーカー", "👟", "Spicy noodles", "ピリ辛の麺", "🍜", "A new neighborhood", "まだ行ったことのない街", "🗺️"),
 ("#4AA3C7", "Spring water", "湧き水の青", 1, 0, "North", "北", "Water bottle", "水筒", "🥤", "Cold soba", "冷たいお蕎麦", "🥢", "By a river", "川のそば", "🌊"),
 ("#7B5EA7", "Plum", "すもも色", 9, 315, "Northwest", "北西", "Small mirror", "小さな鏡", "🪞", "Dark chocolate", "ビターチョコ", "🍫", "A bookshop at dusk", "夕暮れの本屋", "📖"),
 ("#8FBF6A", "Willow green", "やなぎ色", 6, 135, "Southeast", "南東", "Handkerchief", "ハンカチ", "🧵", "Matcha sweets", "抹茶のお菓子", "🍡", "A tree-lined street", "並木道", "🌳"),
 ("#F2C14E", "Sunny yellow", "ひまわり色", 2, 180, "South", "南", "Sunglasses", "サングラス", "🕶️", "Lemon tart", "レモンのタルト", "🍋", "A sunny window seat", "日なたの窓際", "🪟"),
 ("#D9544D", "Cherry red", "さくらんぼ色", 8, 180, "South", "南", "Bracelet", "ブレスレット", "📿", "Strawberries", "いちご", "🍓", "A lively market", "にぎやかな市場", "🛍️"),
 ("#58B3C4", "Sky teal", "空色", 3, 90, "East", "東", "Backpack", "リュック", "🎒", "Fresh fruit", "季節のくだもの", "🍊", "An open hilltop", "見晴らしのよい丘", "🌄"),
 ("#2F5D8A", "Navy", "ネイビー", 7, 270, "West", "西", "Leather wallet", "革のお財布", "👛", "Grilled fish", "焼き魚", "🐟", "A tidy workspace", "整えた仕事机", "🖥️"),
 ("#C9A227", "Antique gold", "アンティークゴールド", 1, 45, "Northeast", "北東", "Ring", "指輪", "💍", "Rice with sesame", "ごま塩ごはん", "🍚", "A shrine garden", "神社の庭", "⛩️"),
 ("#B24A6B", "Raspberry", "ラズベリー", 6, 225, "Southwest", "南西", "Lip balm", "リップクリーム", "💄", "Berry yogurt", "ベリーのヨーグルト", "🫐", "A flower shop", "花屋さん", "💐"),
 ("#6C7A89", "Slate gray", "スレートグレー", 4, 0, "North", "北", "Earphones", "イヤホン", "🎧", "Miso soup", "お味噌汁", "🍲", "A calm night walk", "夜の静かな散歩", "🌙"),
 ("#E58FA3", "Blush pink", "さくら色", 2, 135, "Southeast", "南東", "Hair accessory", "ヘアアクセサリー", "🎀", "Strawberry mochi", "いちご大福", "🍡", "A cherry tree", "桜の木の下", "🌸"),
 ("#D6453D", "Ruby", "ルビーレッド", 9, 180, "South", "南", "Red pen", "赤いペン", "✒️", "Tomato dishes", "トマト料理", "🍅", "A warm kitchen", "あたたかいキッチン", "🍳"),
 ("#2E8B8B", "Deep teal", "青緑", 5, 315, "Northwest", "北西", "Tote bag", "トートバッグ", "👜", "Seaweed rice balls", "海苔のおにぎり", "🍙", "The seaside", "海辺", "🏖️"),
 ("#A67C52", "Warm brown", "あたたかい茶色", 8, 45, "Northeast", "北東", "Leather bookmark", "革のしおり", "🔖", "Baked sweet potato", "焼きいも", "🍠", "A wooden cabin", "木の香りの部屋", "🏡"),
 ("#35507F", "Midnight blue", "夜空の青", 7, 0, "North", "北", "Compact umbrella", "折りたたみ傘", "☂️", "Hot ginger tea", "しょうが湯", "🫚", "Under the stars", "星空の下", "✨"),
 ("#F08BA8", "Peach", "ももいろ", 2, 225, "Southwest", "南西", "Hand cream", "ハンドクリーム", "🧴", "Peaches", "もも", "🍑", "A friend's home", "友だちの家", "🏠"),
 ("#9FB8D6", "Pale sky", "うすい空色", 1, 270, "West", "西", "Fountain pen", "万年筆", "🖋️", "Plain rice porridge", "おかゆ", "🥣", "A quiet museum", "静かな美術館", "🖼️"),
 ("#4F6D7A", "Steel blue", "鉄色", 6, 90, "East", "東", "Calendar", "手帳", "📅", "Barley tea", "麦茶", "🫖", "A park at sunrise", "朝の公園", "🌅"),
 ("#E3B448", "Honey", "はちみつ色", 4, 135, "Southeast", "南東", "Candle", "キャンドル", "🕯️", "Pumpkin soup", "かぼちゃのスープ", "🎃", "A bright living room", "明るいリビング", "🛋️"),
 ("#7A9E7E", "Sage", "セージグリーン", 3, 0, "North", "北", "Plant in a pot", "小さな鉢植え", "🪴", "Green salad", "グリーンサラダ", "🥗", "A greenhouse", "温室", "🌿"),
 ("#C8553D", "Terracotta", "テラコッタ", 9, 225, "Southwest", "南西", "Sketchbook", "スケッチブック", "🎨", "Grilled vegetables", "焼き野菜", "🥕", "A pottery studio", "陶芸の工房", "🏺"),
 ("#5B7DB1", "Cornflower", "矢車菊の青", 5, 90, "East", "東", "Letter paper", "便せん", "✉️", "Fresh bread", "焼きたてのパン", "🥖", "A neighborhood bakery", "町のパン屋さん", "🥐"),
 ("#8E6BBF", "Wisteria", "ふじ色", 8, 315, "Northwest", "北西", "Business-card case", "名刺入れ", "💼", "Grape juice", "ぶどうジュース", "🍇", "A rooftop view", "高い場所からの景色", "🏙️"),
]
assert len(LUCKY) == 27

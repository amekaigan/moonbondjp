# 「自分用の鑑定」の中身（宿ごと）。英語と日本語の組で書く。
# 作り方: tools/build_me.py を実行すると public/me/index.html と public/me-ready.json ができる。
# ここに書いた宿だけが、サイトで「購入できる」状態になる（キーはキャラクターの slug）。

ME = {}

ME['star'] = {
    # 第1章：本当のあなた
    'core': [
        ("You are the kind of person who decides where you are going long before anyone notices you have started. While others talk about their dreams, you are already doing the unglamorous part of it: the early mornings, the practice, the quiet hours nobody sees. You do not need an audience, and you do not trust success that arrives too easily.",
         "あなたは、周りが気づくずっと前に、行き先を決めて歩き出している人です。ほかの人が夢を語っている間に、早起きや練習のような地味な部分をもう始めています。見ている人がいなくても平気で、あっさり手に入った成功のほうが、むしろ信用できません。"),
        ("Your path tends to be slower at the start and stronger at the end. Praise may come late, and that can sting, but what you build with your own hands does not collapse when the wind changes. Behind the calm face is real pride, and a part of you keeps score of every promise you have made to yourself.",
         "歩き出しはゆっくりでも、後半に強くなる道のりです。ほめ言葉が遅れて届くと寂しい日もあるでしょう。それでも、自分の手で積み上げたものは、風向きが変わっても崩れません。静かな顔の奥には確かな誇りがあり、自分との約束を一つずつ数えている面もあります。"),
    ],
    'strengths': [
        ("Staying power", "続ける力",
         "You keep going after the excitement has worn off. That alone puts you ahead of most people.",
         "気持ちが盛り上がっていない日も続けられます。それだけで、多くの人より一歩先に出られます。"),
        ("Self-direction", "自分で決める力",
         "You do not wait to be told. Once you pick a goal, you can plan the road and walk it alone.",
         "指示を待たず、目標を決めたら道筋まで自分で組み立てて進めます。"),
        ("Trustworthiness", "信頼される力",
         "People learn that what you say you will do, you do. Over the years this becomes your biggest asset.",
         "「やる」と言ったことは、やる。そう知られていくことが、年月とともに一番の財産になります。"),
    ],
    'blind': [
        ("Hard to lean on others", "人に頼るのが苦手",
         "You would rather struggle alone than ask. People around you often do not know you need help until you are worn out.",
         "頼むくらいなら一人で抱えたい人です。周りは、あなたが疲れ切るまで助けが必要だと気づけません。"),
        ("Racing the clock", "人と比べて焦る",
         "When someone your age moves faster, you quietly feel behind. Your path simply runs on a different clock.",
         "同じ年ごろの人が先に進むと、静かに焦りが出ます。でも、あなたの道は時計の進み方がもともと違います。"),
        ("Showing only the finished face", "完成した顔しか見せない",
         "Pride makes you show a polished self. Closeness needs the unfinished one too.",
         "誇りが高いぶん、整った顔ばかり見せます。親しくなるには、未完成の顔も必要です。"),
    ],
    # 第2章：恋愛
    'love': {
        'attract': (
            "You are drawn to people who work at something and do not make a show of it. Seriousness, a clear goal and quiet kindness move you far more than charm does.",
            "何かに黙々と取り組んでいる人に惹かれます。派手な魅力よりも、まじめさ、はっきりした目標、さりげない優しさに心が動きます。"),
        'pattern': (
            "You open up slowly, and when you do it is all the way. The trap is that you show the strong version of yourself for months, so your partner falls for someone who never has a bad day. Then you cannot tell them about the bad day.",
            "心を開くまでは時間がかかりますが、開いたら深く開きます。落とし穴は、何か月も「強い自分」だけを見せてしまうこと。相手は弱音を吐かない人に恋をして、あなたも調子の悪い日を打ち明けにくくなります。"),
        'try': (
            "Tell your partner one unfinished thing this month: a worry, or a goal you are not sure of. It will not lower their respect for you. It lets them reach you.",
            "今月、未完成なことを一つ、相手に話してみてください。迷っている目標でも、小さな不安でも構いません。尊敬は下がらず、相手があなたに届くようになります。"),
    },
    # 第3章：仕事とお金
    'work': {
        'fit': [
            ("Craft and expertise: engineering, research, design, the trades. Anywhere mastery counts.",
             "腕前が育つ仕事：技術職、研究、デザイン、職人系。実力がものを言う世界。"),
            ("Work with your own territory: freelancing, running a shop, a role with real discretion.",
             "自分の持ち場がある働き方：独立、自営、裁量の大きい役割。"),
            ("Long-horizon roles: finance, planning, project management, where patience pays.",
             "時間をかけて成果が出る仕事：経理・財務、企画、プロジェクト管理。"),
        ],
        'style': (
            "You do your best work when the goal is clear and nobody hovers. Being micromanaged drains you faster than hard work does.",
            "目標がはっきりしていて、横から口を出されない環境で、いちばん力が出ます。細かく管理されると、仕事の量よりも早く消耗します。"),
        'money': (
            "Money comes from effort and arrives in steps, not in jackpots. You are a natural saver and do best with a plan and a number to aim at. Be careful of the all-or-nothing project you fund alone.",
            "お金は努力に応じて、階段のように増えていきます。一発逆転型ではありません。貯めるのが得意で、目標の金額があると伸びます。気をつけたいのは、一人で全額を出す「一か八か」の挑戦です。"),
        'caution': (
            "Do not turn down good offers just because you feel you have not earned them yet.",
            "「まだ自分にはふさわしくない」と、良い話を断りすぎないでください。"),
    },
    # 第4章：疲れと回復
    'drain': (
        "Being rushed, being compared with others, and meetings that have no purpose.",
        "急かされること、人と比べられること、目的のない付き合い。"),
    'recharge': (
        "An hour of focused work on your own project, a long walk, a quiet evening with one person you trust.",
        "自分の課題に集中する一時間、長めの散歩、信頼できる一人との静かな夜。"),
    # 第6章：今週のひとこと・結び
    'week': (
        "This week, pick one thing you have been building alone and show it to one person you trust.",
        "今週、一人で積み上げてきたことを一つ選んで、信頼できる人に見せてみてください。"),
    'close': (
        "Your light is the kind that gets brighter the longer you carry it. There is no need to hurry it. Just let the right people see it.",
        "あなたの光は、長く灯し続けるほど明るくなる種類のものです。急ぐ必要はありません。ふさわしい人に見える場所へ、そっと出してあげてください。"),
}


# 残りの宿は me_content_a〜e.py に分けて書いてある（あるものだけ読み込む）
import importlib
for _n in ('me_content_a', 'me_content_b', 'me_content_c', 'me_content_d', 'me_content_e'):
    try:
        ME.update(importlib.import_module(_n).ME_X)
    except ModuleNotFoundError:
        pass

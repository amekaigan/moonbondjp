"""カップル完全版の追加章の文章。縁の6つのまとまり（k）ごと。 各項目は (英語, 日本語)。
k: 命(Mirror) / 業胎(Karmic Thread) / 栄親(Prosperity & Kinship) / 友衰(Friendship & Waning) / 安壊(Comfort & Disruption) / 危成(Risk & Achievement)
MEET[k]  = {'story': (en, ja), 'gifts': [(en, ja) x3]}      … 第9章「二人が出会った意味」
LIVE[k]  = [(見出し(en,ja), 本文(en,ja)) x5]                  … 第10章「一緒に暮らすときのコツ」
"""

LIVE_HEADS = [
    ("Mornings and evenings", "朝と夜の過ごし方"),
    ("Money", "お金のこと"),
    ("Days off", "休日の過ごし方"),
    ("After a quarrel", "けんかのあと"),
    ("Anniversaries and turning points", "記念日と節目"),
]

MEET = {
    "命": {
        "story": (
            "You share the same mansion, so you meet as a mirror. Much about the other person feels familiar before it is explained, and that is why you relax so fast. The tradition reads this meeting as a chance to see your own strengths and your own habits from the outside.",
            "二人は同じ宿で、うつし鏡のように出会いました。説明しなくても相手のことが分かる気がして、すぐに安心できるのはそのためです。宿曜では、この出会いを「自分の強みもくせも、外から見せてもらえる機会」と読みます。",
        ),
        "gifts": [
            ("You are understood without having to explain.", "説明しなくても、分かってもらえる安心。"),
            ("You see your own habits clearly, because they show up in the other person.", "自分のくせが相手を通して見えて、気づきになる。"),
            ("You get a partner who truly shares your pace.", "歩くペースが同じ、気を使わない相手。"),
        ],
    },
    "業胎": {
        "story": (
            "Karmic Thread is the old tie. Many people describe it as meeting someone they somehow already knew, and the pull can feel stronger than the reasons for it. The tradition reads this as a bond with something to finish together, and it tends to deepen the longer you stay.",
            "業胎は「前世からの縁」といわれる関係です。初めて会った気がしない、理由より先に引き寄せられた、という人が多い組み合わせ。宿曜では、二人で一緒にやり遂げることがある縁と読み、長く付き合うほど深まります。",
        ),
        "gifts": [
            ("A feeling of belonging that needs no history.", "付き合いの長さに関係なく、そばにいる安心感。"),
            ("A push to grow that you would not give yourself.", "一人では出せない、成長のきっかけ。"),
            ("A bond that gets stronger when you face things together.", "一緒に向き合うほど、強くなる絆。"),
        ],
    },
    "栄親": {
        "story": (
            "Prosperity and Kinship is counted as the luckiest bond. One of you tends to lift the other, and the other quietly supports in return, so both of you do better together than apart. The tradition reads this meeting as a good omen for the two of you.",
            "栄親は、いちばん幸運な縁とされる組み合わせです。一方が相手を引き上げ、もう一方がそっと支える関係で、二人でいるほうがそれぞれ一人のときより力を出せます。宿曜では、この出会いを二人にとっての吉兆と読みます。",
        ),
        "gifts": [
            ("Each of you does better with the other beside you.", "一緒にいるほうが、お互いに力が出る。"),
            ("Luck that flows both ways: one gives energy, one gives steadiness.", "元気をくれる人と、安定をくれる人。運が行き来する。"),
            ("A relationship that grows more fruitful over time.", "年月とともに、実りが増えていく関係。"),
        ],
    },
    "友衰": {
        "story": (
            "Friendship and Waning is the easy, friendly bond. You enjoy each other's company and talk freely, and one of you tends to spend more energy than the other. The tradition reads this meeting as a place to learn balance: how to enjoy someone fully without wearing yourself down.",
            "友衰は、気が合う友だちのような縁です。一緒にいて楽しく、何でも話せる反面、片方がつい多く気を使い、力を使いがちです。宿曜では、この出会いを「楽しみつつ、疲れ切らない付き合い方」を学ぶ場と読みます。",
        ),
        "gifts": [
            ("A companion who makes ordinary days lighter.", "ふつうの毎日を、軽くしてくれる相手。"),
            ("Conversation that never runs out.", "話題が尽きない会話。"),
            ("A lesson in sharing the effort evenly.", "気づかいを、半分ずつにする練習。"),
        ],
    },
    "安壊": {
        "story": (
            "Comfort and Disruption pairs a calming force with a shaking one. One of you brings peace and the other brings change, and at their best they keep each other from getting stuck. The tradition reads this meeting as a way to learn when to settle and when to move.",
            "安壊は、落ち着かせる力と、揺さぶる力の組み合わせです。一方が安らぎを、もう一方が変化を運び、うまくいけば、お互いが行き詰まらずにすみます。宿曜では、この出会いを「落ち着くときと、動くとき」を学ぶ縁と読みます。",
        ),
        "gifts": [
            ("Calm when you are restless, and a nudge when you are stuck.", "落ち着かないときは安心を、停滞したときは後押しを。"),
            ("A view of life you would not reach alone.", "一人では持てない、ものの見方。"),
            ("A relationship that rarely goes stale.", "マンネリになりにくい関係。"),
        ],
    },
    "危成": {
        "story": (
            "Risk and Achievement is the bond of daring and results. One of you opens up possibilities and the other turns them into something finished, so together you tend to get things done. The tradition reads this meeting as a pairing for big goals, where you learn to take risks with care.",
            "危成は、挑戦と成果の縁です。一方が可能性を広げ、もう一方がそれをかたちにするので、二人でいると物事が実現しやすくなります。宿曜では、この出会いを「大きな目標に向かう組み合わせ」と読み、慎重に挑戦する力が育ちます。",
        ),
        "gifts": [
            ("Courage to try, and the follow-through to finish.", "挑戦する勇気と、やり遂げる力。"),
            ("Shared goals that keep you moving forward.", "同じ目標が、二人を前に進める。"),
            ("A partner who steadies your biggest risks.", "大きな挑戦を、支えてくれる相手。"),
        ],
    },
}

LIVE = {
    "命": [
        (("You move at the same pace, so neither of you needs to hurry the other. Keep a little time apart, so the day does not become one long echo.", "ペースが同じなので、急かす必要がありません。一人の時間も少し作ると、毎日が単調になりにくくなります。")),
        (("You tend to spend and save in the same way, so the same blind spot is shared. Ask a third person to look at big purchases.", "お金の使い方も似ているので、同じ見落としをしがちです。大きな買い物は、第三者にも見てもらうと安心です。")),
        (("You enjoy the same things, so plan one new thing a month. Try a place or an activity neither of you chose before.", "好きなものが似ているので、月に一度、二人とも初めてのことを。行ったことのない場所や、新しい趣味がおすすめです。")),
        (("You hurt each other with the same words you use on yourself. Wait a day before you talk, and start with what you also did wrong.", "自分に向ける言葉と同じ言葉で、相手も傷つけがちです。話すのは一晩おいてから、まず自分の非から話しましょう。")),
        (("Make the day yours with a small ritual, such as the same cafe each year. A repeated, simple tradition suits you better than a big event.", "毎年同じカフェに行くなど、小さな決まりごとを。大きなイベントより、くり返せるシンプルな習慣が似合います。")),
    ],
    "業胎": [
        (("Even when you say little, the other feels it. Say good morning and good night out loud, and do not rely on being understood.", "言葉が少なくても、相手には伝わってしまう関係です。おはようとおやすみは、声に出して言いましょう。")),
        (("Money can bring out old worries. Talk about it early and plainly, and keep a joint rule for large amounts.", "お金は、昔からの不安が出やすい話題です。早めにはっきり話して、大きな金額の決まりを二人で持ちましょう。")),
        (("A quiet place suits you, such as a walk, a long drive or an old town. Time without a schedule brings you closer.", "散歩やドライブ、古い町並みなど、静かな場所が合います。予定を詰めない時間が、二人を近づけます。")),
        (("The feelings run deep and can last. Do not go to sleep without one kind word, even when you are still upset.", "気持ちが深く、長引きやすい二人です。怒っていても、寝る前にやさしい一言だけは伝えましょう。")),
        (("You tend to feel turning points strongly. Mark the ones that matter, such as the day you met, with a letter or a trip.", "節目を強く感じる二人です。出会った日など大切な日は、手紙や小さな旅で残しましょう。")),
    ],
    "栄親": [
        (("The one who lifts can get tired, and the one who is lifted can forget to say thanks. Say thank you every day and take turns making the morning meal.", "引き上げる側は疲れやすく、支えられる側は感謝を忘れがちです。毎日のありがとうと、朝ごはんの当番交代を。")),
        (("Money tends to grow well between you. Make one shared goal, such as a trip or a home, and set a little aside each month.", "お金が増えやすい二人です。旅行や住まいなど共通の目標を一つ決めて、毎月少しずつ貯めましょう。")),
        (("Spend days off meeting people together. Your luck extends to the people around you, so invite friends and family often.", "休日は、二人で人と会う時間を。運が周りにも広がる二人なので、友人や家族を気軽に招きましょう。")),
        (("Quarrels pass quickly, but the one who lifts may swallow hurt. Ask, ‘Did I ask too much of you?’ before it builds up.", "けんかはすぐ収まりますが、引き上げる側は我慢しがちです。「頼りすぎたかな」と、早めに聞いてあげましょう。")),
        (("Celebrate in company. A party with the people who support you, and a thank-you to them, suits this bond.", "人を招いてお祝いを。支えてくれた人たちへの感謝を込めた小さな会が、この縁に合います。")),
    ],
    "友衰": [
        (("You talk easily, so one of you may end up giving more. Split the chores by a simple chart, so that the helpful one does not run dry.", "気軽に話せるぶん、片方が多く動きがちです。家事は簡単な表で分けて、よく動く側が疲れ切らないように。")),
        (("Shared spending is easy to let slide. Divide it clearly, for example by a fixed monthly amount into a joint account.", "お金の貸し借りがあいまいになりがちです。毎月決まった額を共通口座に入れるなど、はっきり分けましょう。")),
        (("You are happiest doing things side by side, such as cooking, games or a hobby. Choose an activity, not just a place.", "並んで何かをする時間が合います。料理、ゲーム、趣味など、場所だけでなく「やること」を決めましょう。")),
        (("You tend to talk it out and move on, which is good. The point to watch is the one who gave in: thank them for it afterwards.", "話して水に流せる二人です。気をつけたいのは、譲ったほうへの「ありがとう」。あとで必ず伝えましょう。")),
        (("Keep it light and fun, such as a shared meal or a small outing. Avoid big expectations that one person has to carry.", "食事や小さなお出かけなど、軽く楽しい祝い方を。片方だけが背負う、大きな期待は避けましょう。")),
    ],
    "安壊": [
        (("One of you likes routine and the other likes change. Keep the morning the same and let the evening vary, so both are satisfied.", "習慣を好む人と、変化を好む人の組み合わせです。朝は同じ流れにして、夜は変化をつけると、どちらも満足します。")),
        (("You see money differently: one saves, one spends on experience. Agree on a fun budget that each can use freely.", "お金の見方が違いがちです。貯めたい人と、体験に使いたい人。それぞれ自由に使える枠を決めておきましょう。")),
        (("Alternate who chooses the day. One day is quiet at home, the next is a new outing. Each of you gets your turn.", "休日の行き先は交代で決めましょう。ある日は家でのんびり、次の日は新しい場所へ。お互いの番があると安心です。")),
        (("A quarrel can come from a difference in pace. Pause, name what each of you needs, and meet in the middle. Do not decide anything big while angry.", "けんかは、ペースの違いから起きがちです。一度止まって、お互いの望みを言葉にしましょう。怒っているときに大きなことは決めないで。")),
        (("A surprise suits you, but keep one steady tradition. Mix a planned dinner with one small unplanned gift.", "サプライズが似合う二人です。ただし、毎年の決まりごとも一つ。計画した食事と、小さな思いがけない贈り物を組み合わせて。")),
    ],
    "危成": [
        (("Mornings can be busy because you both have goals. Put one shared goal on the table each week and review it together on Sunday evening.", "二人とも目標が多く、朝が忙しくなりがちです。週に一つ、共通の目標を決めて、日曜の夜に一緒に振り返りましょう。")),
        (("You tend to put money into dreams and plans. Keep an emergency fund first, so that a risk does not become a worry.", "夢や計画にお金を使いがちです。まず生活の予備費を確保しておくと、挑戦が不安になりません。")),
        (("A challenge suits your days off: a hike, a class, or a project. Choose something with a visible result at the end.", "休日は、ハイキングや習いごと、二人のプロジェクトなど、挑戦が似合います。最後に形が残るものを選びましょう。")),
        (("Quarrels often come from pushing too hard. Stop and ask whether the goal still matters more than the person. The answer usually ends the argument.", "けんかは、頑張りすぎたときに起きがちです。「その目標は、相手より大事か」と一度立ち止まれば、たいてい収まります。")),
        (("Celebrate results. When one of you finishes something, mark it properly with a dinner and a few words about what you learned.", "成果をお祝いしましょう。どちらかがやり遂げたら、食事と「何を学んだか」の一言で、きちんと区切りをつけます。")),
    ],
}

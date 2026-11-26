# 「あなた編」の1宿ぶんを、短く書くための型。
# 英語と日本語を (英語, 日本語) の組で書く。強み・つまずきは (英語の見出し, 日本語の見出し, 英語の説明, 日本語の説明)。


def mk(core, strengths, blind, attract, pattern, try_, fit, style, money, caution, drain, recharge, week, close):
    return {
        'core': list(core),
        'strengths': list(strengths),
        'blind': list(blind),
        'love': {'attract': attract, 'pattern': pattern, 'try': try_},
        'work': {'fit': list(fit), 'style': style, 'money': money, 'caution': caution},
        'drain': drain,
        'recharge': recharge,
        'week': week,
        'close': close,
    }

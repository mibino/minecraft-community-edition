from minecraft import lang

if lang == 'en_US':
    from assets.text.en_US import *
elif lang == 'zh_CN':
    from assets.text.zh_CN import *
else:
    from assets.text.en_US import *
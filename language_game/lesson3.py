#!/usr/bin/python
# -*- coding: utf-8 -*-


class Lesson3RadicalsPinYin(object):

    quiz = {
    "巾": "jin1",
    "心": "xin1",
    "日": "ri4",
    "亻": "ren2",
    "女": "nu3",
    }


class Lesson3RadicalsChars(object):

    quiz = {
    """jin3
1.巾  2.心  3.女  4.亻  5.日
""": "1",
    """ri4
1.巾  2.心  3.女  4.亻  5.日
""": "5",
    """ren2
1.巾  2.心  3.女  4.亻  5.日
""": "4",
    """xin1
1.巾  2.心  3.女  4.亻  5.日
""": "2",
    """nu3
1.巾  2.心  3.女  4.亻  5.日
""": "3",
    }


class Lesson3PinYin(object):

    quiz = {
    '老': 'lao3',
    '师': 'shi1',
    '您': 'nin2',
    '早': 'zao3',
    '你': 'ni3',
    '好': 'hao3',
    '再': 'zai4',
    '见': 'jian4',
    '再 见': 'zai4 jian4',
    }


class Lesson3PinYinPhrases(object):

    quiz = {
    '您 早': 'nin2 zao3',
    '你 好': 'ni3 hao3',
    '再 见': 'zai4 jian4',
    }

class Lesson3DialoguePinYin(object):

    quiz = {
    """
1.1
老 师, 您 早!
    """: "lao3 shi1, nin2 zao3!",
    """
1.2
你 早!
    """: "ni3 zao3!",
    """
2.1
老 师, 您 好!
    """: "lao3 shi1, nin2 hao3!",
    """
2.2
你 好!
    """: "ni3 hao3!",
    """
3.1
老 师, 再 见!
    """: "lao3 shi1, zai4 jian4!",
    """
3.2
再 见!
    """: "zai4 jian4!",
    }


class Lesson3DialogueChars(object):

    quiz = {
    """
-------
1.1
lao3 shi1, nin2 zao3!

1.老 师, 您 好!     2.您 好, 老 师!     3.好 师, 您 好!     4.老 师, 您 早!
""": "4",
    """
-------
1.2
ni3 zao3!

1.您 好!      2.您 好!      3.你 早!       4.师 好!
""": "3",
    """
-------
2.1
lao3 shi1, nin2 hao3!

1.老 师, 您 好!     2.老 师, 您 早!     3.您 好, 老 师!     4.师 老, 您 好!
""": "1",
    """
-------
2.2
ni3 hao3!

1.您 好!      2.你 好!      3.师 好!       4.好 您!
""": "2",
    """
-------
3.1
lao3 shi1, zai4 jian4!

1.老 师, 您 早!     2.老 师, 再 见!     3.师 老, 再 见!     4.老 师, 见 再!
""": "2",
    """
-------
3.2
zai4 jian4!

1.再 见!      2.您 早!      3.见 再!      4.师 好!
""": "1"
    }

# -*- coding: utf-8 -*-

from nose.tools import *
from language_game.lesson1 import *
from language_game.lesson3 import *

def test_lessons():
    l1_pinyin = Lesson1PinYin()


    assert_equal(l1_pinyin.quiz['四'], 'si4')
    assert_equal(l1_pinyin.quiz['七'], 'qi1')

    l1_chars = Lesson1Chars()

    assert_equal(l1_chars.quiz["""yi1
1. 三    2. 六    3. 十    4. 一
    """], '4')
    assert_equal(l1_chars.quiz["""si4
1. 八    2. 四    3. 三    4. 六
    """], '2')

    l1_chars_eng = Lesson1CharsToEnglish()

    assert_equal(l1_chars_eng.quiz['五'], 'five')
    assert_equal(l1_chars_eng.quiz['九'], 'nine')

    l1_pinyin_eng = Lesson1PinYinToEnglish()

    assert_equal(l1_pinyin_eng.quiz['ba1'], 'eight')
    assert_equal(l1_pinyin_eng.quiz['shi1'], 'ten')


    l3_radicals_pinyin = Lesson3RadicalsPinYin()

    assert_equal(l3_radicals_pinyin.quiz['心'], 'xin1')
    assert_equal(l3_radicals_pinyin.quiz['女'], 'nu3')

    l3_radicals_chars = Lesson3RadicalsChars()

    assert_equal(l3_radicals_chars.quiz["""jin3
1.巾  2.心  3.女  4.亻  5.日
"""], '1')
    assert_equal(l3_radicals_chars.quiz["""xin1
1.巾  2.心  3.女  4.亻  5.日
"""], '2')

    l3_pinyin = Lesson3PinYin()

    assert_equal(l3_pinyin.quiz['您'], 'nin2')
    assert_equal(l3_pinyin.quiz['再'], 'zai4')

    l3_pinyin_phrases = Lesson3PinYinPhrases()

    assert_equal(l3_pinyin_phrases.quiz['您 早'], 'nin2 zao3')
    assert_equal(l3_pinyin_phrases.quiz['你 好'], 'ni3 hao3')

    l3_dialogue_pinyin = Lesson3DialoguePinYin()

    assert_equal(l3_dialogue_pinyin.quiz["""
1.1
老 师, 您 早!
    """], "lao3 shi1, nin2 zao3!")
    assert_equal(l3_dialogue_pinyin.quiz["""
3.1
老 师, 再 见!
    """], "lao3 shi1, zai4 jian4!")

    l3_dialogue_chars = Lesson3DialogueChars()

    assert_equal(l3_dialogue_chars.quiz["""
-------
1.2
ni3 zao3!

1.您 好!      2.您 好!      3.你 早!       4.师 好!
"""], '3')
    assert_equal(l3_dialogue_chars.quiz["""
-------
3.2
zai4 jian4!

1.再 见!      2.您 早!      3.见 再!      4.师 好!
"""], '1')


def test_lessonarchive():

    from language_game.lessonarchive import LessonArchive
    from language_game.lessonarchive import Main
    lesson_archive_main = Main()
    assert_equal(lesson_archive_main.run_main(), "Test successful!")

def test_score():

    from language_game.score import UserScore
    user_score = UserScore("Johnny", 10)

    assert_equal(user_score.inc_score(), 15)
    assert_equal(user_score.inc_strikes(), 1)


def test_main():
    from language_game.main import prompt_for_lesson
    from language_game.main import Engine
    from language_game.main import UserInterface
    from language_game.main import GameInterface

    engine_instance = Engine("Johnny", 10, '3', True, False)
    assert_equal(engine_instance.get_lesson_list(), "get_lesson_list call successful")
    assert_equal(engine_instance.play(), ("prompt_user call successful",
                                        "get_lesson_list call successful",
                                        "ask_keep_playing call successful"))

    ui_instance = UserInterface(False)
    assert_equal(ui_instance.prompt_user(), "prompt_user call successful")
    assert_equal(ui_instance.ask_keep_playing('Johnny', 10), "ask_keep_playing call successful")

    from language_game.lesson1 import Lesson1PinYin
    quiz_instance = Lesson1PinYin()
    game_interface = GameInterface('Johnny', 'characters', quiz_instance, 10, True, False, False)
    assert_equal(game_interface.launch(), (10, 0))

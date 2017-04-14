#!/usr/bin/python
# -*- coding: utf-8 -*-


class LessonArchive(object):

    def __init__(self, user_name, lesson_num, user_score, flag, run_game):
        self.user_name = user_name
        self.lesson_num = lesson_num
        self.user_score = user_score
        self.flag = flag
        self.run_game = run_game

    def run(self):

        ordered_quiz = False

        if self.lesson_num == '1' or self.lesson_num == '2':
            print """
            ---------------------
                LESSONS 1 & 2
            ---------------------
            """
            print
            print "Enter what you'd like to quiz: "
            print "- Characters"
            print "- Pinyin"
            print "- Characters to English"
            print "- PinYin to English"

            if self.flag == 1:
                quiz_choice = 'pinyin'
            else:
                quiz_choice = raw_input("> ")
                quiz_choice = quiz_choice.strip()
                quiz_choice = quiz_choice.lower()

            if quiz_choice == 'pinyin':
                from lesson1 import Lesson1PinYin
                quiz_instance = Lesson1PinYin()
            elif quiz_choice == 'characters':
                from lesson1 import Lesson1Chars
                quiz_instance = Lesson1Chars()
            elif quiz_choice == 'characters to english':
                from lesson1 import Lesson1CharsToEnglish
                quiz_instance = Lesson1CharsToEnglish()
            elif quiz_choice == 'pinyin to english':
                from lesson1 import Lesson1PinYinToEnglish
                quiz_instance = Lesson1PinYinToEnglish()

            next_lesson = '3'
        elif self.lesson_num == '3':
            print """
            ----------------
                LESSON 3
            ----------------
            """
            print
            print "Enter what you'd like to quiz: "
            print "- Radicals PinYin"
            print "- Radicals Characters"
            print "- PinYin"
            print "- PinYin Phrases"
            print "- Dialogue PinYin"
            print "- Dialogue Characters"

            quiz_choice = raw_input("> ")
            quiz_choice = quiz_choice.strip()
            quiz_choice = quiz_choice.lower()

            if quiz_choice == 'radicals pinyin':
                from lesson3 import Lesson3RadicalsPinYin
                quiz_instance = Lesson3RadicalsPinYin()
            elif quiz_choice == 'radicals characters':
                from lesson3 import Lesson3RadicalsChars
                quiz_instance = Lesson3RadicalsChars()
            elif quiz_choice == 'pinyin':
                from lesson3 import Lesson3PinYin
                quiz_instance = Lesson3PinYin()
            elif quiz_choice == 'pinyin phrases':
                from lesson3 import Lesson3PinYinPhrases
                quiz_instance = Lesson3PinYinPhrases()
            elif quiz_choice == 'radical pinyin':
                from lesson3 import Lesson3RadicalsPinYin
                quiz_instance = Lesson3RadicalsPinYin()
            elif quiz_choice == 'dialogue pinyin':
                from lesson3 import Lesson3DialoguePinYin
                quiz_instance = Lesson3DialoguePinYin()
                ordered_quiz = True
            elif quiz_choice == 'dialogue characters':
                from lesson3 import Lesson3DialogueChars
                quiz_instance = Lesson3DialogueChars()
                ordered_quiz = True

            next_lesson = '4'
        elif self.lesson_num == '4':
            print """
            ----------------
                LESSON 4
            ----------------
            """
            quiz_choice = raw_input("> ")
            quiz_choice = quiz_choice.strip()
            quiz_choice = quiz_choice.lower()

            if quiz_choice == 'pinyin':
                from lesson4 import Lesson4PinYin
                quiz_instance = Lesson4PinYin()
            elif quiz_choice == 'characters':
                from lesson4 import Lesson4Chars
                quiz_instance = Lesson4Chars()

            next_lesson = '5'
        else:
            print "Error!"


        if self.lesson_num == '3':
            add_numbers = False
        else:
            add_numbers = True


        if self.flag == 1:
            return "Test successful!"
        else:
            from main import GameInterface
            game_interface_instance = GameInterface(self.user_name, quiz_choice, quiz_instance, self.user_score, add_numbers, ordered_quiz, self.run_game)
            new_user_score, user_strikes = game_interface_instance.launch()

            return new_user_score, next_lesson, user_strikes


class Main(object):

    def run_main(self):
        lesson_arch = LessonArchive("Johnny", '1', 10, 1, False)
        successful = lesson_arch.run()
        return successful

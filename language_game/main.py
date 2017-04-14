#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def prompt_for_lesson(user_name):
    print
    print "Enter lesson number: "
    lesson_num = str(raw_input("> "))

    user_name = user_name.strip()
    user_name = user_name.lower()
    lesson_num = lesson_num.strip()
    lesson_num = lesson_num.lower()

    return user_name, lesson_num


class Engine(object):

    def __init__(self, user_name, user_score, lesson_num, first_round, run_game):
        self.user_name = user_name
        self.user_score = user_score
        self.lesson_num = lesson_num
        self.first_round = first_round
        self.run_game = run_game


    def get_lesson_list(self):
        from lessonarchive import LessonArchive

        lessonarchive_instance = LessonArchive(self.user_name, self.lesson_num, self.user_score, 0, self.run_game)

        if __name__ == "__main__" or self.run_game:
            new_user_score, next_lesson, user_strikes = lessonarchive_instance.run()
            return new_user_score, next_lesson, user_strikes
        else:
            return "get_lesson_list call successful"

    def play(self):

        if self.first_round == True:

            if __name__ == "__main__" or self.run_game:
                user_interface_instance = UserInterface(True)
                self.user_name, self.lesson_num = user_interface_instance.prompt_user()
            else:
                user_interface_instance = UserInterface(False)
                return1 = user_interface_instance.prompt_user()

        engine_instance = Engine(self.user_name, self.user_score, self.lesson_num, self.first_round, self.run_game)

        if __name__ == "__main__" or self.run_game:
            self.user_score, next_lesson, user_strikes = engine_instance.get_lesson_list()
        else:
            return2 = engine_instance.get_lesson_list()

        if __name__ == "__main__" or self.run_game:
            user_interface_instance = UserInterface(True)
            if user_strikes == 3:
                self.user_score = 0
            user_interface_instance.ask_keep_playing(self.user_name, self.user_score)
        else:
            user_interface_instance = UserInterface(False)
            return3 = user_interface_instance.ask_keep_playing(self.user_name, self.user_score)

        return return1, return2, return3

class UserInterface(object):
    # Prompt the user for their name, lesson_num level, & character-type
    # and set the raw_input values to the attributes
    # user_name, and lesson_num.

    def __init__(self, run_game):
        self.run_game = run_game

    def prompt_user(self):
        if __name__ == "__main__" or self.run_game:
            print """
            --------------------------------------------------
            --------------------------------------------------
                C H I N E S E   C H A R A C T E R  G A M E
            --------------------------------------------------
            --------------------------------------------------

            """
            print
            print "Enter name: "
            user_name = raw_input("> ")

            return prompt_for_lesson(user_name)
        else:
            return "prompt_user call successful"

    def ask_keep_playing(self, user_name, user_score):
        if __name__ == "__main__" or self.run_game:
            print "Keep playing?"
            choice = raw_input("> ")
            choice = choice.strip()
            choice = choice.lower()

            if choice == 'yes':
                user_name, lesson_num = prompt_for_lesson(user_name)
                engine_instance = Engine(user_name, user_score, lesson_num, False, True)
                engine_instance.play()
            else:
                print "Exiting . . ."
                sys.exit(0)

        else:
            return "ask_keep_playing call successful"

class GameInterface(UserInterface):

    def __init__(self, user_name, quiz_choice, quiz_instance, user_score, add_numbers, ordered_quiz, run_game):
        self.user_name = user_name
        self.quiz_choice = quiz_choice
        self.quiz_instance = quiz_instance
        self.user_score = user_score
        self.add_numbers = add_numbers
        self.ordered_quiz = ordered_quiz
        self.run_game = run_game

    def launch(self):

        import random

        from score import UserScore
        user_score_instance = UserScore(self.user_name, self.user_score)

        user_strikes = 0

        # This if-else statement checks if the given quiz already has
        # a pre-determined order.
        if self.ordered_quiz:
            quiz = self.quiz_instance.quiz
            dict_questions = sorted(self.quiz_instance.quiz.keys())

        else:
            quiz = self.quiz_instance.quiz
            dict_questions = list(quiz.keys())
            random.shuffle(dict_questions)

        i = 0

        for question in dict_questions:

            dict_answer = quiz[question]

            if __name__ == "__main__" or self.run_game:
                print
                print

                if self.add_numbers:
                    print "%d. " % (i+1)
                else:
                    print

                char_choice = (self.quiz_choice == 'characters' or
                    self.quiz_choice == 'radicals characters' or
                    self.quiz_choice == 'dialogue characters')
                pinyin_choice = (self.quiz_choice == 'pinyin' or
                    self.quiz_choice == 'radicals pinyin' or
                    self.quiz_choice == 'pinyin phrases' or
                    self.quiz_choice == 'dialogue pinyin')

                if char_choice:
                    question_prompt = "PINYIN: "
                    answer_prompt = "ANSWER: "
                elif pinyin_choice:
                    question_prompt = "CHARACTERS: "
                    answer_prompt = "PINYIN: "
                elif self.quiz_choice == 'characters to english':
                    question_prompt = "CHARACTERS: "
                    answer_prompt = "ENGLISH: "
                elif self.quiz_choice == 'pinyin to english':
                    question_prompt = "PINYIN: "
                    answer_prompt = "ENGLISH: "

                print question_prompt, question

                user_answer = raw_input("> ")
                user_answer = user_answer.strip(' ')
                user_answer = user_answer.lower()

                print answer_prompt, dict_answer
                print
                print

                if user_answer == dict_answer:
                    self.user_score = user_score_instance.inc_score()
                else:
                    user_strikes = user_score_instance.inc_strikes()

                if user_strikes == 3:
                    break

                print ("------------------------------------------------------------------------------")

        return self.user_score, user_strikes

#!/usr/bin/python

class UserScore(object):

    def __init__(self, user_name, user_score, user_strikes=0):
            self.user_name = user_name
            self.user_score = user_score
            self.user_strikes = user_strikes

    def inc_score(self):
        self.user_score += 5
        print "SCORE: ", self.user_score
        print "STRIKES: ", self.user_strikes

        return self.user_score

    def inc_strikes(self):
        self.user_strikes += 1
        print "SCORE: ", self.user_score
        print "STRIKES: ", self.user_strikes

        if self.user_strikes == 3:
            self.user_name = self.user_name.upper()

            print """
            %s, YOU HAVE ACCUMULATED THREE STRIKES

            TOTAL SCORE: %d
            -----------------------------------------
            -----------------------------------------
                G   A   M   E       O   V   E   R
            -----------------------------------------
            -----------------------------------------
            """ % (self.user_name, self.user_score)

        return self.user_strikes

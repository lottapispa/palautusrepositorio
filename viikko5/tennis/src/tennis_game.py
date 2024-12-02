class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def tie_point_calls(self):
        if self.m_score1 == 0:
            self.score = "Love-All"
        elif self.m_score1 == 1:
            self.score = "Fifteen-All"
        elif self.m_score1 == 2:
            self.score = "Thirty-All"
        else:
            self.score = "Deuce"

    def advantage_score_calls(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            self.score = "Advantage player1"
        elif minus_result == -1:
            self.score = "Advantage player2"
        elif minus_result >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"

    def point_calls(self):
        for i in range(1, 3):
            if i == 1:
                self.temp_score = self.m_score1
            else:
                self.score += "-"
                self.temp_score = self.m_score2

            if self.temp_score == 0:
                self.score += "Love"
            elif self.temp_score == 1:
                self.score += "Fifteen"
            elif self.temp_score == 2:
                self.score += "Thirty"
            elif self.temp_score == 3:
                self.score += "Forty"

    def get_score(self):
        self.score = ""
        self.temp_score = 0

        if self.m_score1 == self.m_score2:
            self.tie_point_calls()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            self.advantage_score_calls()
        else:
            self.point_calls()

        return self.score

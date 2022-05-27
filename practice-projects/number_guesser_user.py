class User():
    def __init__(self):
        with open("./max-score.txt", "r", encoding="UTF-8") as max_score_sheet:
            for _ in max_score_sheet:
                max_score_user = int(_)
                self.max_score = max_score_user
        with open("./best-time.txt", "r", encoding="UTF-8") as best_time_sheet:
            for _ in best_time_sheet:
                best_time_user = int(_)
                if best_time_user > 10000000000000000000000000000000000000000000000000000000000:
                    self.best_time = "Aun no has jugado alguna partida, comienza a jugar para obtener un mejor tiempo"
                if best_time_user < 10000000000000000000000000000000000000000000000000000000000:    
                    self.best_time = best_time_user 
        with open("./level.txt", "r", encoding="UTF-8") as level_sheet:
            for _ in level_sheet:
                level_user = int(_)
                self.level = level_user
        with open("./number_of_wins.txt", "r", encoding="UTF-8") as num_wins_user_sheet:
            for _ in num_wins_user_sheet:
                num_wins_user_value = int(_)
                self.wins = num_wins_user_value
    def new_max_score(self, new_max_user_score):
        self.max_score = new_max_user_score
    def new_best_time(self, new_best_user_time):
        self.best_time = new_best_user_time
    def new_level(self,new_user_level):
        self.level = new_user_level  
    def total_wins(self,new_number_of_wins):
        self.wins = new_number_of_wins         



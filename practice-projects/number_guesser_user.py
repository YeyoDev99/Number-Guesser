class User():
    def __init__(self, max_score = 0, best_time=0,level = 0):
        self.max_score = max_score
        self.best_time = best_time
        self.level = level
    def new_max_score(self, new_max_user_score):
        self.max_score = new_max_user_score
    def new_best_time(self, new_best_user_time):
        self.best_time = new_best_user_time
    def new_level(self,new_user_level):
        self.level = new_user_level       




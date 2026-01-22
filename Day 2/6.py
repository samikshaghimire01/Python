#  Implement a class Team with len so that len(team) returns the number of players.

class Team:
    def __init__(self, players):
        self.players = players  

    def __len__(self):
        return len(self.players)

team = Team(["Sam", "Pranu", "Supps", "Dipi"])

print(len(team)) 

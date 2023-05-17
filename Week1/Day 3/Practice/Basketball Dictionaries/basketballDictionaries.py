players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]



# Challenge 1: Update the Constructor




class Player:
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age =player_info["age"] 
        self.position = player_info["position"]
        self.team = player_info["team"]
        
    def display(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)
        
    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
        return display
        
        
    @classmethod
    def get_team(cls, team_list):
        new_list=[]
        for player_info in team_list:
            player_add=Player(player_info)
            new_list.append(player_add)
        return new_list


# Challenge 2: Create instances using individual player dictionaries.
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

player_1=Player(kevin)
player_1=Player(jason)
player_1=Player(kyrie)
# ! testing class method
team_players = Player.get_team(players)
print(team_players)





# Challenge 3: Make a list of Player instances from a list of dictionaries

new_team=[]
for player_info in players:
        player_add=Player(player_info)
        new_team.append(player_add)
print(new_team)

# Football Team Managmenet System

# შექმენით კლასი FootballTeam შემდეგი ატრიბუტებით:
# team_name (string) - კლუბის სახელი
# coach (string) - მწვრთნელი
# players - მოთამაშეების სია(შექმნისას ცარიელი უნდა იყოს)

# კლასს უნდა გააჩნდეს შემდეგი მეთოდები:
# 1. მოთამაშის დამატება - მოთამაშის სახელი, პოზიცია, სათამაშო ნომერი, 
#    ასაკი და ეროვნება(დიქტის სახით უნდა დაემატოს მოთამაშეების სიაში)

# 2. მოთამაშის წაშლა - მოთამაშე უნდა წაიშალოს სიიდან სათამაშო ნომრის მიხედვით

# 3. მოთამაშის ინფორმაციის განახლება - მოთამაშე უნდა მონახოთ სათამაშო ნომრის მიხედვით
#    და უნდა დაუსეტოთ ისეთი ინფორმაცია, რომელსაც გადასცემთ ამ მეთოდს, მაგ: "goal": 1 
#    ანუ key და value უნდა იყოს გადაცემული ამავე მეთოდის გამოძახებისას!

# 4. კლუბის ინფორმაციის ჩვენება - გამოიტანეთ კლუბის სახელი, მწვრთნელის სახელი და მოთამაშეების სია

# 5. მოთამაშის ინფორმაციის ჩვენება - უნდა გამოიტანოთ ინფორმაცია მოთამაშის ნომრის მიხედვით


class Football_Team_Managmenet_System:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []
#1)
    def add_players(self, player_name, player_position, number, age, nationality):
        player = {
            'name': player_name,
            'position': player_position,
            'number': number,
            'age': age,
            'nationality': nationality
        }
        self.players.append(player)
#2)
    def remove_player(self, number):
        for player in self.players:
            player['number'] == number
            self.players.remove(player)
            print(f"Player with number {number} has been removed.")
            break
#3)
    def update_player_info(self, number, **kwargs):
        for player in self.players:
            player['number'] == number
            for key, value in kwargs.items():
                player[key] = value
            break
#4)
    def show_team_info(self):
        print(f"Team Name: {self.team_name}")
        print(f"Coach: {self.coach}")
        print("Players:")
        self.players
        for player in self.players:
            print(f"- {player['name']} (Position: {player['position']}, Number: {player['number']}, Age: {player['age']}, Nationality: {player['nationality']})")
#5)
    def show_player_info(self, number):
            for player in self.players:
                if player['number'] == number:
                    print(f"Player Information:")
                    print(f"Name: {player['name']}")
                    print(f"Position: {player['position']}")
                    print(f"Number: {player['number']}")
                    print(f"Age: {player['age']}")
                    print(f"Nationality: {player['nationality']}")
                    break
            else:
                print(f"Player with number {number} not found.")

# წინა დავალება გადააკეთეთ შემდეგნაირად:

# ცალკე შექმენით მოთამაშის კლასი შემდეგი ატრიბუტებით:
# მოთამაშის აიდი: ავტომატურად ენიჭებოდეს და იზრდებოდეს ერთით ყოველი მოთამაშის ობიექტის შექმნისას,
# სახელი, პოზიცია, სათამაშო ნომერი(private), ასაკი(private) და ეროვნება.

# მეთოდები:
# მოთამაშის სრული ინფორმაციის ჩვენება,
# __str__,
# სურვილისამებრ შეგიძლიათ დაუმატოთ მეთოდები

# ცალკე შექმენით მწვრთნელის კლასი შემდეგი ატრიბუტებით:
# სახელი და გამოცდილების წლები(private).

# მეთოდები:
# მწვრთნელის სრული ინფორმაციის ჩვენება,
# __str__
# სურვილისამებრ შეგიძლიათ დაუმატოთ მეთოდები

# საბოლოოდ შექმენით Team კლასი შემდეგი ატრიბუტებით:
# სახელი, მწვრთნელი(მწვრთნელის ობიექტი) და მოთამაშეები(მოთამაშის ობიექტების სია).
# მეთოდები:
# მოთამაშის დამატება,
# მოთამაშის ძებნა აიდის მიხედვით და ინფორმაციის გამოტანა,
# მოთამაშის ინფორმაციის განახლება(წინა დავალების ანალოგიურად ოღონდ აიდის მიხედვით),
# მოთამაშის წაშლა(აიდის მიხედვით),
# კლუბის სრული ინფორმაციის ჩვენება(სახელი, მწვრთნელი, მოთამაშეები),
# __str__

# ბონუსი: კლუბში ვერ უნდა ემატებოდეს 25 მოთამაშეზე მეტი,
# აწარმოეთ მოთამაშის სტატისტიკა(რამდენი მატჩი ითამაშა, რამდენი გოლი გაიტანა და ა.შ.)

# class Football_Team_Managmenet_System:
#     def __init__(self, team_name, Coach_class):
#         self.team_name = team_name
#         self.coach = Coach_class
#         players = []

#     def add_players(self, player_name, player_position, number, age, nationality):
#         player = {
#             'name': player_name,
#             'position': player_position,
#             'number': number,
#             'age': age,
#             'nationality': nationality
#         }
#         self.players.append(player)

#     def remove_player(self, number):
#         for player in self.players:
#             player['number'] == number
#             self.players.remove(player)
#             print(f"Player with number {number} has been removed.")
#             break

#     def update_player_info(self, number, **kwargs):
#         for player in self.players:
#             player['number'] == number
#             for key, value in kwargs.items():
#                 player[key] = value
#             break

#     def show_team_info(self):
#         print(f"Team Name: {self.team_name}")
#         print(f"Coach: {self.coach}")
#         print("Players:")
#         self.players
#         for player in self.players:
#             print(f"- {player['name']} (Position: {player['position']}, Number: {player['number']}, Age: {player['age']}, Nationality: {player['nationality']})")

#     def show_player_info(self, number):
#             for player in self.players:
#                 if player['number'] == number:
#                     print(f"Player Information:")
#                     print(f"Name: {player['name']}")
#                     print(f"Position: {player['position']}")
#                     print(f"Number: {player['number']}")
#                     print(f"Age: {player['age']}")
#                     print(f"Nationality: {player['nationality']}")
#                     break
#             else:
#                 print(f"Player with number {number} not found.")
        
# ეს იმიტო გადმოვიტანე რეფერენცისთვის მინდოდა


class Player_class:
    _id_counter = 1

    def __init__(self, player_name, position,number, age, nationality):
        self.player_id = Player_class._id_counter
        Player_class._id_counter += 1
        self.player_name = player_name
        self.position = position
        self.__number = number
        self.__age = age
        self.nationality = nationality

    def get_number(self):
        return self.__number
    
    def get_age(self):
        return self.__age

    def __str__(self):
        return f"Player ID: {self.player_id}\nName: {self.player_name}\nPosition: {self.position}\nNumber: {self.__number}\nAge: {self.__age}\nNationality: {self.nationality}"
    
class Coach_class:
    def __init__(self, coach_name, experience):
        self.coach_name = coach_name
        self.__experience = experience

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return f"Coach Name: {self.coach_name}\nExperience: {self.__experience}"
    
    
class The_Football_Team:
    def __init__(self,FootballTeam_name, coach, Players):
        self.FootballTeam_name = FootballTeam_name
        self.coach = Coach_class
        self.players = []

    def add_players(self, players):
        if len(self.players) < 25:
            self.players.append(players) # ეს არ გამიტესტია ამდენი მსახიობების მოფიქრება შემეზარა
        else:
            print("The Player Limit Has Been Reached (This Town Ain't Big Enough For More Than 25 Of Us Partner!)") #;-)

    def find_player_byid(self, player_id):
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None
    
    def update_player_info_byid(self, player_id, **kwargs):
        player = self.find_player_byid(player_id)
        for key, value in kwargs.items():
            setattr(player, key, value)

    def remove_player_byid(self, player_id):
        player = self.find_player_byid(player_id)
        self.players.remove(player)

    def __str__(self, FootballTeam_name, coach, Players):
        return f"Team Name: {self.FootballTeam_name} \nCoach: {self.coach} \nPlayers: {self.Players}"
        
    

player1 = Player_class("Adriano", "Celentano", 6, 87, "Holywood?")
player2 = Player_class("Antonio", "Banderas", 10, 64, "Spanish")
coach1 = Coach_class("John James Rambo", 10)

player1.update_player_info_byid(1,"Adriano","Celentano", 6, 87, "Italiano")

Team1 = The_Football_Team("HolyWood Stars", coach1, [player1])

Team1.add_players(player2)

print(Team1)
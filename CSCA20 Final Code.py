my_list_1 = [800,0,0]
my_list_2 = [500,0,0]
my_list_3 = [200,25,0]
my_list_4 = [250,75,0]
my_list_5 = [300,0,80]
my_list_6 = [350,0,65]
HP = 0
AP = 0
AD = 0

name = input("what hero?")
division = input("please entre Tank or Attack Power Hero or Ability Power Hero, otherwise the suggestion will be inaccurate:")
gear1 = input("what is your first gear?choose from g1 to g6:")
if gear1 == "g1":
    HP = my_list_1[0] 
    AD = my_list_1[1]
    AP = my_list_1[2]
if gear1 == "g2":
    HP = my_list_2[0] 
    AD = my_list_2[1]
    AP = my_list_2[2]
if gear1 == "g3":
    HP = my_list_3[0] 
    AD = my_list_3[1]
    AP = my_list_3[2]
if gear1 == "g4":
    HP = my_list_4[0] 
    AD = my_list_4[1]
    AP = my_list_4[2]
if gear1 == "g5":
    HP = my_list_5[0] 
    AD = my_list_5[1]
    AP = my_list_5[2]
if gear1 == "g6":
    HP = my_list_6[0] 
    AD = my_list_6[1]
    AP = my_list_6[2]
gear2 = input("what is your second gear?choose from  g1 to g6:")
if gear2 == 'g1':
    HP = HP + my_list_1[0] 
    AD = AD + my_list_1[1]
    AP = AP + my_list_1[2]
if gear2 == "g2":
    HP = HP + my_list_2[0] 
    AD = AD + my_list_2[1]
    AP = AP + my_list_2[2]
if gear2 == "g3":
    HP = HP + my_list_3[0] 
    AD = AD + my_list_3[1]
    AP = AP + my_list_3[2]
if gear2 == "g4":
    HP = HP + my_list_4[0] 
    AD = AD + my_list_4[1]
    AP = AP + my_list_4[2]
if gear2 == "g5":
    HP = HP + my_list_5[0] 
    AD = AD + my_list_5[1]
    AP = AP + my_list_5[2]
if gear2 == "g6":
    HP = HP + my_list_6[0] 
    AD = AD + my_list_6[1]
    AP = AP + my_list_6[2]

gear3 = input("what is your third gear?choose from  g1 to g6:")
if gear3 == 'g1':
    HP = HP + my_list_1[0] 
    AD = AD + my_list_1[1]
    AP = AP + my_list_1[2]
if gear3 == "g2":
    HP = HP + my_list_2[0] 
    AD = AD + my_list_2[1]
    AP = AP + my_list_2[2]
if gear3 == "g3":
    HP = HP + my_list_3[0] 
    AD = AD + my_list_3[1]
    AP = AP + my_list_3[2]
if gear3 == "g4":
    HP = HP + my_list_4[0] 
    AD = AD + my_list_4[1]
    AP = AP + my_list_4[2]
if gear3 == "g5":
    HP = HP + my_list_5[0] 
    AD = AD + my_list_5[1]
    AP = AP + my_list_5[2]
if gear3 == "g6":
    HP = HP + my_list_6[0] 
    AD = AD + my_list_6[1]
    AP = AP + my_list_6[2]


gear4 = input("what is your fourth gear?choose from  g1 to g6:")
if gear4 == 'g1':
    HP = HP + my_list_1[0] 
    AD = AD + my_list_1[1]
    AP = AP + my_list_1[2]
if gear4 == "g2":
    HP = HP + my_list_2[0] 
    AD = AD + my_list_2[1]
    AP = AP + my_list_2[2]
if gear4 == "g3":
    HP = HP + my_list_3[0] 
    AD = AD + my_list_3[1]
    AP = AP + my_list_3[2]
if gear4 == "g4":
    HP = HP + my_list_4[0] 
    AD = AD + my_list_4[1]
    AP = AP + my_list_4[2]
if gear4 == "g5":
    HP = HP + my_list_5[0] 
    AD = AD + my_list_5[1]
    AP = AP + my_list_5[2]
if gear4 == "g6":
    HP = HP + my_list_6[0] 
    AD = AD + my_list_6[1]
    AP = AP + my_list_6[2]


gear5 = input("what is your fifth gear?choose from  g1 to g6:")
if gear5 == 'g1':
    HP = HP + my_list_1[0] 
    AD = AD + my_list_1[1]
    AP = AP + my_list_1[2]
if gear5 == "g2":
    HP = HP + my_list_2[0] 
    AD = AD + my_list_2[1]
    AP = AP + my_list_2[2]
if gear5 == "g3":
    HP = HP + my_list_3[0] 
    AD = AD + my_list_3[1]
    AP = AP + my_list_3[2]
if gear5 == "g4":
    HP = HP + my_list_4[0] 
    AD = AD + my_list_4[1]
    AP = AP + my_list_4[2]
if gear5 == "g5":
    HP = HP + my_list_5[0] 
    AD = AD + my_list_5[1]
    AP = AP + my_list_5[2]
if gear5 == "g6":
    HP = HP + my_list_6[0] 
    AD = AD + my_list_6[1]
    AP = AP + my_list_6[2]

gear6 = input("what is your sixth gear?choose from  g1 to g6:")
if gear6 == 'g1':
    HP = HP + my_list_1[0] 
    AD = AD + my_list_1[1]
    AP = AP + my_list_1[2]
if gear6 == "g2":
    HP = HP + my_list_2[0] 
    AD = AD + my_list_2[1]
    AP = AP + my_list_2[2]
if gear6 == "g3":
    HP = HP + my_list_3[0] 
    AD = AD + my_list_3[1]
    AP = AP + my_list_3[2]
if gear6 == "g4":
    HP = HP + my_list_4[0] 
    AD = AD + my_list_4[1]
    AP = AP + my_list_4[2]
if gear6 == "g5":
    HP = HP + my_list_5[0] 
    AD = AD + my_list_5[1]
    AP = AP + my_list_5[2]
if gear6 == "g6":
    HP = HP + my_list_6[0] 
    AD = AD + my_list_6[1]
    AP = AP + my_list_6[2]

if division == "Tank":
  if HP > 3000:
    print("this equipment combination is reasonable")
  else:
      print("please change the equipment combination, HP need to be improved")

if division == "Attack Power Hero":
  if AD > 100:
    print("this equipment combination is reasonable")
  else:
      print("please change the equipment combination, AD need to be improved")

if division == "Ability Power Hero":
  if AP > 100:
    print("this equipment combination is reasonable")
  else:
      print("please change the equipment combination, AP need to be improved")

print("here is your property table")
print(HP)
print(AD)
print(AP)

print("here is free hero this week!resource from League of Legend offcial website!")
import requests
url = 'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=RGAPI-610e1919-71fc-4504-897e-1c4dcf6a4b99'
r = requests.get(url)
string = (r.json()["freeChampionIds"])
print (string)
data = {
    266:"Aatrox",
    412:"Thresh",
    23: "Tryndamere",
    79: "Gragas",
    69: "Cassiopeia",
    136:"Aurelion Sol",
    13: "Ryze",
    78: "Poppy",
    14: "Sion",
    1: "Annie",
    202:"Jhin",
    43: "Karma",
    111:"Nautilus",
    240:"Kled",
    99: "Lux",
    103:"Ahri",
    2: "Olaf",
    112:"Viktor",
    34: "Anivia",
    27: "Singed",
    86: "Garen",
    127:"Lissandra",
    57: "Maokai",
    25: "Morgana",
    28: "Evelynn",
    105:"Fizz",
    74: "Heimerdinger",
    238:"Zed",
    68: "Rumble",
    82: "Mordekaiser",
    37: "Sona",
    96: "Kog'Maw",
    55: "Katarina",
    117:"Lulu",
    22: "Ashe",
    30: "Karthus",
    12: "Alistar",
    122:"Darius",
    67: "Vayne",
    110:"Varus",
    77: "Udyr",
    89: "Leona",
    126:"Jayce",
    134:"Syndra",
    80: "Pantheon",
    92: "Riven",
    121:"Kha'Zix",
    42: "Corki",
    268:"Azir",
    51: "Caitlyn",
    76: "Nidalee",
    85: "Kennen",
    3: "Galio",
    45: "Veigar",
    432:"Bard",
    150:"Gnar",
    90: "Malzahar",
    104:"Graves",
    254:"Vi",
    10: "Kayle",
    39: "Irelia",
    64: "Lee Sin",
    420:"Illaoi",
    60: "Elise",
    106:"Volibear",
    20: "Nunu",
    4: "Twisted Fate",
    24: "Jax",
    102:"Shyvana",
    429:"Kalista",
    36: "Dr. Mundo",
    427:"Ivern",
    131:"Diana",
    223:"Tahm Kench",
    63: "Brand",
    113:"Sejuani",
    8: "Vladimir",
    154:"Zac",
    421:"Rek'Sai",
    133:"Quinn",
    84: "Akali",
    163:"Taliyah",
    18: "Tristana",
    120:"Hecarim",
    15: "Sivir",
    236:"Lucian",
    107:"Rengar",
    19: "Warwick",
    72: "Skarner",
    54: "Malphite",
    157:"Yasuo",
    101:"Xerath",
    17: "Teemo",
    75: "Nasus",
    58: "Renekton",
    119:"Draven",
    35: "Shaco",
    50: "Swain",
    91: "Talon",
    40: "Janna",
    115:"Ziggs",
    245:"Eko",
    61: "Orianna",
    114:"Fiora",
    9: "Fiddlesticks",
    31: "Cho'Gath",
    33: "Rammus",
    7: "LeBlanc",
    16: "Soraka",
    26: "Zilean",
    56: "Nocturne",
    222:"Jinx",
    83: "Yorick",
    6: "Urgot",
    203:"Kindred",
    21: "Miss Fortune",
    62: "Wukong",
    53: "Blitzcrank",
    98: "Shen",
    201:"Braum",
    5: "Xin Zhao",
    29: "Twitch",
    11: "Master Yi",
    44: "Taric",
    32: "Amumu",
    41: "Gangplank",
    48: "Trundle",
    38: "Kassadin",
    161:"Vel'Koz",
    143:"Zyra",
    267:"Nami",
    59: "Jarvan IV",
    81: "Ezreal",
    325: "Senna",
    235:"God Mel"
}
for id in string:
    print(data[id])

print("these are free hero this week!")


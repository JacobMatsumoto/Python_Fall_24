import random


def main():
    franchises = ['ToyStory', 'MadMax', 'Shrek', 'FindingNemo', 'HowtoTrainYourDragon', 'DespicableMe', 'Cars', 'MonstersInc.', 'TheIncredibles', 'KungFuPanda', 'Madagascar', 'TheLegoMovie', 'Frozen', 'Moana', 'Zootopia', 'Trolls', 'Coco',
                  'TheSecretLifeofPets', 'Sing', 'TheJungleBook', 'BeautyandtheBeast', 'Aladdin', 'TheLionKing', 'FrozenII', 'Encanto', 'Spider-ManIntotheSpider-Verse', 'TheLittleMermaid', 'Ratatouille', 'InsideOut', 'Up', 'ToyStory4', 'Onward']
    users_name = ['James', 'JayKizer', 'AstroBoy', 'JasonGomez', 'EricPayton',
                  'EarlDube', 'ChristianWestonChandler', 'Stephany', 'NiletheHeroBoy', 'MikeOxlong']
    user_birthday = ['12/2/90', '11/4/01', '2001', '4/24',
                     '2003', '4/20', '5/23', '4/22/1992', '3/2/2022', '6/5/1998']
    user = []
    franchise_1 = random.randrange(0, 29)
    franchise_2 = random.randrange(0, 29)
    while franchise_2 == franchise_1:
        franchise_2 = random.randrange(0, 29)
    name = random.randrange(0, 9)
    bday = random.randrange(0, 9)
    uname = users_name[name]
    user.append(uname)
    ubday = user_birthday[bday]
    user.append(ubday)
    fran = franchises[franchise_1]
    user.append(fran)
    user.append('YES')
    fran = franchises[franchise_2]
    user.append(fran)
    user.append('NO')
    user_details = ''.join(user)
    user_details.strip

    print(user_details)


main()

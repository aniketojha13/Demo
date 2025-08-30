print("WELCOME!!!")

print("")

print("*ENTER ANY NAME TO KNOW HIM*")

print("")

print("Mohit,Sumit,Vaibhav,Ayush,Shabd")

print("Ashish,Amit,Bhaskar,Aniket,Nikhil")

print("")

import pandas as pd



data = {

    'Student Name': ['Mohit', 'Sumit', 'Vaprint("WELCOME!!!")print("")print("*ENTER ANY NAME TO KNOW HIM*")print("")print("Mohit,Sumit,Vaibhav,Ayush,Shabd")print("Ashish,Amit,Bhaskar,Aniket,Nikhil")print("")import pandas as pddata = {    'Student Name': ['Mohit', 'Sumit', 'Vaibhav', 'Ayush', 'Shabd', 'Ashish', 'Amit', 'Bhaskar', 'Aniket', 'Nikhil'],
    'Funny Ability': ['Joke telling', 'Comic timing', 'Pun-making', 'Prankster', 'Meme creating', 'Cool Attitude', 'Dead jokes', 'Joker', '-------', 'Flying in the Sky'],
    'Code Name': ['Gole', 'Doremon', 'Bebo', 'Mahesh', 'Meetha', 'KELI', 'Dark Fanstasy', 'Jokesy', 'OG', 'Mosquito'],
    'Superpower': ['Muscle Power', 'Devil Smile', 'Ben Stokes', 'Nothing','jaggery Behaviour', 'Being Supportive', 'Silent Killing machine', 'Innocent Thobda', '-------', 'His wings'],
    'Strength': ['Beast Body', 'Chemistry Period', 'Ashram', '522','00', 'Mountain Dew', 'Balcony', 'Phekus', '-------', 'Light body'],
    'Source of Energy': ['Behisab khana', 'Tuglakabad', 'Rooh afja', 'Water bottle','Sweety Supari', 'Physique', 'Being too innocent', 'Sence Organ', '-------', 'Lean Body'],
'Ambition':['Dr. Hongkong','Mr. Mevla Maharaj','Dr. Gynecologist','Mr. Mariz','Mr. Barfi','Mr. Marinda','Redi wala','Mr. Udisha','______','Flying Jatt'],
    'Birthday': ['28 October', '15 August', '24 November', '31 January','11 May', '-------', '-------', '-------', '13 August', '29 February']}
df = pd.DataFrame(data)
df.index = ('Mohit', 'Sumit', 'Vaibhav', 'Ayush', 'Shabd', 'Ashish', 'Amit', 'Bhaskar', 'Aniket','Nikhil')
while True:
    z = input("ENTER THE NAME: ")
    random_index_label = z
    row = df.loc[random_index_label]
    print(row)
    print("")
    print("*Thanks For Using Our Code*")
    print("")
    print("You Can Try Another One.")
    if z == 'exit':
        print("Exiting input loop...")
        break;
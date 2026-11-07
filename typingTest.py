from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except :
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)   
    speed = len(userinput) / time_r
    return round(speed)

test = [
    "Python ek powerful programming language hai.Iska use web development aur automation me hota hai.Yeh beginners ke liye bhi easy hai.",

    "HTML aur CSS website banane ke basic tools hain. Inse webpage ka structure aur design tayar hota hai. Web development ki shuruaat yahin se hoti hai.",

    "Data Analysis se useful insights nikale jate hain. Python me Pandas aur NumPy popular libraries hain. Companies decision making ke liye iska use karti hain.",

    "Machine Learning AI ka ek important hissa hai.Isse computer data se patterns seekhta hai. Prediction aur automation me iska use hota hai.",

    "Database me data ko store aur manage kiya jata hai. SQL ek popular database language hai. Iska use applications me bahut hota hai.",

    "Cricket duniya ke sabse lokpriya khelon me se ek hai. Is khel ko do teamon ke beech khela jata hai. Har team jeetne ke liye adhik run banane ki koshish karti hai.",

    "Batsman ka mukhya kaam run banana hota hai. Woh bowler ki gendon ka saamna karta hai. Acchi batting team ko majboot score dilati hai.",

    "Bowler wicket lene aur run rokne ki koshish karta hai. Fast aur spin bowling cricket ke do pramukh prakar hain. Acchi bowling match ka rukh badal sakti hai.",

    "Fielders maidan me alag-alag sthanon par khade hote hain. Unka kaam ball ko rokna aur catch pakadna hota hai. Tez fielding team ko fayda pahunchati hai.",

    "Cricket World Cup sabse bada antarashtriya tournament mana jata hai. Isme duniya ki shreshth teams bhaag leti hain. Har khiladi apne desh ke liye behtareen pradarshan karna chahta hai.",
]

if __name__ == "__main__":
    print("Welcome to the Typing Speed Test!")
    print("You will be given a random text to type.")
    print("Type it as fast and accurately as you can.")
    print("Let's begin!")
    print()
    while True:
        ck = input("Do you want to take typing test? (y/n): ")
        if ck.lower() == "y":
            letsTest = r.choice(test)
            print("Typing Test: ")
            print(letsTest)
            print()
            print()
            time1 = time()
            testinput = input("Type the above text: ")
            time2 = time()
            print("Speed: ", speed_time(time1, time2, testinput), "characters per second")
            print("Error: ", mistake(letsTest, testinput), "mistakes")
        elif ck.lower() == "n":
            print("Thank you for using the typing test.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
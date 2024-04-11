import random, string


# Takes in a NickName 
def guessNickName(name:str):
    nickName = name[0:3]
    return nickName

# Takes in a Pet Nickname
def generatePetName(name:str):
    nickName = name[0:3] + name[0:3]
    return nickName

# Takes in a NickName and generates a Spanish style name abbreviation

def generateSpanishNickName(name:str):
    prefix = name[0:3]
    nickName = name + "ito"
    
    if(prefix.endswith("e") or prefix.endswith("i")) : 
        name[0:4]
        return name +"ito"
    
    else :    
        return nickName


# Takes in an Animal nickname
def generateAnimalNickName(name:str):
    prefix = name[0:3]
   
    if prefix[0] == "M":
       nickName = "Tiger" + prefix
    elif prefix[0]=="A":
       nickName = "Bunny" + prefix
    elif prefix[0] == "E":
        nickName= "Elegant Elephant" + prefix
    else:
       nickName= "Sardine" + prefix

    return nickName
   


# Takes in a User's name and returns a DJ name
def generateDJNickName(name:str):
    nickname = ""
    if name.startswith("D") or name.startswith("B") or name.startswith("J") or name.startswith("K"):
        nickname = "DJ BoogeyDown " + name
    elif name.startswith("A") or name.startswith("C") or name.startswith("Z") or name.startswith("F"):
        nickname = "DJ LargerThanLife " + name
    elif name.startswith("U") or name.startswith("E") or name.startswith("L") or name.startswith("M"):
        nickname = "DJ Frostbite " +  name
    elif name.startswith("T") or name.startswith("N") or name.startswith("G") or name.startswith("O"):
        nickname = "DJ Disco Dancey " + name
    elif name.startswith("H") or name.startswith("I") or name.startswith("J") or name.startswith("K"):
        nickname = "DJ Funky " + name
    elif name.startswith("P") or name.startswith("Q") or name.startswith("R") or name.startswith("S"):
        nickname = "DJ Boom Boom " + name
    elif name.startswith("W") or name.startswith("X") or name.startswith("Y") or name.startswith("Z"):
        nickname = "MC Sonic " + name

    return nickname

    
#Calling the program
def main():
    print("Hello, welcome to the Nickname Generator!")
    name = input("Please enter your name!")
    print("Hello," + " "+ name + "!")

    while(1==1):
        text = """
                Select the number corresponding to the mode you'd like
                1. General nickname
                2. Pet nickname 
                3. Spanish nickname
                4. Animal nickname
                5. DJ nickname 
        """
        print(text)
        response = int(input("Please enter a number between 1 and 5 to choose the mode"))

        if response == 1 : 
            nickName = guessNickName(name)
        elif response == 2:
            nickName = generatePetName(name)
        elif response == 3: 
            nickName = generateSpanishNickName(name)
        elif response == 4:
            nickName = generateAnimalNickName(name)
        elif response == 5:
            nickName = generateDJNickName(name)
        else: 
            print("Invalid number entered, please choose a number from 1-5.")

        print(nickName)


if __name__ == "__main__":
    main()




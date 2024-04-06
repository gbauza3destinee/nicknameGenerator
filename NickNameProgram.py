import random, string
#! python3
#  After writing in Method save project,


# Takes in a NickName 
def guessNickName():
    name = input("Enter your name, and I will give you a new nickname: \n")
    nickname = name[0:3]
    print("Your new nickname is " + nickname)
guessNickName()


# Takes in a Silly 

def generatePetName():
    name = input("Enter your name, and I will give you an endearing your nickname:\n")
    nickname = name[0:3]
    print("Your new nickname is " + nickname + nickname)



# Takes in a NickName and generates a Spanish style name abbreviation

def generateSpanishNickName():
    name = input("Enter your name, and I will guess your Spanish nickname:\n")
    prefix = name[0:3]
    spanishNickName = nickname + "ito"

    
    if(prefix.endswith("e"|| "i")) : name[0:4])
    
    else :    
        spanishNickName = nickname + "ito"
        spanishNickName2= nickname + "ita"
    print("Your new Spanish nickname is " +spanishNickName) 



# Takes in a NickName and generates an name with alliteration
def generateAlliterationNickName():
    name = input("Enter your name, and I will guess your animal inspired nickname:\n")
    prefix = name[0:3]
   
    if(prefix[0] == "M") {
       return "Mambo" + prefix
    
   } elseif(prefix[0]=="A"){
       return "Apple" + prefix
   } elseif(prefix[0] == "E"){
       return "Elegant Elephant" + prefix
   } else{
       "return Saucy Stud" + prefix
   }


# Takes in a User's name and returns a DJ Nickname Alliteration  

def generateDJNickName():
    name = input("Enter your name, and I will guess your animal inspired nickname:\n")
    djBeginnerWords = HashMap;
    djBeginnerWords.put("B", "BoogeyDown");
    djBeginnerWords.put("L", "LargerThan");
    djBeginnerWords.put("S", "ShakinMyBoots");
    djBeginnerWords.put("U", "UwannaPieceAme")
    djBeginnerWords.put( "M", "MF")
    djBeginnerWords.put("T" "LITTY SMITTY")
    djBeginnerWords.put("D" "DISCOBALL")


## TODO Next- determine how to hand out a dj nickname based on first char of input name 

    djBeginnerWords.stream().collect(hashMap.toCollectorList())
    if (name[0] == djBeginnerWords.getKey()) : return djBeginnerWords.getValue();
        


    





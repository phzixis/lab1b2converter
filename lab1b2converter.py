import os

class Converter:
    def __init__(self):
        self.spellList = ["Stone Curse", "Lightning Bolt", "Thunder Storm", "Cold Bolt", "Frost Driver", "Fire Bolt", 
        "Fire Ball", "Fire Wall", "Sight", "Napalm Beat", "Soul Strike", "Safety Wall", "Increase SP Recovery"]
        self.spellDict = {"S1tone Curse":"Stone Curse", "Lightning Bolt": "Lightning Bolt", "Thunder Storm":"Thunder Storm", "Cold Bolt":"Cold Bolt", "Frost Driver":"Frost Driver", "Fire Bolt":"Fire Bolt", 
        "Fire Ball":"Fire Ball", "Fire Wall":"Fire Wall", "Sight":"Sight", "Napalm Beat":"Napalm Beat", "Soul Strike":"Soul Strike", "Safety Wall":"Safety Wall", "Increase SP Recovery":"Increase SP Recovery"}
        self.starter = "["
        self.content = "(%s, %s)"
        self.delimiter = ";"
        self.ender = "]"
        self.file = open(os.path.join(os.path.dirname(__file__),"input.txt"),"r").readlines()
        self.functionCall = "is_skill_build_valid %s"
        self.MainLoop()

    def MainLoop(self):
        while True:
            inp = input('''Select an option:
            1. Start
            2. Change Spell List Name
            3. Change Content
            4. Change Function Call
            5. Exit\n''')
            if inp == "1":
                outF = open(os.path.join(os.path.dirname(__file__),"output.txt"), "w")
                outF.write(self.Convert())
                outF.close()
                print("Output saved to output.txt")
            elif inp == "2":
                self.ChangeSpellList()
            elif inp == "3":
                self.ChangeContent()
            elif inp == "4":
                self.ChangeFunctionCall()
            elif inp == "5":
                print("Goodluck!!")
                break
            else:
                print("input not recognized")
                
    def Convert(self):
        string = ""
        q = 1
        i = 0

        while True:
            string += "let q"+str(q)+" = " + "let qlst" + str(q) + " = " + self.starter
            t = int(self.file[i])
            i += 1
            for j in range(t):
                words = self.file[i+j].split(" ")
                name = words[0]
                if len(words) == 3:
                    name += " " + words[1]
                num = int(words[len(words)-1])
                if j != 0:
                    string += "\t"
                string += self.PrintContent(name,str(num))
                if j != t-1:
                    string += self.delimiter + "\n"
            
            i += t
            string += self.ender + " in " + "\n" + self.functionCall % ("qlst"+str(q)) + "\n\n" 
            q+=1
            if i >= len(self.file):
                break
        return(string)
                
    def ChangeFunctionCall(self):
        num = 0
        count = 0
        while True:
            fc = input("Input your function call. The asterisk (*) is where we're going to put the input\nCurrent function call: " + self.functionCall % "[input name]" + "\n")
            for i in range(len(fc)):
                if fc[i] == "*":
                    if count == 0:
                        count = 1
                        num = i
                    else:
                        count = 0
                        break
            if count < 1:
                print("You don't have exactly one asterisk")
                continue
            else: 
                break
        self.functionCall = fc[:num] + "%s" + fc[num+1:]

    def ChangeSpellList(self):
        for i in range(len(self.spellList)):
            self.spellDict[self.spellList[i]] = input("Change name for " + self.spellList[i]+"\n")
    
    def ChangeMiddle(self):
        num1 = 0
        num2 = 0
        count = 0
        while True:
            middle = input("Input your content. There must be two asterisks (*) to put the skill type and amount in\n")
            for i in range(len(middle)):
                if middle[i] == "*":
                    if count == 0:
                        count = 1
                        num1 = i
                    elif count == 1:
                        count = 2
                        num2 = i
                    else:
                        count = 0
                        break
            if count < 2:
                print("you don't have two asterisks")
                continue
            else:
                break
        return middle[:num1] + "%s" + middle[num1+1:num2] + "%s" + middle[num2+1:]

    def PrintContent(self, name, num):
        return self.content % (self.spellDict[name], num)

    def PrintSample(self):
        return self.starter + self.content % (self.spellDict[self.spellList[0]], 10) + self.delimiter + \
self.content % (self.spellDict[self.spellList[1]], 5) + self.ender

    def ChangeContent(self):
        while True:
            print("1. Start: " + self.starter)
            print("2. Content: " + self.content % ("*", "*"))
            print("3. Delimiter: " + self.delimiter)
            print("4. End: " + self.ender)
            print("\nSample: " + self.PrintSample())
        
            inp = input("\n What to change? input (1-4), otherwise none\n")
            if inp == "1":
                self.starter = input("Changing start to: ")
            elif inp == "2":
                self.content = self.ChangeMiddle()
            elif inp == "3":
                self.delimiter = input("Changing delimiter to: ")
            elif inp == "4":
                self.ender = input("Changing end to: ")
            else:
                break

converter = Converter()
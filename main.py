print("|          |                                            ")
print("|    /\    |   ___  |    |        ___   ___  |\  /|  ___")
print("|   /  \   |  |__   |    |       |     |   | | \/ | |__")
print("|  /    \  |  |___  |___ |___    |___  |___| |    | |___")

print("_______  ____  ")
print("   |    |    |")
print("   |    |    |")
print("   |    |____| ")

print("         ____   ____")
print(" |  /   |    | |      ")
print(" | /    |____| |        ")
print(" | \    |    | |        ")
print(" |  \   |____| |_____   ")




questions = [
  ["what is the capital of Pakistan?", "a.karachi", "b.islamabad", "c.lahore", "d.peshawar", 2],

  ["who is the founder of pakistan ?" , "a.Alama Iqbal","b.Imran khan","c.Quaid e azam", "d.Nawaz sharif", 3 ],
  
  ["What’s the national flower of Japan?","a.Cherry blossom","b.Sun Flower","c.Rose" , "d.Tulip",1],
  
  ["How many days does it take for the Earth to orbit the Sun?","a.364","b.365","c.366","d.337",2],
  
  ["How many minutes are in full week? "," a.1080","b.1440","c.129090","d.10080",4],

  ["which is the largest country in the world?", "a.Russia", "b.China","c.pakistan", "d.USA",1],
  ["what is the capital of Pakistan?", "a.karachi", "b.islamabad", "c.lahore", "d.peshawar", 2],

  ["who is the founder of pakistan ?" , "a.Alama Iqbal","b.Imran khan","c.Quaid e azam", "d.Nawaz sharif", 3 ],
  
  ["What’s the national flower of Japan?","a.Cherry blossom","b.Sun Flower","c.Rose" , "d.Tulip",1],
  
  ["How many days does it take for the Earth to orbit the Sun?","a.364","b.365","c.366","d.337",2],
  
  ["How many minutes are in full week? "," a.1080","b.1440","c.129090","d.10080",4],

  ["which is the largest country in the world?", "a.Russia", "b.China","c.pakistan", "d.USA",1],
  ["what is the capital of Pakistan?", "a.karachi", "b.islamabad", "c.lahore", "d.peshawar", 2],

  ["who is the founder of pakistan ?" , "a.Alama Iqbal","b.Imran khan","c.Quaid e azam", "d.Nawaz sharif", 3 ],
  
  ["What’s the national flower of Japan?","a.Cherry blossom","b.Sun Flower","c.Rose" , "d.Tulip",1],
  
  ["How many days does it take for the Earth to orbit the Sun?","a.364","b.365","c.366","d.337",2],
  
  ["How many minutes are in full week? "," a.1080","b.1440","c.129090","d.10080",4],

  ["which is the largest country in the world?", "a.Russia", "b.China","c.pakistan", "d.USA",1],
  ["what is the capital of Pakistan?", "a.karachi", "b.islamabad", "c.lahore", "d.peshawar", 2],

  ["who is the founder of pakistan ?" , "a.Alama Iqbal","b.Imran khan","c.Quaid e azam", "d.Nawaz sharif", 3 ],
  
  ["What’s the national flower of Japan?","a.Cherry blossom","b.Sun Flower","c.Rose" , "d.Tulip",1],
  
 
  
  
] 

# questions complete

# lets make levels
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,20000000,30000000,40000000,50000000,60000000,70000000]


money = 0


for i in range(0,len(questions)):
  q = questions[i]
  print(f"\n\n Question for rupees Rs {levels[i]}")
  
  print(f"\n {q[0]}")
  print(f"{q[1]}         {q[2]}")
  print(f"{q[3]}        {q[4]}")

  reply = int(input("enter the answer by using keyboard keys (1-4) :  "))
  if reply == q[-1]:
    print(f"correct answer you have won Rs {levels[i]}")
    if i == 4:
      money = 10000

    elif i == 9:
      money = 320000
      
    elif i == 14:
      money = 10000000
      
    elif i == 20:
      money = 10000000
      

  else :
    print ("Wrong answer")
    


    print(f" Your take  money is {money} ")
    break


print("the game is finished")
    
  




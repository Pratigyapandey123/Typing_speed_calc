from time import *
import random as r

def mistake(partest,usertest):
     error = 0
     for i in range(len(partest)):
          try:
               if partest[i] != usertest[i]:
                    error = error+1
          except:
               error = error+1
     return error

def speed_time(time_s,time_e,userinput):
     time_delay = time_e - time_s
     time_R = round(time_delay,2)
     speed = len(userinput) / time_R
     return round(speed)
     
if __name__ == '__main__':
    while True:
        ck = input("Ready for test : yes/no ::")
        if ck =="yes":
            test = ["In today's fast-paced digital world, efficient typing skills are essential for productivity. Whether you're typing up reports, sending emails, or chatting with friends, the ability to type quickly and accurately can save you valuable time.",
                    "The quick brown fox jumps over the lazy dog.",
                    "Touch typing, where you type without looking at the keyboard, is a skill that can significantly enhance your typing speed."]
            test1 = r.choice(test)
            print("-------Typing Speed Calculation-------")
            print(test1)
            print()
            print()
            time_1 = time()
            test_input = input("Start Typing: ")
            time_2 = time()

            print('Speed:',speed_time(time_1,time_2,test_input), "words/sec")
            print('Error:',mistake(test1,test_input))

        elif ck == "no":
            print("Thank you")
            break
        
        else:
            print("wrong input")



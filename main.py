from function.names import getName, getMail
from function.telegram import sendMessage
from function.parser import parser, getValue
from function import debug
import time



def main():
    #print("===============================================")
    
    #sendMessage(getName(), getMail(), parser(10))

    #print("===============================================")
    #print(getValue())

    min = int(debug.getLine())
    max = int(getValue())

    debug.message(f"Начинаю отправку со строки: {min}")
    print("===============================================")

    i = min
    while i < max:
        result = sendMessage(getMail(), getName(), parser(i))
        if(result == "инет"):
            i = i
            time.sleep(60)
        else:
            i += 1
            time.sleep(10)

        print("===============================================")


        

if __name__ == "__main__":
    main()
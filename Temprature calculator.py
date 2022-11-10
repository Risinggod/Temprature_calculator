juser_input=input("ride down a temprature in c")
cast=float(juser_input)
#funktionen
def f():
    return (cast * 9 / 5) + 32

def k():
    return cast + 273.15
#schleife
while True:
    question = input("what do you whana know f or k")
    f()
    k()
    if question=="f":
        print(f())
        break
    elif question=="k":
        print(k())
        break
    else:
        print("rong anser try agen")
        continue

inpout_safe=open("Temp.txt", "a")
inpout_safe.write("Fahrenheit:" + str(f()) + "\n")
inpout_safe.write("kelvin:" + str(k()) + "\n")
inpout_safe.write("user_input:" + question + "\n")
inpout_safe.write("========================" + "\n")

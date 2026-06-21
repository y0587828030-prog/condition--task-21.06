stap 1
geiven_age = int(input("what is your age? "))
if geiven_age > 17:
    print("can enter")
else:
    print("cannot enter")

#stap 2
temperature = 38.2
if temperature > 37.5:
    print("High temperature")
else:
    print("High temperature")

#stap 3
geiven_namber = int(input("geiven namber "))
if geiven_namber % 2 == 0:
    print("even number")
else:
    print("odd number")

stap 4
define_battery = 15
is_charging = True
if define_battery < 20 and is_charging == True:
    print("low battery, charging now")
if define_battery < 20 and is_charging != True:
    print("low battery, connect charger")
else:
    print("battery OK")

#stap 5
given_password = (input("given_passwor"))
password = "python123"
if given_password == password:
    print("access approved ")
else:
    print("access danied ")

stap 7
given_namber_1 = (input("given tow namber 1 "))
given_namber_2 = (input("given tow namber 2 "))
if given_namber_1 > given_namber_2:
    print("first is bigger")
if given_namber_2 > given_namber_1:
    print("second is bigger")
if given_namber_1 == given_namber_2:
    print("equal")

#stap 8
define = 40
distance = 30

if define - distance > 9:
    print("Enough fuel with reserve")
elif define - distance > 0:
    print("Enough fuel, low reserve")
else:
    print("Not enough fuel")

#stap 9
given_username = input("Please fill in your name. ")
print("hello",given_username)
username = "yehosh"
if given_username == username:
    print("usernme")

else:
    print("guest user ")

#stap 10
time = int(input("Enter the time "))
if time> 23 or time <1:
    print("lnvalid hour")
if time < 12:
    print("morning")
if time < 18:
    print("aftenoon")
else:
    print("evening")










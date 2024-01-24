#1 Juku laheb kinno

name = input("Mis on su nimi? ")
if name.upper()=="JUKU":
	print("Laheme kinno")
	age=int(input("Kui vana sa oled? "))
	if age<0 or age>120:
		answer="viga vastusega"
	elif age<6:
		answer="tasuta pilet"
	elif age<14:
		answer="lastepilet"
	elif age<65:
		answer="taispilet"
	elif age<120:
		answer="sooduspilet"
	print("On vaja Jukule osta", answer)
else:
	print("Joonistame")

#2 Pinginaabrid

n1 = input("Esimene nimi: ")
n2 = input("Teine nimi: ")
if n1.upper()=="A" and n2.upper()=="B" or n1.upper()=="B" and n2.upper()=="A":
	print("Pinginaabrid")
else:
	print("Nad ei ole naabrid")
if n1.upper() in ["A","B"] and n2.upper() in ["A","B"]:
	print("Pinginaabrid")
else:
	print("Nad ei ole naabrid")

#3 Remont

wall1 = float(input("Esimese seina pikkus: "))
wall2 = float(input("Teise seina pikkus: "))
S = wall1 * wall2
print("Pindala ruutmeetrites on: ", S)
answer = input("Soovite teha remonti? ")
if answer.lower()=="jah":
	price = float(input("Palju maksab ruutmeeter? "))
	summa = price * S
	print("Ruutmeetri hind: ", summa)

#4 Allahindus

price = float(input("Hind: "))
if price>700:
	price*=0.7
print("Uus hind: ", price)

#5 Temperatuur

temperature = float(input("Kirjutage toa temperatuur: "))

if  temperature > 18:
    print("Temperatuur on rohkem kui 18 kraadi.")
else:
    print("Temperatuur on alla 18 kraadi.")

#6 Pikkus

height = float(input("Kirjutage oma pikkus: "))

if height < 160:
    print("Sa oled luhike.")
elif height >= 160 and height <= 180:
    print("Sa oled keskmine.")
else:
    print("Sa oled pikk.")

#7 Pikkus ja sugu

height = float(input("Pikkus: "))
sex = input("Sugu (M/F): ")

if sex == "M":
    if height < 160:
        print("Sa oled luhike.")
    elif height >= 160 and height <= 180:
        print("Sa oled keskmine.")
    else:
        print("Sa oled pikk.")
elif sex == "F":
    if height < 150:
        print("Sa oled luhike.")
    elif height >= 150 and height <= 170:
        print("Sa oled keskmine.")
    else:
        print("Sa oled pikk.")
else:
    print("Viga sugu valimisel.")

#8 Poes

milk_price = 2.99
bread_price = 1.99
eggs_price = 0.99

milk_qty = int(input("Palju pakke piima tahad osta? "))
bread_qty = int(input("Palju pakke leiba tahad osta? "))
eggs_qty = int(input("Palju pakke mune tahad osta? "))

milk_cost = milk_price * milk_qty
bread_cost = bread_price * bread_qty
eggs_cost = eggs_price * eggs_qty

kokku = milk_cost + bread_cost + eggs_cost

print("Summa kokku on", round(kokku, 2))

#9 Ruut

side1 = float(input("Sisesta pikkus 1: "))
side2 = float(input("Sisesta pikkus 2: "))
side3 = float(input("Sisesta pikkus 3: "))
side4 = float(input("Sisesta pikkus 4: "))

if side1 == side2 == side3 == side4:
    print("See on ruut.")
else:
    print("See ei ole ruut.")

#10 Matemaatika

num1 = float(input("Esimene number: "))
num2 = float(input("Teine number: "))

operation = input("Valige tehe (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Viga"

print("Tulemus on", result)

#11 Juubel

birthday = int(input("Kirjuta oma sunnipaev: "))

if birthday % 10 == 0:
    print("See on juubel!")
else:
    print("See ei ole juubel!")

#12 Müük

price = float(input("Kirjuta toote hind €: "))

if price <= 10:  
    discount = price * 0.10
else:
    discount = price * 0.20

final_price = price - discount
print("Lopphind on", final_price, "€")

#13 Jalgpalli meeskond

sugu = input("Mis on kandidaadi sugu (mees/naine): ")

if sugu == "mees":
    age = int(input("Kui vana ta on: "))
    if age >= 16 and age <= 18:
        print("Ta sobib tiimi.")
    else:
        print("Ta ei sobi tiimi.")
elif sugu == "naine":
    print("Ta ei sobi tiimi.")
else:
    print("Viga!")

#14 Busside logistika

passagners = int(input("Palju inimesi on: "))
seats = int(input("Palju mahub bussi: "))

buses = passagners // seats
remaining_people = passagners % seats

if remaining_people > 0:
    buses += 1

print("Vaja laheb busse:", buses)
print("Inimesi viimases bussis:", remaining_people)

import random

#Για σκακιέρα 8x8

pointswhite=0
pointsblack=0
board8x8=[1,2,3,4,5,6,7,8]

for i in range(100):

    p1=random.choice(board8x8)
    p2=random.choice(board8x8)
    a1=random.choice(board8x8)
    a2=random.choice(board8x8)

    print("Γύρος: ", i+1)
    print("")

    while ((p1==a1) and (p2==a2)):
        p1=random.choice(board)
        p2=random.choice(board)
        a1=random.choice(board)
        a2=random.choice(board)

    if (p1==a1 or p2==a2):
        pointswhite=pointswhite+1
        print("O λευκός πύργος έφαγε τον μάυρο αξιωματικό")
    elif ((a1-p1)==(a2-p2) or (a1-p1)==(p2-a2) or (p1-a1)==(a2-p2) or (p1-a1)==(p2-a2)):
        pointsblack=pointsblack+1
        print("Ο μαύρος αξιωματικός έφαγε τον λευκό πύργο")
    else:
        print("Ισοπαλία")

print("Ο παίχτης με τα λεφκά συγκέντρωσε:",pointswhite,"πόντους")
print("Ο παίχτης με τα μαύρα συγκέντρωσε:",pointsblack,"πόντους")
print("")

#Για σκακιέρα 7x7

board7x7=[1,2,3,4,5,6,7]
pointsblack=0  #Μηδενισμός μεταβλητών
pointswhite=0

for i in range(100):

    p1=random.choice(board7x7)
    p2=random.choice(board7x7)
    a1=random.choice(board7x7)
    a2=random.choice(board7x7)

    print("Γύρος: ", i+1)
    print("")

    while ((p1==a1) and (p2==a2)):
        p1=random.choice(board7x7)
        p2=random.choice(board7x7)
        a1=random.choice(board7x7)
        a2=random.choice(board7x7)

    if (p1==a1 or p2==a2):
        pointswhite=pointswhite+1
        print("O λευκός πύργος έφαγε τον μάυρο αξιωματικό")
    elif ((a1-p1)==(a2-p2) or (a1-p1)==(p2-a2) or (p1-a1)==(a2-p2) or (p1-a1)==(p2-a2)):
        pointsblack=pointsblack+1
        print("Ο μαύρος αξιωματικός έφαγε τον λευκό πύργο")
    else:
        print("Ισοπαλία")

print("Ο παίχτης με τα λεφκά συγκέντρωσε:",pointswhite,"πόντους")
print("Ο παίχτης με τα μαύρα συγκέντρωσε:",pointsblack,"πόντους")
print("")

#Για σκακιέρα 7x8

board7=[1,2,3,4,5,6,7]
board8=[1,2,3,4,5,6,7,8]
pointsblack=0 #Μηδενισμός μεταβλητών
pointswhite=0

for i in range(100):

    p1=random.choice(board7)
    p2=random.choice(board8)
    a1=random.choice(board7)
    a2=random.choice(board8)

    print("Γύρος: ", i+1)
    print("")

    while ((p1==a1) and (p2==a2)):
        p1=random.choice(board7)
        p2=random.choice(board8)
        a1=random.choice(board7)
        a2=random.choice(board8)

    if (p1==a1 or p2==a2):
        pointswhite=pointswhite+1
        print("O λευκός πύργος έφαγε τον μάυρο αξιωματικό")
    elif ((a1-p1)==(a2-p2) or (a1-p1)==(p2-a2) or (p1-a1)==(a2-p2) or (p1-a1)==(p2-a2)):
        pointsblack=pointsblack+1
        print("Ο μαύρος αξιωματικός έφαγε τον λευκό πύργο")
    else:
        print("Ισοπαλία")

print('Ο παίχτης με τα λεφκά συγκέντρωσε:',pointswhite,"πόντους")
print('Ο παίχτης με τα μαύρα συγκέντρωσε:',pointsblack,"πόντους")

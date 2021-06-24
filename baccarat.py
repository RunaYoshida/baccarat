import random
cards = [["A",1], [2,2], [3,3],  [4,4],  [5,5],  [6,6], [7,7], [8,8], [9,9], [10,0], ["J",0], ["Q",0], ["K",0]]

m = 1000

while m > 0:

    print("")
    print("どちらに賭けますか？")
    print("BANKER or PLAYER or TIE")
    print("Odds : BANKER 0.95, PLAYER 1.00, TIE 8.00")
    print("BANNKER→0　PLAYER→1 TIE→2")

    n = int(input())

    print("")
    print("所持金$" + str(m))
    print("いくら賭けますか？")

    #Bettorの賭け金
    a = int(input())
    while a > m:
        print("所持金以上を賭けることはできません")
        print("所持金$" + str(m))
        print("いくら賭けますか？")
        a = int(input())

    print("")
    print("ゲーム開始！")

    b1 = random.randint(0,12)
    b2 = random.randint(0,12)
    p1 = random.randint(0,12)
    p2 = random.randint(0,12)

    #足す数
    b = [int(cards[b1][1]), int(cards[b2][1])]
    p = [int(cards[p1][1]), int(cards[p2][1])]

    ba = b[0] + b[1]
    pa = p[0] + p[1]
    
    print("B:   " + str(cards[b1][0]) + "  " + str(cards[b2][0]))
    print("P:   " + str(cards[p1][0]) + "  " + str(cards[p2][0]))

    input()

    if ba%10 >= 8 or pa%10 >= 8:
        print("「ナチュラル」")

    elif pa%10 >= 6:
        if ba%10 < 6:
            b3 = random.randint(0,12)
            print("B:   " + str(cards[b1][0]) + "  " + str(cards[b2][0]) + "  " + str(cards[b3][0]))
            print("P:   " + str(cards[p1][0]) + "  " + str(cards[p2][0]))
            input()
            ba += int(cards[b3][1])

    else:
        p3 = random.randint(0,12)
        print("B:   " + str(cards[b1][0]) + "  " + str(cards[b2][0]))
        print("P:   " + str(cards[p1][0]) + "  " + str(cards[p2][0]) + "  " + str(cards[p3][0]))
        input()
        pa += int(cards[p3][1])
        if pa%10 == 8:
            if ba%10 < 3:
                b3 = random.randint(0,12)
                print("B:   " + str(cards[b1][0]) + "  " + str(cards[b2][0]) + "  " + str(cards[b3][0]))
                print("P:   " + str(cards[p1][0]) + "  " + str(cards[p2][0]) + "  " + str(cards[p3][0]))
                input()
                ba += int(cards[b3][1])
        elif pa%10 <= 1 or pa%10 ==9:
            if ba%10 < 4:
                b3 = random.randint(0,12)
                print("B:   " + str(cards[b1][0]) + "  " + str(cards[b2][0]) + "  " + str(cards[b3][0]))
                print("P:   " + str(cards[p1][0]) + "  " + str(cards[p2][0]) + "  " + str(cards[p3][0]))
                input()
                ba += int(cards[b3][1])
        elif pa%10 <=3:
            if ba%10 < 5:
                b3 = random.randint(0,12)
                print("B:   " + str(cards[b1][0]) + "  " + str(cards[b2][0]) + "  " + str(cards[b3][0]))
                print("P:   " + str(cards[p1][0]) + "  " + str(cards[p2][0]) + "  " + str(cards[p3][0]))
                input()
                ba += int(cards[b3][1])
        elif pa%10 <= 5:
            if ba%10 < 6:
                b3 = random.randint(0,12)
                print("B:   " + str(cards[b1][0]) + "  " + str(cards[b2][0]) + "  " + str(cards[b3][0]))
                print("P:   " + str(cards[p1][0]) + "  " + str(cards[p2][0]) + "  " + str(cards[p3][0]))
                input()
                ba += int(cards[b3][1])
        elif pa%10 <= 7:
            if ba%10 < 7:
                b3 = random.randint(0,12)
                print("B:   " + str(cards[b1][0]) + "  " + str(cards[b2][0]) + "  " + str(cards[b3][0]))
                print("P:   " + str(cards[p1][0]) + "  " + str(cards[p2][0]) + "  " + str(cards[p3][0]))
                input()
                ba += int(cards[b3][1])

    if ba%10 > pa%10:
        print("BANKERの勝ち")
        if n == 0:
            m += a*0.95
        else:
                m -= a
    elif ba%10 == pa%10:
        print("「タイ」")
        if n == 0 or n == 1:
            continue
        else:
            m += a*8
    elif ba%10 < pa%10:
        print("PLAYERの勝ち")
        if n == 0 or n == 2:
            m -= a
        else:
            m += a

    if m == 0:
        break
    
    print("")
    print("$" + str(m))
    print("ゲームを続けますか？")
    print("YES→0 NO→1")
    if int(input()) == 1:
        break
    print("")
    
print("")
print("ゲーム終了")
print("$" + str(int(m)))
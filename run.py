from pygem import screen as gemscreen

gs1 = gemscreen.GemScreen()
gs2 = gemscreen.GemScreen()

if gs1 == gs2:
    print ("Yay")
else:
    print("Problem")

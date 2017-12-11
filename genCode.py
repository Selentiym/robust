
stats = ("mean","hodges","pirson")
damages = ("quadrDamage","absoluteDamage","strangeDamage")
for stat in stats:
    print("stat = "+stat + "(sample)")
    for damage in damages:
        print("rez[\""+stat+"\"][\""+damage+"\"].append("+damage+"(2,stat))")

l = [0 for x in range(0,4)]
print(l)

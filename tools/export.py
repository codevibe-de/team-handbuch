import os, sys, re, json
import datetime

# export tag statistics
data = {}
T = {}
cnt = 0

def doit(p):
    global cnt
    for f in os.listdir(p):
        if f.endswith(".md"):
            try:
                txt = open(p + "/" + f, encoding="utf-8").read()
                if txt.startswith("---"):
                    fm = txt.split("---")[1]
                    for l in fm.split("\n"):
                        if l.startswith("tags:"):
                            x = l[5:].strip()
                            x = x.replace("[", "").replace("]", "")
                            for t in x.split(","):
                                t = t.strip()
                                if t != "":
                                    if t in data:
                                        data[t] = data[t] + 1
                                    else:
                                        data[t] = 1
                        if l.startswith("typ:"):
                            y = l[4:].strip()
                            if y in T:
                                T[y] = T[y] + 1
                            else:
                                T[y] = 1
                    cnt = cnt + 1
            except:
                pass

doit("notes")

if len(sys.argv) > 1 and sys.argv[1] == "csv":
    print("tag;count")
    for k in sorted(data, key=lambda k: -data[k]):
        print(k + ";" + str(data[k]))
    print("")
    print("typ;count")
    for k in sorted(T, key=lambda k: -T[k]):
        print(k + ";" + str(T[k]))
else:
    print("| Tag | Anzahl | Anteil |")
    print("|---|---|---|")
    for k in sorted(data, key=lambda k: -data[k]):
        print("| " + k + " | " + str(data[k]) + " | " + str(round(data[k] / cnt * 100, 1)) + " % |")
    print("")
    print("| Typ | Anzahl | Anteil |")
    print("|---|---|---|")
    for k in sorted(T, key=lambda k: -T[k]):
        print("| " + k + " | " + str(T[k]) + " | " + str(round(T[k] / cnt * 100, 1)) + " % |")
    print("")
    print("Notizen: " + str(cnt))

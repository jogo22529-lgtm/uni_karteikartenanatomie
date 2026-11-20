# Baut index.html aus index.src.html + cards.txt
src=open("index.src.html",encoding="utf-8").read()
cards=open("cards.txt",encoding="utf-8").read().strip().replace("\\","\\\\").replace("`","\\`")
open("index.html","w",encoding="utf-8").write(src.replace("/*CARDS*/",cards))

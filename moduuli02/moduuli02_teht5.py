leiviskat = input("Anna leiviskät.\n")
print("")
naulat = input("Anna naulat.\n")
print("")
luodit = input ("Anna luodit.\n")
print("")

kokonaispaino = float(leiviskat)*20*32*13.3 + float(naulat)*32*13.3 + float(luodit)*13.3

print(f"\nMassa nykymittojen mukaan:\n{int(kokonaispaino/1000)} kilogrammaa ja {kokonaispaino - int(kokonaispaino/1000)*1000:.2f} grammaa.")
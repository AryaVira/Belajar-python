def calculator (a,b,operation):
    if(operation == "Tambah"):
        return a + b

def calculatora (a,b,operation):
    if(operation == "kurang"):
        return a - b

def calculators (a,b,operation):
    if(operation == "kali"):
        return a * b

def calculatorz (a,b,operation):
    if(operation == "bagi"):
        return a % b

print(calculator(1,2, "Tambah"))
print(calculatora(10,3, "kurang"))
print(calculators(1100,2, "kali"))
print(calculatorz(2000,2, "bagi"))
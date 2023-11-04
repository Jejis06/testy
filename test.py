import os

# 1- bud
# 2- bud
# 3- test

print("""
maksymalne przedzily testow dla danego zestawu: 

1 : 1-600 ----------

  1-100 podzadanie 1 (m = 1)
  101-200 podzadanie 2 (n <= 30)
  201-300 podzadanie 3 (n <= 300)
  301-600 podzadanie 4 (n <= 1500)

2 : 1-85 ------------
3 : 1-999 -----------


                      !! UWAGA !!
w zestawie testow 1 pole zajete jest oznaczone znakiem `#` w odroznieniu
do zadania gdzie takie pole oznaczane jest literka `X`

      """)

testcases = int(input("ktory zestaw testow(1, 2, 3): "))
progname = input("nazwa programu ktory chcesz przetestowac : ")

PATH = f"testcase{testcases}" 
if testcases == 1 or testcases == 2:
    TNAME = 'bud'
else: TNAME = 'test'
mode = (input("przedzial testow podzadan w formacie `1-n`:")).split('-')

s = int(mode[0])
e = int(mode[1]) + 1

pth = os.path.join(os.getcwd(), PATH)
for i in range(s, e):
    arg = f'< {os.path.join(pth,os.path.join("in",TNAME + str(i) + ".in"))}'
    out = os.popen(f'./{progname} {arg}').read().replace(' ',"").replace('\t',"").replace("\n","")
    with open(os.path.join(pth,os.path.join("out",TNAME + str(i) + ".out")), 'r') as f:
        expected = f.read().replace(' ',"").replace('\t',"").replace("\n","")
        f.close()

    if out != expected:
        print(f"Error : {i} | expected: {expected} / got: {out}")
        break
    print(f"OK {i}")




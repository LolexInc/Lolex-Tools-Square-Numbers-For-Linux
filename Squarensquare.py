import sys,os,subprocess,io,time
sys.path.insert(0,"/home/")
print("Welcome to Lolex Square Numbers For Android v1.1 CODENAME:because_life_can_get_hard_at_times update.")
try:
    import squarenumber
except(ImportError):
    with open ("/home/squarenumber.py","a") as f: f.write("squarenumbers = 2\noriginsquare = 2")
import squarenumber
squarenumbers = squarenumber.squarenumbers
originsquare = squarenumber.originsquare
gone = 0
gonecon = 0
squarecont = int(input("Do you wish to input a number to continue every 1000 square numbers to continue. Please enter 1 if you do."))
while True:
    squarenumbers = originsquare*originsquare
    originsquare = originsquare + 1
    print(squarenumbers)
    gone = gone + 1
    if gone == 1000 or gone>1000:
        try:
            os.remove("/home/squarenumber.py")
        except(FileNotFoundError):
           pass
        with open ("/home/squarenumber.py","a") as f: f.write("\nsquarenumbers = ")
        with open ("/home/squarenumber.py","a") as outf: outf.write(str(squarenumbers))
        with open ("/home/squarenumber.py","a") as f: f.write("\noriginsquare = ")
        with open ("/home/squarenumber.py","a") as outf: outf.write(str(originsquare))
        gone = 0
        gonecon = gonecon + 1000
        if gonecon == 100000:
            continuer = int(input("Do you wish to continue? Please enter 0 if you DON'T."))
            if continuer == 0:
                exit()


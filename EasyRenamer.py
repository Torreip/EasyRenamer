import os
import sys
import time

#MassRenameFunction
def main():
    folder = ""
    while folder == "":
        folder = str(input("Enter the complete path of your desired folder ? (It can't be left blank) "))
        name = str(input("What should it be renamed to ? "))
    #MainLoop
    for count, filename in enumerate(os.listdir(folder)):
        current = f"{str(folder)}{str(filename)}"
        fname , fext = os.path.splitext(f"{str(current)}")
        dst = f"{str(name)}{str(count)}{str(fext)}"
        src =f"{folder}/{filename}"
        dst =f"{folder}/{dst}"
         
        os.rename(src, dst)
    print(f"Every file in '{str(folder)}' has been renamed.")
    c1 = input("Make your choice (Y or n) ")
    c1 = c1.lower()

    if c1 == "y" or c1 == "ye" or c1 == "yes":
        main()
    else:
        print("\33[94mThank's for using my program ! \nSigned Torreip 2022")
        time.sleep(2)
        sys.exit()

 
if __name__ == '__main__':
    main()
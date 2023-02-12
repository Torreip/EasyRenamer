import os, sys, time

def readSettings():
    try:
        with open("config.cfg", "r") as f:
            lines = f.readlines()
            if lines == []:
                raise FileNotFoundError
            for i in lines:
                if i.startswith("log"):
                    if (i.rstrip().strip().split("=")[1].upper()) == "FALSE":
                        log = False
                    else:
                        log = True
                if i.startswith("_path"):
                    log_path = i.rstrip().strip().split("=")[1]
                if i.startswith("_mode"):
                    log_mode = i.rstrip().strip().split("=")[1]
            print("Settigs for this session : ")
            print(log, "||", log_path, "||" ,log_mode)
            return log, log_path, log_mode
            
    except FileNotFoundError:
        with open("config.cfg", "w") as f:
            f.write("log=False\n")
            f.write("_path=EasyRenamer.log\n")
            f.write("_mode=append\n")
        return readSettings()

    except ValueError:
        with open("config.cfg", "w") as f:
            f.write("log=False\n")
            f.write("_path=EasyRenamer.log\n")
            f.write("_mode=append\n")
        return readSettings()

#ContinueFuntion
def choice(log, log_path, log_mode):
    print("Do you want to rename other files ? ")
    c1 = input("Make your choice (Y or n) ").lower()

    if c1 == "y" or c1 == "ye" or c1 == "yes":
        main(log, log_path, log_mode)
    else:
        print("\33[94mThank's for using my program (V1.3) ! \nSigned Torreip 2023\u001b[0m")
        time.sleep(2)
        sys.exit(0)

#EasyRenamerMainFunction
def main(log, log_path, log_mode):
    logRaw = []
    folder = ""
    while folder == "":
        folder = str(input("Enter the complete path of your desired folder ? (It can't be left blank) "))
        name = str(input("What should it be renamed to ? "))
    #MainLoop
    max = len(str(len(os.listdir(folder))))-1
    treshold = int("1" + "0" * max)-1
    try:
        for count, filename in enumerate(os.listdir(folder)):
            if count < treshold:
                leadingZeros = "0" * (max+1 - len(str(count)))
                number = f"{leadingZeros}{str(count+1)}"
            else:
                number = f"{str(count+1)}"
            current = f"{str(folder)}{str(filename)}"
            fname , fext = os.path.splitext(f"{str(current)}")
            dst = f"{str(name)}{str(number)}{str(fext)}"
            src =f"{folder}/{filename}"
            dst =f"{folder}/{dst}"
            ex = 0
            if log == True:
                logRaw.append(f"{str(src)} -> {str(dst)}\n")
            try:
                os.rename(src, dst)
            except FileExistsError:
                ex = ex + 1
                pass
        if ex == 0:
            print(f"Every file in '{str(folder)}' has been renamed.")
        else:
            print(f"Every file in '{str(folder)}' has been renamed.")
            print(f"{str(count+2 - ex)} files already beared their new name.")
        if log == True:
            import datetime
            if log_mode == "append":
                with open(f"{str(log_path)}", "a") as f:
                    f.write(f"\n\n --- Log for folder '{str(folder)}' LOG GENERATED ON {datetime.datetime.now()}  \n")
                    f.writelines(logRaw)
            else:
                with open(f"{str(log_path)}", "w") as f:
                    f.write(f"\n\n --- Log for folder '{str(folder)}' LOG GENERATED ON {datetime.datetime.now()}  \n")
                    f.writelines(logRaw)
        choice(log, log_path, log_mode)
    except (FileNotFoundError, NotADirectoryError, PermissionError, OSError):
        print("An error occured, please try again.")
        main(log, log_path, log_mode)
 
if __name__ == '__main__':
    log, log_path, log_mode = readSettings()
    main(log, log_path, log_mode)
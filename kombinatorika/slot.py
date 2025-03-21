# Materi kombinatorika untuk filling slot atau peluang mengisi suatu slot
# https://www.youtube.com/watch?v=ZmKG7KDu_5g < sumber
# Jika ada kata "atau" = ditambah, seperti 1 pria atau 1 wanita, jumlah pria = 65, wanita = 15 => 80
# Jika ada kata "dan" = dikali, seperti 1 pria dan 1 wanita, (dari atas) => 65*15 = 975
#

def main():
    while True:
        print("OPTIONS \n")
        print("[1] Password Possible Combinations")
        options = input("~> ")

        if options == "1":
            print("What characters/how many characters in the combinations?")
            sChar = input("~> ")
            try:
                int(sChar)
            except:
                print("ERROR, not integer")
                break
            print("How long the password will be?")
            sLength = input("~> ")
            try:
                int(sChar)
            except:
                print("ERROR, not integer")
                break
            total = int(sChar)**int(sLength)
            print(f"total: {total}")
            break
        else:
            continue

main()
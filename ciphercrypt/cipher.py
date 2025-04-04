# Encryptor Decryptor Enkripsi Cipher Text

alphanum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" * 2
anumLength = 72

def typeerr(type):
    print(f"[ERR!] the input has to be {type}, user entered other than {type}")

def main():
    #Start
    while True:
        print("Cipher Text Encryptor-Decryptor by nvll-zen")
        print("Please select the options below:")
        print("[1] Encryptor \n[2] Decryptor")
        optList = [1,2]
        option = input("> ")
        try:
            option = int(option)
        except:
            typeerr("Integer")
            break
        if option not in optList:
            print(option, type(option))
            print("[ERR!] user entered an option outside of the list provided")
            break

        # Encryptor
        if option == 1:
            rawText = input("Text to encrypt:")
            rawText = rawText.upper()

            key = input("Input key:")
            try:
                key = int(key)
            except:
                typeerr("Integer")

            outputText = []
            for char in rawText:
                if alphanum.find(char) == -1:
                    outputText.append(char)
                else:
                    try:
                        outputText.append(alphanum[(alphanum.find(char)+key) % 36])
                    except:
                        outputText.append("?")


            print(f"\nEncrypted Text: {"".join(outputText)}\n")
            break
        elif option == 2:
            rawText = input("Text to decrypt:")
            rawText = rawText.upper()

            key = input("Input key:")
            try:
                key = int(key)
            except:
                typeerr("Integer")

            outputText = []
            for char in rawText:

                if alphanum.find(char) == -1:
                    outputText.append(char)
                else:
                    try:
                        outputText.append(alphanum[(alphanum.find(char)-key) % 36])
                    except:
                        outputText.append("?")


            print(f"\nEncrypted Text: {"".join(outputText)}\n")
            break

main()
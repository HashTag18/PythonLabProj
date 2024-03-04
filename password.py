import random,os

def complexity():
            
        os.system('cls')
        length=int(input("Enter The length of desired Password :"))
        os.system('cls')
        print("Password Complexity : ? \n 1.Hard (Numerical and Character) \n 2. Very Hard (Numerical , special symbols and Character) \n ")
        choice=int(input())
        
        os.system('cls')
        
        if(choice == 1):
                hard(length)
        if(choice == 2):
                veryHard(length)
        else:
            print("Invalid choice.")
        


def hard(length):
        letters="zAyBxCwDvEuF0tGsH9rIqJ8pKoL7nMmN6lOkP5jQiR4hSgT3fUeV2dWcX1bYaZ"
        letter=''.join(random.choice(letters) for _ in range(length))
        print(letter)

def veryHard(length):
        letters="A1B2C3D4E5F6G7H8I9J0K`L!M@N#O$P.QaRb&cSdTeUfVgWhXiYjZklmnopqrstuvwxyz"
        letter=''.join(random.choice(letters) for _ in range(length))
        print(letter)
        
while(True): 
    complexity()
    another_try=input("Another Try : \n Yes ? or No ? ").lower()
    os.system('cls')
    if another_try != 'yes':
        break
def get_file():
        file = open("exam.txt","r")
        text = file.read()
        _list = text.split("\n")
        true_list = []
    
        for i in _list:
            true_list.append(i)   
        return true_list
        file.close()

def XXX_AAA(num):
     l_ist= get_file()
     for x,y in enumerate(l_ist):
         l_ist[x] = y.split("--")  
     for j in l_ist:
        if int(j[1]) > num:
           print("XXX  > then AAA in : ")
           print(f"{j[0]}--{j[1]}")
            
def main():
    while True:
        num = input("Enter AAA number: ")
        if num.isdigit():
            XXX_AAA(int(num))
            break
        else:
            print("Enter only numbers")
main() 
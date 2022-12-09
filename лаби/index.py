def get_file():
        file = open("exam.txt")
        text = file.read()
        _list = text.split("\n")
        true_list = []
    
        for i in _list:
            true_list.append(i)   
        file.close()
        
        return true_list


def XXX_AAA(num):
     l_ist=get_file()
     x=True
     
     for i in l_ist:
            adres = i.split(" -- "[1])
            for j in adres : 
                if j > num :
                    print(i)
                   
def main():
    num = input("Enter AAA number: ")
    XXX_AAA(num)
main()
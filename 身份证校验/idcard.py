import urllib.request
import sys

print('''
 _____   _       ___   _____   _____        ___   __   _  
|  _  \ | |     /   | /  _  \ |  _  \      /   | |  \ | | 
| |_| | | |    / /| | | | | | | |_| |     / /| | |   \| | 
|  ___/ | |   / / | | | | | | |  _  /    / / | | | |\   | 
| |     | |  / /  | | | |_| | | | \ \   / /  | | | | \  | 
|_|     |_| /_/   |_| \_____/ |_|  \_\ /_/   |_| |_|  \_|
''')





def get_idcard(idnumber):
    url = 'http://apis.haoservice.com/idcard/VerifyIdcard?cardNo='+idnumber+'&realName='+'%e7%9f%b3%e6%98%8c%e9%9b%84'+'&key=************'


    response = urllib.request.urlopen(url)

    response = response.read().decode('utf-8')

    return response
def get_idnumber():
    id1 = '45032219910110'       #  身份证前六位为地区  八位生日数字
    number = []
    idnumber1 =[]
    for i in range(100,1000):
        if i%2 != 0:       #奇数为男偶数为女
            number.append(i)

    for i in number:
        idnumber1.append(id1+str(i))
        #print(len(id1+str(i)))
    return idnumber1

def get_last(idnumber1):                #计算身份证最后一位
    idnumber = []
    for i in idnumber1:
        total = int(i[0])*7+int(i[1])*9+int(i[2])*10+int(i[3])*5+int(i[4])*8+int(i[5])*4+int(i[6])*2+int(i[7])+int(i[8])*6+int(i[9])*3+int(i[10])*7+int(i[11])*9+int(i[12])*10+int(i[13])*5+int(i[14])*8+int(i[15])*4+int(i[16])*2
        remainder = total%11
        if remainder == 0:
            idnumber.append(i+str(1))
        elif remainder == 1:
            idnumber.append(i+str(0))
        elif remainder == 2:
            idnumber.append(i+'x')
        elif remainder == 3:
            idnumber.append(i+str(9))
        elif remainder == 4:
            idnumber.append(i+str(8))
        elif remainder == 5:
            idnumber.append(i+str(7))
        elif remainder == 6:
            idnumber.append(i+str(6))
        elif remainder == 7:
            idnumber.append(i+str(5))
        elif remainder == 8:
            idnumber.append(i+str(4))
        elif remainder == 9:
            idnumber.append(i+str(3))
        elif remainder == 10:
            idnumber.append(i+str(2))
    return idnumber        #计算身份证列表


if __name__ == '__main__':
    idnumber1 = get_idnumber()
    idnumber = get_last(idnumber1)
    #print(idnumber)
    f = open('id.txt','w')
    for i in idnumber:
        a = str(i)+'\n'
        f.write(a)
    f.close()
#response = get_idcard(idnumber=i)


            
            
    
    
        
    

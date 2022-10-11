import pandas as pd
import random
from datetime import datetime as dt

data_frame = pd.read_csv('C:/Users/rtssl/PycharmProjects/reservoir/final.csv')

data_frame.drop(["Unnamed: 0"], axis=1)
con = 0
# data_frame = pd.DataFrame(columns= ["Date","Time","Shift","Ques","C_ans","G_ans","Selected","Rejected"])

while con < 1:

    a = random.randint(0,1000)
    b = random.randint(50,1000)
    sy = ["+","-"]
    Sy = random.choice(sy)
    if Sy == "+":
        c = a + b
    else:
        c = a - b
    ques = f"{a} {Sy} {b}"
    C = int(input(f"Enter the value {ques} = "))

    if C == c:
        select = 1
        reject = 0
    else:
        select = 0
        reject = 1

    now = dt.now()
    date = now.strftime("%d/%m/%y")
    c_time = now.strftime("%H:%M:%S")
    if (c_time >= "06:00:00") and (c_time <= "14:30:00") :
        shift = 1
    elif (c_time >= "14:30:00") and (c_time <= "22:30:00") :
        shift = 2
    else:
        shift = 3


    datas = pd.DataFrame({"Date":[date],"Time":[c_time],"Shift":[shift],"Ques":[ques],"C_ans":[c],"G_ans":[C],"Selected":[select],"Rejected":[reject]})
    data_frame = pd.concat([data_frame,datas],ignore_index=True)
    con += 1
print(data_frame)

data_frame.to_csv("final.csv")

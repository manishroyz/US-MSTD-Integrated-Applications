# generate random integer values
from random import seed
from random import randint
import matplotlib.pyplot as plt
# seed random number generator
seed(1)

data_rows = []
# generate some integers
for _ in range(5):
    data_row = []
    tof_s1 = randint(100, 110)
    tof_s2 = randint(150, 160)
    tof_s3 = randint(200, 210)
    tof_s4 = randint(250, 260)
    temp_s1 = randint(50, 100)
    temp_s2 = randint(300, 400)
    temp_s3 = randint(600, 700)
    temp_s4 = randint(900, 1000)
    tc_1 = randint(50, 70)
    tc_2 = randint(150, 180)
    tc_3 = randint(250, 280)
    tc_4 = randint(450, 480)
    tc_5 = randint(750, 780)
    tc_6 = randint(1050, 1080)


    data_row.append(tof_s1)
    data_row.append(tof_s2)
    data_row.append(tof_s3)
    data_row.append(tof_s4)
    data_row.append(temp_s1)
    data_row.append(temp_s2)
    data_row.append(temp_s3)
    data_row.append(temp_s4)
    data_row.append(tc_1)
    data_row.append(tc_2)
    data_row.append(tc_3)
    data_row.append(tc_4)
    data_row.append(tc_5)
    data_row.append(tc_6)
    data_rows.append(data_row)

header_names = ["collect_date", "tof_s1", "tof_s2", "tof_s3", "tof_s4", "temp_s1", "temp_s2", "temp_s3", "temp_s4",
                "tc1", "tc2", "tc3", "tc4", "tc5", "tc6"]

print('Generated data:')
for x in data_rows:
    print(x)

# Slicing 1st index(column) of all rows
print("Sliced data:")
data_sliced = [x[0] for x in data_rows]
print(data_sliced)
plt.plot(data_sliced)
plt.show()

# DB Insertions:
for data in data_rows:
    print(data)
    #Call class funtion here...that will insert into database
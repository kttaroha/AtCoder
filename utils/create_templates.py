# obtained from https://qiita.com/redmeteor777/items/f88c5481c6bb51300cc0

import os

for i in range(10):
    folder_name1 = "../src/ABC{:x<3}".format(i)
    os.makedirs(folder_name1, exist_ok=True)

    for j in range(10):
        folder_name2 = folder_name1 + "/ABC{}{}x".format(i, j)
        os.makedirs(folder_name2, exist_ok=True)

        for k in range(10):
            folder_name3 = folder_name2 + "/ABC{}{}{}".format(i, j, k)
            os.makedirs(folder_name3, exist_ok=True)
            file_name = folder_name3 + "/ABC{}{}{}".format(i, j, k)

            with open(file_name + "A.py", mode='w') as f:
                pass
            with open(file_name + "B.py", mode='w') as f:
                pass
            with open(file_name + "C.py", mode='w') as f:
                pass
            with open(file_name + "D.py", mode='w') as f:
                pass
            with open(file_name + "E.py", mode='w') as f:
                pass
            with open(file_name + "F.py", mode='w') as f:
                pass
            with open(folder_name3 + "/input.txt", mode='w') as f:
                pass


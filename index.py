main = []
searching = input("\nвведите нназвание обьекта")
with open("INN.csv", 'r', encoding="utf-8")as file:
    for line in file:
        arr = file.readlines()
        for i in range(0, len(arr)):
            res = []
            spl = arr[i].strip()
            delt = (spl.split(";"))
            #print(delt)
            num = delt[0].strip().replace("\ufeff", "")
            ind = delt[1].strip()
            num_2 = delt[2].strip()
            cntry = delt[3].strip()
            res.append(num)
            res.append(ind)
            res.append(num_2)
            res.append(cntry)
            if searching == res[2]:
                ind=res[0]












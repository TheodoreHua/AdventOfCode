def sum_check(target:int, values:list):
    compare_list = values[:]
    for i in values:
        for j in compare_list:
            if i + j == target:
                print("{0} + {1} = {2}\n{0} * {1} = {3}".format(i, j, i + j, i * j))
                return


with open("../input.txt", "r") as f:
    report = f.readlines()
    try:
        report = [int(r.strip()) for r in report]
    except ValueError:
        print("Invalid Value in Report")
        exit(1)

sum_check(2020, report)

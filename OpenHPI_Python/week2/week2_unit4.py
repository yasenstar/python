stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]

sell_list = []

for i in stocks:
    if float(i[2]) > 5:
        # print(i)
        # print(i[0])
        sell_list.append(str(i[0]))
        # print(sell_list)

for i in (sell_list):
    print(i)
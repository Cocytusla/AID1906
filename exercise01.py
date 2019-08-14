

#字典　起名字　逻辑意义
shang_pin_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

ding_dan = []


def shopping():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def buying():
    for key, value in shang_pin_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
    while True:
        cid = int(input("请输入商品编号："))
        if cid in shang_pin_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    ding_dan.append({"cid": cid, "count": count})
    print("添加到购物车。")


def settlement():
    total_price = 0
    for item in ding_dan:
        commodity = shang_pin_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))
        total_price += commodity["price"] * item["count"]
    while True:
        qian = float(input("总价%d元，请输入金额：" % total_price))
        if qian >= total_price:
            print("购买成功，找回：%d元。" % (qian - total_price))
            ding_dan.clear()
            break
        else:
            print("金额不足.")


shopping()

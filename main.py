# coding:utf-8
import random
import datetime
import origin


# 将重量大于背包容量的物品剔除
def delete_item(m, w, v):
    list_tuple = [(x, y) for x, y in zip(w, v) if x <= m]
    return [i[0] for i in list_tuple], [i[1] for i in list_tuple]


# 按照性价比将物品排序
def price_ratio(w, v):
    ratio = [float(y / x) for x, y in zip(w, v)]
    zipper = zip(ratio, w, v)
    list_tuple = sorted(zipper, key=lambda zipper: zipper[0], reverse=True)
    # print(list_tuple)
    return [i[1] for i in list_tuple], [i[2] for i in list_tuple]


if __name__ == "__main__":
    n = 10000  # 物品
    m = random.randint(0.5 * n, n)  # 容量
    random_w = range(1, 2 * n)
    w = random.sample(random_w, n)  # 物品重量
    random_v = range(1, 2 * n)
    v = random.sample(random_v, n)  # 物品价格
    begin = datetime.datetime.now()
    origin.sort(n, m, w, v)

    end = datetime.datetime.now()
    print('优化前时间:' + str(end - begin))

    begin = datetime.datetime.now()
    w, v = delete_item(n, w, v)
    n = len(w)
    w, v = price_ratio(w, v)
    origin.sort(n, m, w, v)
    end = datetime.datetime.now()
    print('优化后时间:' + str(end - begin))

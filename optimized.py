# coding:utf-8
def sort(n, m, w, v):
    matrix = [([0] * (m + 1)) for i in range(n + 1)]  # 建立二维数组 n+1行 m+1列

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matrix[i][j] = matrix[i - 1][j]  # 先将已经算出来的最优解赋值给新的一行
            for num in range(1, j // w[i - 1] + 1):
                if j >= w[i - 1] and matrix[i][j] < matrix[i - 1][j - num * w[i - 1]] + num * v[i - 1]:
                    matrix[i][j] = matrix[i - 1][j - num * w[i - 1]] + num * v[i - 1]
    return matrix

def price_ratio(w, v):
    ratio = [float(y / x) for x, y in zip(w, v)]
    print(ratio)
    li=zip(ratio, w, v)
    print(sorted(li, key = lambda li:li[0]))

def delete_item(m, w, v):
    list_tuple = [(x, y) for x, y in zip(w, v) if x <= m]
    return [i[0] for i in list_tuple], [i[1] for i in list_tuple]


def show(n, m, w, res):
    print("最大为" + str(res[n][m]))
    x = [False for i in range(n)]
    j = m
    for i in range(n, 0, -1):
        if res[i][j] != res[i - 1][j]:
            x[i - 1] += 1
            j -= w[i - 1]
    for i in range(n):
        if x[i]:
            print("第" + str(i + 1) + "个物品加入" + str(x[i]) + '次')
    print('')


if __name__ == "__main__":
    n = 5  # 物品
    m = 8  # 容量
    w = [1, 2, 3, 4, 5]  # 物品重量
    v = [1, 3, 5, 7, 111]  # 物品价格
    # w, v = delete_item(n, w, v)
    # n = len(w)
    # bag = sort(n, m, w, v)
    # for i in bag:
    #     print(str(i) + '\n')
    # show(n, m, w, bag)
    price_ratio(w,v)

    # 性价比排序
    # 删除比自己背包容量还要大的物品重量

    # random_w = range(1, 200)
    # w = random.sample(random_w, n)# 物品重量
    # random_v = range(1, 200)
    # v = random.sample(random_v, n)  # 物品价格


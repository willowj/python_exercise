# coding:utf8

def quick_sort(lis, mleft=None, mright=None):

    pl_ = mleft  = mleft if (mleft is not None) else 0
    pr_ = mright = mright if (mright is not None) else len(lis)-1
    # 不要用 mright = mright or len(),这样的写法
    # 这样传入 mright=0 _>mright =len() --- 导致无限递归
    if mleft>= mright:
        return lis

    while pl_ < pr_:
        while lis[mleft] <= lis[pr_] and pl_ < pr_:
            pr_ -= 1
        while lis[mleft] >= lis[pl_] and pl_ < pr_:
            pl_ += 1
        lis[pr_], lis[pl_] = lis[pl_], lis[pr_]

    lis[mleft], lis[pl_] = lis[pl_], lis[mleft]

    # pdb.set_trace()
    quick_sort(lis, mleft=mleft, mright=pl_-1)
    quick_sort(lis, mleft=pl_+1, mright=mright)
    return lis

print quick_sort([9, 7, 6, 8, 2, 3, 1, 0, 4, 5])
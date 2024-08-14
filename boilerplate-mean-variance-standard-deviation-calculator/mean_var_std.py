import numpy as np

def calculate(list):

    if len(list) == 9:

        Num = np.array([
            [list[0],list[1],list[2]],
            [list[3],list[4],list[5]],
            [list[6],list[7],list[8]],
        ])

        Mean = [[np.mean(Num[...,0]),np.mean(Num[...,1]),np.mean(Num[...,2])],[np.mean(Num[0,...]),np.mean(Num[1,...]),np.mean(Num[2,...])], np.mean(Num)]
        Var = [[np.var(Num[...,0]),np.var(Num[...,1]),np.var(Num[...,2])],[np.var(Num[0,...]),np.var(Num[1,...]),np.var(Num[2,...])], np.var(Num)]
        SD = [[np.std(Num[...,0]),np.std(Num[...,1]),np.std(Num[...,2])],[np.std(Num[0,...]),np.std(Num[1,...]),np.std(Num[2,...])], np.std(Num)]
        Max = [[np.max(Num[...,0]),np.max(Num[...,1]),np.max(Num[...,2])],[np.max(Num[0,...]),np.max(Num[1,...]),np.max(Num[2,...])], np.max(Num)]
        Min = [[np.min(Num[...,0]),np.min(Num[...,1]),np.min(Num[...,2])],[np.min(Num[0,...]),np.min(Num[1,...]),np.min(Num[2,...])], np.min(Num)]
        Sum = [[np.sum(Num[...,0]),np.sum(Num[...,1]),np.sum(Num[...,2])],[np.sum(Num[0,...]),np.sum(Num[1,...]),np.sum(Num[2,...])], np.sum(Num)]

        calculations = {
            'mean': Mean,
            'variance': Var,
            'standard deviation': SD,
            'max': Max,
            'min': Min,
            'sum': Sum
        }
    else:
        raise ValueError("List must contain nine numbers.")
        calculations = list

    return calculations

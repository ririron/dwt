import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from util import calcWaveletCoef, calcScalingCoef

def calcCoef(target, result):
    for tar, res in zip(target[:, :], result[:, :]):
        scl = calcScalingCoef(tar)
        wav = calcWaveletCoef(tar)
    
        res[:len(scl)] = scl
        res[len(scl):] = wav 
    
    return result


im = np.array(Image.open('resource/LENNA.bmp')) #入力画像

result = np.zeros((3 ,im.shape[0], im.shape[1]))
result[0] = im

##まずは横にDWT
result[1] = calcCoef(result[0], result[1])


tpResult = result[1].T #楽にするために転置
##次は縦にそれぞれ変換
result[2] = calcCoef(tpResult, result[2])


resultImg = Image.fromarray(result[2].T).convert('L')
resultImg.save('result/test2.bmp')

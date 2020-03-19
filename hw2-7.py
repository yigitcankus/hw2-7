# import pandas as pd
# import numpy as np
# import warnings
# warnings.filterwarnings('ignore')
#
# """
# Endeksi alfabenin ilk 10 harfi olan ve
# ilk 10 asal sayıyı ve ilk 10 fibonacci sayısını içeren bir veri çerçevesi oluşturun.
# """
# index = ("a","b","c","d","e","f","g","h","i","j")
# frame = pd.DataFrame(index=index)
# asal_sayilar=[2,3,5,7,11,13,17,23,27,29]
# fibo=[1,1,2,3,5,8,13,21,34,55]
# frame["asal sayilar"]=asal_sayilar
# frame["fibo sayilar"]=fibo
# print(frame)
#
# #########
# """
# Kaggle'dan Titanic: Machine Learning from Disaster isimli yarışmanın train.csv isimli dosyasını indirin ve
# Pandas veri çerçevelerini kullanarak tüm veriyi yükleyin.
# Veri çerçevelerinin .groupby() metodunu kullanarak yolcuların ortalama yaşlarını
# herbir cinsiyet için ayrı olacak şekilde hesaplayın.
# """
#
# df = pd.read_csv('train.csv')
# print(df.groupby(by="Sex").mean()["Age"])
#
# """
# Koşullu seçim yöntemlerini de kullanarak, 30 yaşından küçük tüm yolcuların kurtulma oranını (survival ratio) hesaplayın.
# Daha sonra, kurtulma oranını cinsiyete göre ayrı ayrı hesaplayın.
# """
#
# print("\n\n\n")
# print(len(df[df["Survived"] == 1] & df["Age"] <30))
# ##yapamadım
#




#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   DİZİDEKİ EN                       #
#                    KÜÇÜK SAYI                       #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################

dizi = [-1500,9,-990,7,-1900,5,4,-100,2,-500]
enKucuk = dizi[0]
for i in range(dizi.__len__()):
    if dizi[i] <= enKucuk:
        enKucuk = dizi[i]
print('DİZİDEKİ EN KÜÇÜK DEĞER...:' , enKucuk)

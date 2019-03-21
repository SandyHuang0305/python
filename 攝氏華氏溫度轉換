#攝氏華氏溫度轉換

celsius = float(input('請輸入攝氏溫度:'))

#計算華氏溫度
fahrenheit = (celsius * 1.8) + 32
print(celsius,'攝氏溫度轉成華氏溫度為', fahrenheit)

#進階版

#問要以哪個溫度為主
a = int(input('攝氏溫度轉華氏溫度請按1\n華氏轉攝氏請按2\n'))
while a != 1 and a != 2:
	a = int(input('輸入錯誤，請重新輸入'))

#以攝氏溫度為主	
if a == 1:
    celsius = float(input('請輸入攝氏溫度:'))	
    fahrenheit = (celsius * 1.8) + 32
    print(celsius, '攝氏溫度轉成華氏溫度為', fahrenheit)

#以華氏溫度為主
else:
	fahrenheit = float(input('請輸入華氏溫度:'))
	celsius = (fahrenheit - 32) / 1.8
	print(fahrenheit, '華氏轉成攝氏溫度為', celsius)

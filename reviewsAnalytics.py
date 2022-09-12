data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print("檔案讀取完，總共有", len(data), "筆資料")

sum = 0
for d in data:
	sum = sum + len(d)

print("留言的平均長度為", sum/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("一共有", len(new), "筆留言長度小於100")
print(new[0]) #index = 0 的資料內容

good = []
for d in data:
	if "good" in d:
		good.append(d)
print("一共有", len(good), "筆留言提到good")
print(good[0]) #index = 0 的資料內容

good1 = [1 for d in data if "good" in d]
print("一共有", len(good1), "筆留言提到good")
#good1 = good 快寫法

bad = ["bad" in d for d in data]
#output = [運算 for 變數 in 清單 (if 篩選條件)]
print(len(bad))

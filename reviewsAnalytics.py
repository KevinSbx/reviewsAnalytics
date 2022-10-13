import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
		# if count % 1000 == 0:
		# 	print(len(data))

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

good1 = [d for d in data if "good" in d]
print("一共有", len(good1), "筆留言提到good")
#good1 = good 快寫法
# d for d in data 第一個d是指原封不動的資料，d也可改ex:1，將1裝進清單中

bad = ["bad" in d for d in data]
#output = [運算 for 變數 in 清單 (if 篩選條件)]
# print(bad) 裡面都是裝True or False 清單
# bad = []
# for d in data:
	# bad.append("bad" in d)


print(data[0])

# 文字計數
star_time = time.time()
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print("花了", end_time - star_time, "seconds")

print(len(wc))
print(wc["Allen"])

while True:
	word = input("請問你想查什麼字: ")
	if word == "q":
		break
	if word in wc:
		print(word, "出現過的次數為: ", wc[word])
	else:
		print("這個字沒有出現過唷!")

print("感謝使用本查詢功能")

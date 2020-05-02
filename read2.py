data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('Done reading file. Total: ', len(data), 'data')

print(data[0])

#文字計數
word_count = {}
word_most_used_count = 0
for d in data:
	words = d.split()
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
new = {}
count = 0
most_word = None
for word in word_count:
	if word_count[word] > 1000000:
		new[word] = word_count[word]

		
		if word_count[word] > count:
			count = word_count[word] 
			most_word = word

print("Most used word count: ", count, 'The word is: ', most_word)
			
print(len(word_count))

while True:
	user_input= input("Search: ")
	if user_input == 'q': 
		break
	elif user_input in word_count:
		print(user_input,' 出現過的次數為： ' ,word_count[user_input])

	else:
		print(user_input, ' 沒有出現過')

print('掰掰～感謝使用本查詢功能 ')

data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('Done reading file. Total: ', len(data), 'data')

# calculate the average characters in each comment.
sum_len = 0
for d in data:  #d is str, data is list
	sum_len = sum_len + len(d)
average = sum_len / len(data)
print('Average characters in each comment: ', average)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('Reviews under 100 characters: ',len(new))
print(new[0])
print(new[1])

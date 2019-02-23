data = []
total_length = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		total_length += len(line) 
		data.append(line.strip())
		#count += 1
		#if count % 1000 == 0:
			#print(len(data))
average_length = total_length / len(data)
print('The file is completely loaded, there is', len(data), 'pieces of comments')
print('The average length of the comment is', average_length)

new_data = []
for d in data:
	if len(d) < 100:
		new_data.append(d)

print(len(new_data))
print(new_data[0])
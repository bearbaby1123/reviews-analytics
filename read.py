import time
import progressbar

# Read File
def read_file(filename):
	with open(filename, 'r') as f:
		bar = progressbar.ProgressBar(max_value=1000000)
		data = []
		count = 0
		total_length = 0
		for line in f:
			data.append(line.strip())
			total_length += len(line) 
			count += 1
			bar.update(count)
		
		data_and_length = [data, total_length]
	return data_and_length

# Filter reviews under 100 words
def filter_len(data, length):
	new_data = []
	for d in data:
		if len(d) < length:
			new_data.append(d)
	return new_data

# Filter reviews including good
def filter_word(data, word):
	word_data = []
	for d in data:
		if word in d:
			word_data.append(d)
	return word_data

# Count how many times a word used
def wc(data):
	word_count = {}
	for d in data:
		for word in d.split(' '):
			if word in word_count:
				word_count[word] += 1
			else:
				word_count[word] = 1
	return word_count

#Filter words used over	100000 times
def filter_count(word_count, count):
	for word in word_count:
		if word_count[word] > count:
			print(word, ':', word_count[word])

# Let user search
def user_search(word_count):
	while True:
		word = input('Which word do you want to look up? ')
		if word == 'q':
			break
		if word in word_count:
			print(word_count[word])
		else:
			print('This word is not involved in all reviews')

def main():
	data_and_length = read_file('reviews.txt')
	data = data_and_length[0]
	total_length = data_and_length[1]
	#new_data = filter_len(data, 100)
	#word_data = filter_word(data, 'good')
	#print('The file is completely loaded, there is', len(data), 'pieces of comments')
	#average_length = total_length / len(data)
	#print('There are', len(new_data), 'comments under 100 words')
	#print('The average length of the comment is', average_length)
	#print('There are', len(word_data), 'comments including "good"')
	#print(word_data[0])
	start_time = time.time()
	word_count = wc(data)
	print('There are', len(word_count), 'different words in all reviews')
	filter_count(word_count, 1000000)
	end_time = time.time()
	print('it takes ', end_time - start_time, 'seconds')
	user_search(word_count)

main()

#the basics 
#Sara Gottlieb
# reverse a string 
# method takes in argument of the sample_string
# in python, strings are immutable, so I have to split the string into a list, then return a new string
def reverse_string(sample_string):
	#first I change the string into a list, so I can chenge the indexes
	sample_string = list(sample_string)
	# I start a for loop that starts at 0 and goes to half the length of the list
	for i in range(0, len(sample_string)/2):
		#now change the list in place by saving my first index to a
		a = sample_string[i]
		#set the current index to the opposite index in the list
		sample_string[i] = sample_string[len(sample_string)-1-i]
		#then set the opposite to the variable where we saved the initial
		sample_string[len(sample_string)-1-i] = a
	#now join the list back into a string and return the result	
	return ''.join(sample_string)
# find the longest repeating substring in text

#nth fibonacci in sequence
#recursion
def fibonacci_recursion(n):
	#first I need to set the initial 2 positions
	if n==0:
		return 0
	elif n==1:
		return 1
	#then call recursively to build off of the initial positions and return the result
	#it will call recursively until it hits 0 and then build itself back up to produce the results
	elif n>1:
		return fibonacci(n-1) + fibonacci(n-2)

#iteration
def fibonacci_iter(n):
	#again I have to set the first two cases, then I can build off of that
	a, b = 0, 1
	#I take in the argument and create a for loop up until that number
	#every time I iterate through a number in the range, I add on top of my first two cases 
	#I set the first case to the next number and b(next number) to the current plus the next	
	for i in range(n):
		a, b = b, a+b
	#once I've exited the for loop, I return the current number
	return a


# I have to import regular expression to parse through the events
import re
def access_logs():
	#read in log file
	#first read in the file, save it, then close it
	f = open("mediacast_access.log")
	text = f.read()
	f.close()
	#then split the text file into each event that I want to parse through-by spliting on every line
	text = text.split('\n')
	# creating empty dictionaries and a list to store the information that will be parsing out 
	# going to make an exceptions list to put in the events that are erroring (usually just empty, but just in case)
	exceptions = []
	request_counts ={}
	top_url = {}
	request_size  =[]
	for events in text:
		#using regular expression to search through each item to parse out the url, status_code and size
		request = re.search('"GET (.*) H.*" (\d{3}) (\d*)', str(events))
		#so I won't raise an error, check that I actually have gotten a response
		if request != None:
			#set each of the values parsed out to their respective variable names
			url = request.group(1)
			status_code = request.group(2)
			size = request.group(3)
			# add the request counts and url requests to dictionaries 
			# use the get method to either get the value from the dictionary or set the value to zero 
			url_count = top_url.get(url, 0)
			top_url[url] = url_count + 1
			request_count = request_counts.get(status_code, 0)
			request_counts[status_code] =request_count +1 
			#append the size to the list of sizes to then extract the avg and median
			request_size.append(int(size))
		else:
			exceptions.append(events)
	#get the median and average use the request_median and average method
	median = request_median(request_size)	
	average = request_average(request_size)
	to_url_results = top_five(top_url)
	print request_counts
#sort top url
def request_median(request_list):
	#take in the request list and calculate the median 
	request_list.sort()
	if len(request_list) % 2 == 0:
		median = (request_list[len(request_list)/2]+ request_list[len(request_list)/2+1])/2
	else:
		median = request_list[len(request_list)/2 +1]
	#print the results
	print 'median request size = ', median
	return median 

def request_average(request_list):
	#do the same for average
	average = sum(request_list)/len(request_list)
	print 'average request size = ', average
	return average

#make a method that takes a dictionary and returns the top 5 URLs and counts
def top_five(url_dict):
	#first, create a list to put the values in -[value, key]
	top = [[0, 0]]*5
	#iterate through the list
	for k, v in url_dict.iteritems():
		#for every event, sort the top list so the url with the fewest hits is the first item in the list
		top.sort()
		#if the value is greater than the smallest item in the list, it replaces the smallest
		if v > top[0][0]:
			top[0] = [v, k]
	print "top five urls and number of hits = " top
	return top

access_logs()









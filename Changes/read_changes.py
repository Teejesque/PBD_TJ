
# open the file - and read all of the lines.
changes_file = "changes_python.log"

#my_file = open(changes_file, 'r')
#data = my_file.readlines()
data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

commits = []

index = 0

while index < len(data):
	try:
		# parse each of the commits and put them into a list of commits
		details = data[index + 1].split(' | ')
		#print details
		commits.append(details)
		
		index = data.index(sep, index + 1)
	except IndexError:
		break
		
# print len(commits)


output_file = "changes.csv"
my_file = open(output_file, "w")
my_file.write("Revision,Author,Date\n")

for details in commits:
	my_file.write(details[0].strip() + "," + details[1].strip() + ",'" + details[2] + "'\n")

my_file.close()

arr = []

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature. Ignore the row")

# print(arr)
# print(sum(arr[0:7]) / len(arr[0:7]))
# print(max(arr))

# in part above we want to work with the entire data so list is enough. below we show how to
# use dictionary to work on specific dates.

# print("Second Question")

nyc_temp = {}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            day = tokens[0]
            temperature = int(tokens[1])
            nyc_temp[day] = temperature
        except:
            print("Invalid temperature. Ignore the row")

# print(nyc_temp['Jan 9'])
# print(nyc_temp['Jan 4'])

########################################
#Question 3

print("Question 3")

word_count = {}

with open("poem.txt") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n', '')
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

print(word_count)
print("The word with maximum count is:", {i for i in word_count if word_count[i] == max(word_count.values())})
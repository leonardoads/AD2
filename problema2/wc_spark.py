def output(text):
    word = text.split(',')
    return (word[4][18:28]+word[0][10:],1)

text_file = sc.textFile("input.txt")
counts = text_file.flatMap(lambda line: line.split("\n")
counts = counts.map(lambda word:  output(word))
counts.saveAsTextFile("out2")

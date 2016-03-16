def output(text):
    word = text.split(',')
    return (word[1][12:]+word[2][13:],1)

text_file = sc.textFile("input.txt")
counts = text_file.flatMap(lambda line: line.split("\n"))
counts = counts.map(lambda word:  output(word))
counts.saveAsTextFile("out2")

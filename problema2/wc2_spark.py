def output(text):
    word = text.split(',')
    return ("%s|%s"%(word[1][13:-1],word[2][14:-1]),1)

def output0(text):
    word = text.split(',')
    return "%s|%s"%(word[1][13:-1],word[2][14:-1])

def output1(text):
    word = text.split('|')
    return (word[0],1)

text_file = sc.textFile("input.txt")
counts = text_file.flatMap(lambda line: line.split("\n"))
counts = counts.map(lambda word:  output(word))
counts = counts.reduceByKey(lambda a, b: a + b)
counts = counts.map(lambda word:  output1(word[0]))
counts = counts.reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("out2")

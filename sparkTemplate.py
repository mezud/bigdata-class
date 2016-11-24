from pyspark import SparkConf, SparkContext


def main(sc):
    textFile = sc.textFile("shakespeare_100.txt")
    words = textFile.flatMap(lambda line: line.split())
    wordWithCount = words.map(lambda word: (word, 1))
    wordWithCount.saveAsTextFile("word_count.txt")
    collectedWords = wordWithCount.take(5)
    print(collectedWords)


if __name__  == "__main__":
    conf = SparkConf().setAppName("Testing Spark Commands")
    sc = SparkContext(conf = conf)
    main(sc)
    sc.stop()



#spark-submit --master yarn-client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m sparkTemplate.py
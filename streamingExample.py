from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext

if __name__  == "__main__":
    conf = SparkConf().setAppName("Testing Spark Streaming")
    sc = SparkContext(conf = conf)
    stream = StreamingContext(sc, 1)
    lines = stream.socketTextStream("localhost", 9999)
    counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
    counts.pprint()
    stream.start()
    stream.awaitTermination()











#spark-submit --master yarn-client --executor-memory 512m --num-executors 3 --executor-cores 1 --driver-memory 512m streamingExample.py
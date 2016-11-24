from pyspark import SparkConf, SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel

def main(sc):
    data = [[1.0,1.0],[1.0,0.8],[-1.0,1.0],[-1.0,-1.0]]
    parsedData=sc.parallelize(data)
    kmeansModel = KMeans.train(parsedData, 2, maxIterations=10, runs=10, initializationMode="random")
    print(kmeansModel.predict([1.0, 1.0]))
    print(kmeansModel.predict([1.0, -2.0]))
    # Save and load model
    kmeansModel.save(sc, "KMeansModel")
    model = KMeansModel.load(sc, "KMeansModel")
    print(model.predict([1.0, 1.0]))
    print(model.predict([1.0, -2.0]))


if __name__  == "__main__":
    conf = SparkConf().setAppName("Testing Spark Commands")
    sc = SparkContext(conf = conf)
    main(sc)
    sc.stop()
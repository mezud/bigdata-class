from pyspark.mllib.classification import LogisticRegressionWithSGD, LogisticRegressionModel
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkConf, SparkContext

def main(sc):
    data = [
        LabeledPoint(0.0, [0.0, 1.0]),
        LabeledPoint(1.0, [1.0, 0.0])
        ]
    lrm = LogisticRegressionWithSGD.train(sc.parallelize(data), iterations=10)
    print (lrm.predict([1.0, 0.0]))
    print(lrm.predict([0.0, 1.0]))
    # Save and load model
    lrm.save(sc, "lrsgd")
    sameModel = LogisticRegressionModel.load(sc, "lrsgd")
    print(sameModel.predict([1.0, 0.0]))
    print(sameModel.predict([0.0, 1.0]))

if __name__  == "__main__":
    conf = SparkConf().setAppName("Testing Spark Commands")
    sc = SparkContext(conf = conf)
    main(sc)
    sc.stop()
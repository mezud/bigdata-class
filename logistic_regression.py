#install numpy
# yum install -y numpy
from pyspark.mllib.classification import LogisticRegressionWithLBFGS, LogisticRegressionModel
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkConf, SparkContext

def main(sc):
# Load and parse the data
    def parsePoint(line):
        values = [float(x) for x in line.split(' ')]
        return LabeledPoint(values[0], values[1:])

    data = sc.textFile("logistic_regression_data.txt")
    parsedData = data.map(parsePoint)

    # Build the model
    model = LogisticRegressionWithLBFGS.train(parsedData)

    # Evaluating the model on training data
    labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
    trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())
    print("Training Error = " + str(trainErr))

    # Save and load model
    model.save(sc, "myModelPath")
    sameModel = LogisticRegressionModel.load(sc, "myModelPath")


if __name__  == "__main__":
    conf = SparkConf().setAppName("Testing Spark Commands")
    sc = SparkContext(conf = conf)
    main(sc)
    sc.stop()


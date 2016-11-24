from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
from pyspark import SparkConf, SparkContext

def main(sc):
    r1 = (1, 1, 1.0)
    r2 = (1, 2, 2.0)
    r3 = (2, 1, 2.0)
    ratings = sc.parallelize([r1, r2, r3])
    model = ALS.train(ratings, 10, 10)
    # Evaluate the model on training data
    testdata = sc.parallelize([(1,1),(2,2)])
    predictions = model.predictAll(testdata)
    print(predictions.collect())
    # Save and load model
    model.save(sc, "myCollaborativeFilter")
    sameModel = MatrixFactorizationModel.load(sc, "myCollaborativeFilter")
    #Try using the loaded model
    print(sameModel.predictAll(testdata).collect())


if __name__  == "__main__":
    conf = SparkConf().setAppName("Testing Spark Commands")
    sc = SparkContext(conf = conf)
    main(sc)
    sc.stop()
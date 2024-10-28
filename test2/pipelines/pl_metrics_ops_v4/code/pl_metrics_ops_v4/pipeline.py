from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v4.config.ConfigStore import *
from pl_metrics_ops_v4.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v4")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v4")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v4", config = Config)(pipeline)

if __name__ == "__main__":
    main()

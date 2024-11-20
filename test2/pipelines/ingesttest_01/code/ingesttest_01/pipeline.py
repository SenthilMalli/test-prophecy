from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ingesttest_01.config.ConfigStore import *
from ingesttest_01.functions import *
from prophecy.utils import *
from ingesttest_01.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_malformed = src_csv_malformed(spark)
    df_OrderBy_1 = OrderBy_1(spark, df_src_csv_malformed)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("ingesttest_01")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ingesttest_01")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/ingesttest_01", config = Config)(pipeline)

if __name__ == "__main__":
    main()

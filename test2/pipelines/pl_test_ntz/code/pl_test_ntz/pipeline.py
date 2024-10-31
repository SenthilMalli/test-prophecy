from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_test_ntz.config.ConfigStore import *
from pl_test_ntz.functions import *
from prophecy.utils import *
from pl_test_ntz.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_ds = src_ds(spark)
    df_add_created_timestamp = add_created_timestamp(spark, df_src_ds)
    tgt_ds(spark, df_add_created_timestamp)
    df_SodaDataQualityCheck_1 = SodaDataQualityCheck_1(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_test_ntz")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_test_ntz")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_test_ntz", config = Config)(pipeline)

if __name__ == "__main__":
    main()

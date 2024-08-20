from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_observability_test_v1.config.ConfigStore import *
from pl_observability_test_v1.functions import *
from prophecy.utils import *
from pl_observability_test_v1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_ds_test_in2 = src_ds_test_in2(spark)
    df_src_ds_test = src_ds_test(spark)
    df_reformat_columns = reformat_columns(spark, df_src_ds_test)
    df_inner_join = inner_join(spark, df_reformat_columns, df_src_ds_test_in2)
    df_reformat_columns_1 = reformat_columns_1(spark, df_inner_join)
    tgt_ds_test(spark, df_reformat_columns_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_observability_test_v1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_observability_test_v1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_observability_test_v1", config = Config)(pipeline)

if __name__ == "__main__":
    main()

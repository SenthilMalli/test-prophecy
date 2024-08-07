from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_test_observability.config.ConfigStore import *
from pl_test_observability.functions import *
from prophecy.utils import *
from pl_test_observability.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_ds = src_ds(spark)
    df_src_ds = collectMetrics(
        spark, 
        df_src_ds, 
        "graph", 
        "q9wWy3qWhN7vA3MaUPjxz$$JWHoJfhoCPtoSPHps5Srw", 
        "Bw9PbkgUtV97-4P6UBi6u$$fB_90fnVFB60CcTBXEQBx"
    )
    df_add_created_timestamp = add_created_timestamp(spark, df_src_ds)
    df_add_created_timestamp = collectMetrics(
        spark, 
        df_add_created_timestamp, 
        "graph", 
        "MbhYgXsvxWX1rA0YeDjYg$$XodXDMjGRdw9yMb4XeEnm", 
        "_-2y4z9urpuvVTT5wYrBk$$_jGTtusxYSohFs81Y1dLP"
    )
    tgt_ds(spark, df_add_created_timestamp)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_test_observability")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_test_observability")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_test_observability", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

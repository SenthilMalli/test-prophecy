from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_observability_test_v1_inputonly.config.ConfigStore import *
from pl_observability_test_v1_inputonly.functions import *
from prophecy.utils import *
from pl_observability_test_v1_inputonly.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_ds_test_in2 = src_ds_test_in2(spark)
    df_src_ds_test_in2 = collectMetrics(
        spark, 
        df_src_ds_test_in2, 
        "graph", 
        "0fOR39nett9fFG2bQ7RSg$$xdB8DX35Q2v8PBStK1a28", 
        "bkgwKAcYM0cYLKEycN3EE$$CIQEqqENDzhdOWoOW5IH_"
    )
    df_src_ds_test = src_ds_test(spark)
    df_src_ds_test = collectMetrics(
        spark, 
        df_src_ds_test, 
        "graph", 
        "TXpEUXBIKHYGTSm8ZsjTC$$GROT6C0bbVm4yi_JePKLB", 
        "r2qRnbiV25e3ziGts9npe$$SGI6n-dqRuf7FDvKa-nqa"
    )
    df_reformat_columns = reformat_columns(spark, df_src_ds_test)
    df_reformat_columns = collectMetrics(
        spark, 
        df_reformat_columns, 
        "graph", 
        "TRJmnemKYCAGUih3FrzoM$$JMTbjGBBLapLkLEqCABWH", 
        "rph-AT7AuvMz4D83i8Pps$$VIgtpbpX3SygFQfelMlYW"
    )
    df_inner_join = inner_join(spark, df_reformat_columns, df_src_ds_test_in2)
    df_inner_join = collectMetrics(
        spark, 
        df_inner_join, 
        "graph", 
        "AuN9tJFx26ZcFfHxEhZtW$$UNlR-tg7n-dosOZc5asc_", 
        "c4X_dK51WD3-AokhoLjZr$$DRlI8GB-W88FieYhorhTE"
    )
    df_reformat_columns_1 = reformat_columns_1(spark, df_inner_join)
    df_reformat_columns_1 = collectMetrics(
        spark, 
        df_reformat_columns_1, 
        "graph", 
        "6IOE4xzBcj6kYnMIQjMNC$$hzWtLzPETmLPhIfuYVMkr", 
        "_fAsXq20EEY6N3M5ikIg3$$7fLf8UXPZoHXa4ZbxHYd6"
    )
    tgt_ds_test(spark, df_reformat_columns_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_observability_test_v1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_observability_test_v1_InputOnly")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_observability_test_v1_InputOnly", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

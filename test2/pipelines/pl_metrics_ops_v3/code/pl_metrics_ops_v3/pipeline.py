from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v3.config.ConfigStore import *
from pl_metrics_ops_v3.functions import *
from prophecy.utils import *
from pl_metrics_ops_v3.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_metric3 = src_csv_metric3(spark)
    df_src_csv_metric3 = collectMetrics(
        spark, 
        df_src_csv_metric3, 
        "graph", 
        "4E8mCEGD7_ESRbMXaZAWp$$521FqleZtuI6YoQjFXmkJ", 
        "21bHPGy0a6hRfQK589BgH$$jHgkHkRi4iir9CCf1WKiN"
    )
    df_sales_projection = sales_projection(spark, df_src_csv_metric3)
    df_sales_projection = collectMetrics(
        spark, 
        df_sales_projection, 
        "graph", 
        "5Vc8j5rNCzw7I8T1RQg48$$78-rxZ_zXGEFsxBQgTtmm", 
        "5khuTlnl85jco4-cfLsy6$$01KmVfWWjBlf1M8j3nRZK"
    )
    tgt_tbl_metric3(spark, df_sales_projection)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v3")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v3")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v3", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

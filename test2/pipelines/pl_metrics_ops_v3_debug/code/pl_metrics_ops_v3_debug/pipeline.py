from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v3_debug.config.ConfigStore import *
from pl_metrics_ops_v3_debug.functions import *
from prophecy.utils import *
from pl_metrics_ops_v3_debug.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_metric3 = src_csv_metric3(spark)
    df_src_csv_metric3 = collectMetrics(
        spark, 
        df_src_csv_metric3, 
        "graph", 
        "rFPoikStAyB-cnqo6V-bw$$L3A1God9MmdEJ_6RcPB0V", 
        "-wH_eSg1Lg-CjTsR6DFul$$7wazRnxEyCHWGvdhhH8gX"
    )
    df_sales_projection = sales_projection(spark, df_src_csv_metric3)
    df_sales_projection = collectMetrics(
        spark, 
        df_sales_projection, 
        "graph", 
        "at65WvcVhVBpm15TRML5X$$bCtJHjtFaqw_TAPBQyFE9", 
        "IX96cdfclTlwNdV3lnKvB$$ZGqPRZawzjapO_o8gLCDp"
    )
    tgt_tbl_metric3(spark, df_sales_projection)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v3_debug")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v3_debug")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v3_debug", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

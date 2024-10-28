from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v2.config.ConfigStore import *
from pl_metrics_ops_v2.functions import *
from prophecy.utils import *
from pl_metrics_ops_v2.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_tbl_pq_metrics_test2 = src_tbl_pq_metrics_test2(spark)
    df_src_tbl_pq_metrics_test2 = collectMetrics(
        spark, 
        df_src_tbl_pq_metrics_test2, 
        "graph", 
        "LIWW_VN8LVEVyidfMG_v-$$GQ3ccPd2Q9O5LORtitMK6", 
        "p_LCxAax1s0ajWdzrcfNf$$ZMRI8obCWHHATbehNidKj"
    )
    df_sales_projection = sales_projection(spark, df_src_tbl_pq_metrics_test2)
    df_sales_projection = collectMetrics(
        spark, 
        df_sales_projection, 
        "graph", 
        "5FvNtehEQ2WNM1xvd8vY1$$T_4-juY0iKDXr3GQP5vJ7", 
        "EXrNLAM-C057LJe6Hv4Dh$$AVzQx2o1qIZdTFzQ_1sMH"
    )
    tgt_tbl_metric3(spark, df_sales_projection)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v2")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v2")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v2", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

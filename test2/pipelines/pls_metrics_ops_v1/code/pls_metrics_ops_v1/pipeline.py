from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pls_metrics_ops_v1.config.ConfigStore import *
from pls_metrics_ops_v1.functions import *
from prophecy.utils import *
from pls_metrics_ops_v1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_tbl_pq_metrics_test2 = src_tbl_pq_metrics_test2(spark)
    df_src_tbl_pq_metrics_test2 = collectMetrics(
        spark, 
        df_src_tbl_pq_metrics_test2, 
        "graph", 
        "pgMALTu9cupCVVqPAYSBC$$eik3Ornf3SIH53FZCTbzy", 
        "MyxEePxzeIczNclKh9zAP$$JpcVv0RdN1PAJZvz3sPfR"
    )
    df_add_created_timestamp = add_created_timestamp(spark, df_src_tbl_pq_metrics_test2)
    df_add_created_timestamp = collectMetrics(
        spark, 
        df_add_created_timestamp, 
        "graph", 
        "cG8Ws0TqFcwcs5l2Q88Ps$$ktrhJe00Pc0lca0AUnNf8", 
        "oU_bDFhRIgwYAiZrH6VGc$$g05RHvM6HAdnQRoj2nN70"
    )
    tgt_tbl_pq_metric_r1(spark, df_add_created_timestamp)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pls_metrics_ops_v1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pls_metrics_ops_v1")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pls_metrics_ops_v1", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

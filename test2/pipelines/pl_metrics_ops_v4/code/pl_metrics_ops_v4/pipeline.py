from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v4.config.ConfigStore import *
from pl_metrics_ops_v4.functions import *
from prophecy.utils import *
from pl_metrics_ops_v4.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_metric3 = src_csv_metric3(spark)
    df_src_csv_metric3 = collectMetrics(
        spark, 
        df_src_csv_metric3, 
        "graph", 
        "WWDDcZj8KLlMk8bpde43z$$V5MaTZ_R6ivkCzMc8VDhD", 
        "3OppFFyOCfyQ7H39aZqZF$$w1VD6AL2MK5aksM0Isomr"
    )
    df_sales_projection = sales_projection(spark, df_src_csv_metric3)
    df_sales_projection = collectMetrics(
        spark, 
        df_sales_projection, 
        "graph", 
        "tqqFhX-3zABSN56gaF8q8$$bjLE7HVp3quJBsK8Bob64", 
        "lrW-1PHmzfG4_6ErdcAlQ$$5pQBWdq14Th4Ee5hRmNhJ"
    )
    tgt_tbl_metric3(spark, df_sales_projection)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v4")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v4")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v4", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

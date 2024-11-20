from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v6.config.ConfigStore import *
from pl_metrics_ops_v6.functions import *
from prophecy.utils import *
from pl_metrics_ops_v6.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_tbl_metric5 = src_tbl_metric5(spark)
    df_src_tbl_metric5 = collectMetrics(
        spark, 
        df_src_tbl_metric5, 
        "graph", 
        "jNZcBOPW7cyuZevbWHuR8$$iBW_KHG9KgDzm9W-0XVuw", 
        "izvCrfLMP7yS2xlViCnn0$$BZwu0_4M3nLpz-Si4zS8u"
    )
    df_select_columns = select_columns(spark, df_src_tbl_metric5)
    df_select_columns = collectMetrics(
        spark, 
        df_select_columns, 
        "graph", 
        "B4gqFq3ASzv8nyZqFrgkC$$s2WRyGhjGSjp9CtP_LGvy", 
        "mXdGs-D6CpQCSyAqsfIwD$$R7BDskUsiBwXlmLWpBPbP"
    )
    df_select_columns.cache().count()
    df_select_columns.unpersist()

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v6")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v6")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v6", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

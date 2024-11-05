from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v5.config.ConfigStore import *
from pl_metrics_ops_v5.functions import *
from prophecy.utils import *
from pl_metrics_ops_v5.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_metric3 = src_csv_metric3(spark)
    df_src_csv_metric3 = collectMetrics(
        spark, 
        df_src_csv_metric3, 
        "graph", 
        "NsnNWwAY26Nqu20rnGxzl$$ci3dAJbAn5USgVWd2enjn", 
        "ig0NHwxouoAW3dWl3O9CK$$6TkzD7dE9l7N0B5HqOhsV"
    )
    df_sales_projection = sales_projection(spark, df_src_csv_metric3)
    df_sales_projection = collectMetrics(
        spark, 
        df_sales_projection, 
        "graph", 
        "vJfhXIlV1xuXUKVlpZ-f6$$SqKvqghS5PrV8j3ZGR3nq", 
        "aozo5q1uffa6-5EfbUnEh$$TkEyflq26yDj_qlmGmeJa"
    )
    tgt_tbl_insert_metric3(spark, df_sales_projection)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v5")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v5")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v5", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

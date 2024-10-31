from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v5.config.ConfigStore import *
from pl_metrics_ops_v5.functions import *
from prophecy.utils import *
from pl_metrics_ops_v5.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_metric3 = src_csv_metric3(spark)
    df_sales_projection = sales_projection(spark, df_src_csv_metric3)
    tgt_tbl_insert_metric3(spark, df_sales_projection)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v5")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v5")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v5", config = Config)(pipeline)

if __name__ == "__main__":
    main()

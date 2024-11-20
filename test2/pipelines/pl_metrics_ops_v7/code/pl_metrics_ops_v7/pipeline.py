from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v7.config.ConfigStore import *
from pl_metrics_ops_v7.functions import *
from prophecy.utils import *
from pl_metrics_ops_v7.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_metric5 = src_csv_metric5(spark)
    df_sales_projection = sales_projection(spark, df_src_csv_metric5)
    tgt_tbl_metric5(spark, df_sales_projection)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v7")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v7")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v7", config = Config)(pipeline)

if __name__ == "__main__":
    main()

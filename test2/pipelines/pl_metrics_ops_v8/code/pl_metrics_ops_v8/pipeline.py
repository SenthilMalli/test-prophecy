from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v8.config.ConfigStore import *
from pl_metrics_ops_v8.functions import *
from prophecy.utils import *
from pl_metrics_ops_v8.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_tbl_metric5 = src_tbl_metric5(spark)
    df_reformat_columns = reformat_columns(spark, df_src_tbl_metric5)
    tgt_tbl_metric5(spark, df_reformat_columns)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_metrics_ops_v8")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v8")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v8", config = Config)(pipeline)

if __name__ == "__main__":
    main()

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pls_metrics_ops_v1.config.ConfigStore import *
from pls_metrics_ops_v1.functions import *
from prophecy.utils import *
from pls_metrics_ops_v1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_tbl_pq_metrics_test2 = src_tbl_pq_metrics_test2(spark)
    df_add_created_timestamp = add_created_timestamp(spark, df_src_tbl_pq_metrics_test2)
    tgt_tbl_pq_metric_r1(spark, df_add_created_timestamp)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pls_metrics_ops_v1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pls_metrics_ops_v1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pls_metrics_ops_v1", config = Config)(pipeline)

if __name__ == "__main__":
    main()

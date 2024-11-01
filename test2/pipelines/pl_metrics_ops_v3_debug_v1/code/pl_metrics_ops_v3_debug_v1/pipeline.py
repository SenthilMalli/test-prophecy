from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_metrics_ops_v3_debug_v1.config.ConfigStore import *
from pl_metrics_ops_v3_debug_v1.functions import *
from prophecy.utils import *
from pl_metrics_ops_v3_debug_v1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_metric3 = src_csv_metric3(spark)
    df_Reformat_1 = Reformat_1(spark, df_src_csv_metric3)
    tgt_tbl_insert_metric3(spark, df_Reformat_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_metrics_ops_v3_debug_v1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_metrics_ops_v3_debug_v1", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()

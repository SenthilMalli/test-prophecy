from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_test_observability.config.ConfigStore import *
from pl_test_observability.functions import *
from prophecy.utils import *
from pl_test_observability.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_table = src_table(spark)
    df_src_table = collectMetrics(
        spark, 
        df_src_table, 
        "graph", 
        "ep596CjQTUhERwyYHmCsE$$FTijs9efr3SwPNC4KDSi1", 
        "eC_7pufXb8hDvSgw1BJ_P$$eTSjRNvDM1kQ86uK8ZnnJ"
    )
    df_Reformat_1 = Reformat_1(spark, df_src_table)
    df_Reformat_1 = collectMetrics(
        spark, 
        df_Reformat_1, 
        "graph", 
        "ZrzPlQX07NNhAMPDvyffz$$CLIVAhWdJAebUYOkrDdYs", 
        "PjMftZdlLMzLALF73tu2t$$qQhIM17E0bgOhbMzlZk3k"
    )
    tgt_table(spark, df_Reformat_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_test_observability")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_test_observability")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_test_observability", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()

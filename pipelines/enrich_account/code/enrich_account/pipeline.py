from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from enrich_account.config.ConfigStore import *
from enrich_account.udfs.UDFs import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("enrich_account")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/enrich_account")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/enrich_account", config = Config)(pipeline)

if __name__ == "__main__":
    main()

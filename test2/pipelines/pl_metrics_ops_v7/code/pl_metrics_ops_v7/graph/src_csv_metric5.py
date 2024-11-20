from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v7.config.ConfigStore import *
from pl_metrics_ops_v7.functions import *

def src_csv_metric5(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("trandate", StringType(), True), StructField("salesamt", LongType(), True), StructField("ymd", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/mnt/landing/prophecy/ops/transsample.csv")

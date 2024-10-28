from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v3.config.ConfigStore import *
from pl_metrics_ops_v3.functions import *

def src_csv_metric3(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("trandate", StringType(), True), StructField("salesamt", StringType(), True), StructField("ymd", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/mnt/landing/prophecy/ops/transsample.csv")

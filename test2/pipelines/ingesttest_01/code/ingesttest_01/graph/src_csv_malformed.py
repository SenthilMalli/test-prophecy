from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from ingesttest_01.config.ConfigStore import *
from ingesttest_01.functions import *

def src_csv_malformed(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Name", StringType(), True), StructField(" Age", StringType(), True), StructField(" Salary", StringType(), True), StructField("malformed", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("mode", "permissive")\
        .option("sep", ",")\
        .option("columnNameOfCorruptRecord", "malformed")\
        .csv("/mnt/landing/prophecy/malformed/*.csv")

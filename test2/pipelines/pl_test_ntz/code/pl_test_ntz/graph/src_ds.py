from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_ntz.config.ConfigStore import *
from pl_test_ntz.functions import *

def src_ds(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("parquet")\
        .load("dbfs:/mnt/landing/prophecy/s4/sourcesample/part-Z1uDuYqG3pMk8SHX-Gw_MOFZjz1D4iA3w.parquet")

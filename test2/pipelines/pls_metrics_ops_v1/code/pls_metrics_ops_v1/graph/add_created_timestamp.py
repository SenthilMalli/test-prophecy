from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pls_metrics_ops_v1.config.ConfigStore import *
from pls_metrics_ops_v1.functions import *

def add_created_timestamp(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("transdate"), 
        col("salesamt"), 
        col("ymd"), 
        from_utc_timestamp(now(), "Europe/London").alias("createdtimestamp")
    )

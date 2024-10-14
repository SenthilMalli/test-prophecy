from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_observability_test_v1_targets.config.ConfigStore import *
from pl_observability_test_v1_targets.functions import *

@instrument
def reformat_columns(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("col1").cast(IntegerType()).alias("s1_col1"), 
        col("col2").cast(IntegerType()).alias("s1_col2"), 
        (col("col2") * col("col1")).alias("s1_col3"), 
        from_utc_timestamp(col("load_timestamp").cast(TimestampType()), "Europe/London").alias("s1_load_timestamp")
    )

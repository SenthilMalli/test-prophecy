from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_observability.config.ConfigStore import *
from pl_test_observability.functions import *

@instrument
def add_created_timestamp(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("col1"), 
        col("col2"), 
        from_utc_timestamp(current_timestamp(), "Europe/London").alias("load_timestamp")
    )

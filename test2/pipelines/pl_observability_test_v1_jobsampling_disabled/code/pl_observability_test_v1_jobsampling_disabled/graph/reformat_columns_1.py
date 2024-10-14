from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_observability_test_v1_jobsampling_disabled.config.ConfigStore import *
from pl_observability_test_v1_jobsampling_disabled.functions import *

@instrument
def reformat_columns_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("s1_col1").cast(DecimalType(10, 2)).alias("col1"), 
        col("col2"), 
        col("s1_col3").cast(DecimalType(10, 2)).alias("col3"), 
        col("load_timestamp")
    )

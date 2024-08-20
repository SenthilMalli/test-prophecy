from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_ntz.config.ConfigStore import *
from pl_test_ntz.functions import *

def add_created_timestamp(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("col1"), 
        col("col2"), 
        col("file_name"), 
        col("file_id"), 
        col("load_timestamp"), 
        col("pipeline_id"), 
        col("year"), 
        col("month"), 
        col("day")
    )

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_ntz.config.ConfigStore import *
from pl_test_ntz.functions import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("referencelevel1"), 
        col("referencelevel2"), 
        col("key"), 
        col("value"), 
        col("createdtimestamp"), 
        col("modifiedtimestamp")
    )

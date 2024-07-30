from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_observability.config.ConfigStore import *
from pl_test_observability.functions import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("submitted_at"), 
        col("date_range"), 
        col("region"), 
        col("no_of_collegues"), 
        col("response"), 
        col("label"), 
        col("store"), 
        col("file_name"), 
        col("load_datetime")
    )

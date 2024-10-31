from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v4.config.ConfigStore import *
from pl_metrics_ops_v4.functions import *

@instrument
def sales_projection(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("trandate").cast(DateType()).alias("trandate"), 
        col("salesamt").cast(DecimalType(10, 0)).alias("salesamt"), 
        col("ymd").cast(DecimalType(10, 0)).alias("ymd")
    )

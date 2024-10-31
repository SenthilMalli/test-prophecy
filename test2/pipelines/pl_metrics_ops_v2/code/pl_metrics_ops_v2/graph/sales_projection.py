from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v2.config.ConfigStore import *
from pl_metrics_ops_v2.functions import *

@instrument
def sales_projection(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("transdate"), col("salesamt"), col("ymd"))

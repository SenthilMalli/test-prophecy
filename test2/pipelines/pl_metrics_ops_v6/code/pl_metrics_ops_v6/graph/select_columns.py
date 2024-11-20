from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v6.config.ConfigStore import *
from pl_metrics_ops_v6.functions import *

@instrument
def select_columns(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("col1").cast(LongType()).alias("col1"), col("col2"), col("load_timestamp"))

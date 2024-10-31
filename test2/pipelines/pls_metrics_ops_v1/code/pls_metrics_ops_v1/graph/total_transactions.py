from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pls_metrics_ops_v1.config.ConfigStore import *
from pls_metrics_ops_v1.functions import *

@instrument
def total_transactions(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.agg(count(col("transdate")).alias("total_trans"))

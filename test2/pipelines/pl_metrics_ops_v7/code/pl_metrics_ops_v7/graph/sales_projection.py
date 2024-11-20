from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v7.config.ConfigStore import *
from pl_metrics_ops_v7.functions import *

def sales_projection(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("salesamt").alias("col1"), col("trandate").alias("col2"), now().alias("load_timestamp"))

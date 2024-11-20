from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from ingesttest_01.config.ConfigStore import *
from ingesttest_01.functions import *

def OrderBy_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy()

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_observability.config.ConfigStore import *
from pl_test_observability.functions import *

def src_table(spark: SparkSession) -> DataFrame:
    return spark.read.table("`cultureamp_ingest_ndev`.`surveyresponse_s_tbl`")

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_observability.config.ConfigStore import *
from pl_test_observability.functions import *

def tgt_table(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("error").saveAsTable("`sst_ingest_ndev`.`observabilitytest_ns_tbl`")

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_ntz.config.ConfigStore import *
from pl_test_ntz.functions import *

def src_ds(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sst_ingest_ndev`.`opsdeadlock1_ns_tbl`")

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v2.config.ConfigStore import *
from pl_metrics_ops_v2.functions import *

@instrument
def src_tbl_pq_metrics_test2(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sst_ingest_ndev`.`pq_metrics_test2`")

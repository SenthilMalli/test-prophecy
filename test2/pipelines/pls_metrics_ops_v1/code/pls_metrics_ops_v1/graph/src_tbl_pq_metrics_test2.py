from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pls_metrics_ops_v1.config.ConfigStore import *
from pls_metrics_ops_v1.functions import *

@instrument
def src_tbl_pq_metrics_test2(spark: SparkSession) -> DataFrame:
    return spark.read.table("`spark_catalog`.`sst_ingest_ndev`.`pq_metrics_test2`")
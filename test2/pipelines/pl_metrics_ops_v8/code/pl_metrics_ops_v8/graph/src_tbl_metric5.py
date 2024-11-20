from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v8.config.ConfigStore import *
from pl_metrics_ops_v8.functions import *

def src_tbl_metric5(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sst_ingest_ndev`.`test_input5_observability`")

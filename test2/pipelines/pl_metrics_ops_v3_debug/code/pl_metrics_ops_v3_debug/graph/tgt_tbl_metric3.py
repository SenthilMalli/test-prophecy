from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v3_debug.config.ConfigStore import *
from pl_metrics_ops_v3_debug.functions import *

@instrument
def tgt_tbl_metric3(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("append").saveAsTable("`spark_catalog`.`sst_ingest_ndev`.`metrics_insert_test3`")
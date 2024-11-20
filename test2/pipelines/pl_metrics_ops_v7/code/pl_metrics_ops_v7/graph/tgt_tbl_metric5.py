from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v7.config.ConfigStore import *
from pl_metrics_ops_v7.functions import *

def tgt_tbl_metric5(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable("`spark_catalog`.`sst_ingest_ndev`.`test_output5_observability`")

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pls_metrics_ops_v1.config.ConfigStore import *
from pls_metrics_ops_v1.functions import *

def tgt_tbl_pq_metric_r1(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("path", "abfss://ndev@dtaeunndevadlsanalyst01.dfs.core.windows.net/ingest/sst/nonsensitive/pq_metrics_r1")\
        .mode("overwrite")\
        .saveAsTable("`spark_catalog`.`sst_ingest_ndev`.`pq_metric_r1`")

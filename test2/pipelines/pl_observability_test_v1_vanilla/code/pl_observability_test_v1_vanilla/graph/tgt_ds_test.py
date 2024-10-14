from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_observability_test_v1_vanilla.config.ConfigStore import *
from pl_observability_test_v1_vanilla.functions import *

@instrument
def tgt_ds_test(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("append").saveAsTable("`sst_ingest_ndev`.`test_output_observability`")

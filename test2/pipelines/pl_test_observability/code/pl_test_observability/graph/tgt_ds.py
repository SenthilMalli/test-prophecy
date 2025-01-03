from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_observability.config.ConfigStore import *
from pl_test_observability.functions import *

@instrument
def tgt_ds(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`sst_ingest_ndev`.`s4_ntz_test`")

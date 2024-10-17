from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_observability_test_v1_inputonly.config.ConfigStore import *
from pl_observability_test_v1_inputonly.functions import *

@instrument
def src_ds_test(spark: SparkSession) -> DataFrame:
    return spark.read.table("`sst_ingest_ndev`.`test_input_observability`")
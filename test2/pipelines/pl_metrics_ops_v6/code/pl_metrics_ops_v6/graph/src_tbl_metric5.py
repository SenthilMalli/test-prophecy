from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v6.config.ConfigStore import *
from pl_metrics_ops_v6.functions import *

@instrument
def src_tbl_metric5(spark: SparkSession) -> DataFrame:
    from prophecy.utils import synthetic_data_generator
    import json

    return synthetic_data_generator\
        .FakeDataFrame(spark, 100)\
        .addColumn(
          "col1",
          synthetic_data_generator.RandomListElements(elements = ["154565656"]),
          data_type = LongType(),
          nulls = 0
        )\
        .addColumn("col2", synthetic_data_generator.RandomEmail(), data_type = StringType(), nulls = 0)\
        .addColumn(
          "load_timestamp",
          synthetic_data_generator.RandomDateTime(
            start_datetime = "2024-01-01 11:10:10",
            end_datetime = "2024-12-20 11:10:10"
          ),
          data_type = TimestampType(),
          nulls = int(100 * (11.0 / 100))
        )\
        .build()

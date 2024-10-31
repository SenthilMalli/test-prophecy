from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_metrics_ops_v2.config.ConfigStore import *
from pl_metrics_ops_v2.functions import *

@instrument
def tgt_tbl_metric3(spark: SparkSession, in0: DataFrame):
    from pyspark.sql.utils import AnalysisException

    try:
        desc_table = spark.sql("describe formatted `spark_catalog`.`sst_ingest_ndev`.`metrics_test3`")
        table_exists = True
    except AnalysisException as e:
        table_exists = False

    if table_exists:
        from delta.tables import DeltaTable, DeltaMergeBuilder
        DeltaTable\
            .forName(spark, "`spark_catalog`.`sst_ingest_ndev`.`metrics_test3`")\
            .alias("target")\
            .merge(in0.alias("source"), (col("target.ymd") == col("source.ymd")))\
            .whenMatchedUpdate(set = {"salesamt" : col("source.salesamt")})\
            .whenNotMatchedInsertAll()\
            .execute()
    else:
        in0.write.format("delta").mode("overwrite").saveAsTable("`spark_catalog`.`sst_ingest_ndev`.`metrics_test3`")

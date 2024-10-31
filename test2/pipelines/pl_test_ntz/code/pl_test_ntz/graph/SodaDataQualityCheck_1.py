from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_test_ntz.config.ConfigStore import *
from pl_test_ntz.functions import *

def SodaDataQualityCheck_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from soda.scan import Scan
    import os
    scan = Scan()
    scan.set_scan_definition_name(None)
    import yaml
    scan.add_sodacl_yaml_str("\n")
    scan.add_configuration_yaml_str("""
                soda_cloud:
                    host: 
                    api_key_id: 
                    api_key_secret: 
                """)
    scan.execute()
    checksData = []

    for checks in scan.scan_results.get("checks"):
        checksData.append(
            (checks.get("name"), checks.get("type"), checks.get("dataSource"), checks.get("table"),
             checks.get("column"), checks.get("outcome"))
        )

    return spark.createDataFrame(
        checksData,
        schema = StructType([
          StructField("check_name", StringType(), True),
                                                        StructField("check_type", StringType(), True),
                                                        StructField("data_source", StringType(), True),
                                                        StructField("table_name", StringType(), True),
                                                        StructField("column_name", StringType(), True),
                                                        StructField("result", StringType(), True)
      ])
    )

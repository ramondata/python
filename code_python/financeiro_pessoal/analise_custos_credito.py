from pyspark.sql import SparkSession
from pyspark.sql.functions import*
from pyspark.sql.types import*

spark = SparkSession.builder.appName("app_custos").getOrCreate()

data_set = spark.read\
            .option("header", "True")\
            .option("delimiter", "\t")\
            .csv("/Users/ramon/Documents/custos.csv")\
            .select("tipo", col("valor").cast(DoubleType()))\
            .groupby("tipo")\
            .agg(sum("valor"))\
            .withColumnRenamed("sum(valor)","valor")\
            .select("tipo", round("valor", 2))\
            .withColumnRenamed("round(valor, 2)", 'valor')\
            .select("tipo", "valor")\
            .sort("valor")\
            .show(truncate=False)
from pyspark.sql import SparkSession

# إنشاء الجلسة مع تعريف مسارات الـ JDBC للـ Postgres
spark = SparkSession.builder \
    .appName("HorrorMoviesCleaning") \
    .config("spark.jars", "/tmp/spark/postgresql-42.5.0.jar") \
    .getOrCreate()

# 1. قراءة البيانات من HDFS (تحقيق شرط الـ HDFS)
# ملحوظة: بنفترض إنك رفعت الملف هناك أو بتستخدم المسار المربوط
input_path = "hdfs://namenode:9000/data/horror_movies.csv"
# لو الـ HDFS لسه مش جاهز ارفع عليه الملف الأول أو خليها /tmp/data/horror_movies.csv مؤقتاً
df = spark.read.csv("/tmp/data/horror_movies.csv", header=True, inferSchema=True)

# 2. التنظيف
cols_to_drop = ['Unnamed: 0', 'overview', 'poster_path', 'status']
df_cleaned = df.drop(*cols_to_drop).filter("title IS NOT NULL")

# 3. التحميل إلى Data Warehouse (Postgres) - تحقيق شرط الـ DWH
# بنرمي الداتا في جدول اسمه public.cleaned_horror_movies
df_cleaned.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/airflow") \
    .option("dbtable", "public.cleaned_horror_movies") \
    .option("user", "airflow") \
    .option("password", "airflow") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

print("--- Done! Data pushed to Postgres (DWH) ---")
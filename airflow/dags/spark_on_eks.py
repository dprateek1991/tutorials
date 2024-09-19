from airflow import DAG
from datetime import timedelta, datetime
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

args = {
    "owner": "prateek.dubey",
    "email": ["prateekdubey12@gmail.com"],
    "depends_on_past": False,
    "start_date": datetime(2019, 1, 1),
    "catchup": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(dag_id="spark_on_eks", default_args=args, schedule_interval=None)

spark_on_eks = KubernetesPodOperator(
        namespace='airflow',
        image='datawavelabs/spark:latest',
        image_pull_policy='Always',
        service_account_name='airflow',
        name='spark_on_eks',
        task_id='spark_on_eks',
        in_cluster=True,
        get_logs=True,
        cmds=["/opt/spark/bin/spark-submit"],
        arguments=[
                '--master', 'k8s://https://EFB9DF439C60D66475CF45513273626D.gr7.us-east-1.eks.amazonaws.com:443',
                '--deploy-mode', 'cluster',
                '--name', 'pyspark-data-analysis',
                '--conf', 'spark.kubernetes.driver.pod.name=pyspark-data-analysis',
                '--conf', 'spark.kubernetes.executor.podNamePrefix=pyspark-data-analysis',
                '--conf', 'spark.kubernetes.namespace=airflow',
                '--conf', 'spark.executor.instances=1',
                '--conf', 'spark.executor.cores=1',
                '--conf', 'spark.executor.memory=1g',
                '--conf', 'spark.kubernetes.container.image=datawavelabs/spark:latest',
                '--conf', 'spark.kubernetes.container.image.pullPolicy=Always',
                '--conf', 'spark.kubernetes.authenticate.driver.serviceAccountName=airflow',
                '--conf', 'spark.kubernetes.authenticate.executor.serviceAccountName=airflow',
                '--conf', 'spark.eventLog.enabled=false',
                'file:////opt/spark/examples/src/main/python/pi.py'
            ],
        dag=dag
    )

spark_on_eks
#!/bin/bash
sudo apt-get -y install python3-pip;
sudo python3 -m pip  install wheel;
sudo python3 -m pip install --upgrade setuptools;
sudo python3 -m pip install databricks-cli;
sudo git clone https://github.com/Prateekagarwal9/supplychain;
sudo chmod +x supplychain;
echo Celebal;
echo Celebal;
sudo databricks workspace import  -f DBC -l SCALA supplychain/ARIMA.dbc /ARIMA;
sudo databricks workspace import  -f DBC -l SCALA supplychain/Prophet.dbc /Prophet;
sudo databricks workspace import  -f DBC -l SCALA supplychain/Holt-Winter /Holt-Winter;
sudo databricks fs mkdirs dbfs:/databricks/init/$3/;
sudo databricks fs mkdirs dbfs:/databricks1/init/$3/;
sudo databricks fs cp installation.sh dbfs:/databricks/init/$3/;
sudo databricks fs cp installation1.sh dbfs:/databricks1/init/$3/;
#cluster_id=$(sudo databricks clusters create --json-file cluster_conf.json);
#cluster_id_parsed=$(echo $cluster_id | jq -r '.cluster_id');
runid=$(sudo databricks jobs create --json-file json.json);
echo $runid
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew
sudo databricks jobs run-now --job-id $runidnew;
runid=$(sudo databricks jobs create --json-file json1.json);
echo $runid
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew
sudo databricks jobs run-now --job-id $runidnew;


runid=$(sudo databricks jobs create --json-file json2.json);
echo $runid
runidnew=$(echo $runid | jq -r '.job_id');
echo $runidnew
sudo databricks jobs run-now --job-id $runidnew;
#sudo databricks libraries install --maven-coordinates "com.microsoft.azure:azure-eventhubs-spark_2.11:2.3.10" --cluster-id $runidnew

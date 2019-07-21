import sys
databricks_instance = sys.argv[1]
databricks_token = sys.argv[2]
clusters_name = "test"
template2 = {
  "name": "SparkPi Python job",
  "new_cluster": {
  	"name":clusters_name,
    "spark_version": "5.2.x-scala2.11",
    "node_type_id": "Standard_DS3_v2",
    "num_workers": 1,

    "init_scripts": [
    {
      "dbfs": {
        "destination": "dbfs:/databricks/init/"+clusters_name+"/installation.sh"
      }
    }
  ]
  },
  "notebook_task": {
    "notebook_path": "/Holt-Winter"
  }
}


template = {
  "name": "SparkPi Python job",
  "new_cluster": {
        "name":clusters_name,
    "spark_version": "5.2.x-scala2.11",
    "node_type_id": "Standard_DS3_v2",
    "num_workers": 1,

    "init_scripts": [
    {
      "dbfs": {
        "destination": "dbfs:/databricks/init/"+clusters_name+"/installation.sh"
      }
    }
  ]
  },
  "notebook_task": {
    "notebook_path": "/ARIMA"
  }
}


template1 = {
  "name": "SparkPi Python job",
  "new_cluster": {
  	"name":clusters_name,
    "spark_version": "5.4.x-conda-scala2.11",
    "node_type_id": "Standard_DS3_v2",
    "num_workers": 1,
    "init_scripts": [
    {
      "dbfs": {
        "destination": "dbfs:/databricks1/init/"+clusters_name+"/installation1.sh"
      }
    }
  ]
  },
  "notebook_task": {
    "notebook_path": "/Prophet"
  }
}

print(databricks_instance, databricks_token)
import json
import subprocess

with open('json.json', 'w') as fp:
    json.dump(template, fp)

with open('json2.json', 'w') as fp:
    json.dump(template2, fp)

with open('json1.json', 'w') as fp:
    json.dump(template1, fp)

subprocess.call(['prtkshell.bat',databricks_instance,databricks_token,clusters_name])

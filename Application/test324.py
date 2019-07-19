'''from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials

def auth_callback(server, resource, scope):
    credentials = ServicePrincipalCredentials(
        client_id = '412070f3-2925-4dcf-9979-b3389693b8c7',
        secret = '?LoxbfI/1xD6VQEDa65tabIjcrjYR*p]',
        tenant = '7e3e1374-888b-45e9-9a4a-bf7b5d109f16',
        resource = "https://vault.azure.net"
    )
    token = credentials.token
    return token['token_type'], token['access_token']

client = KeyVaultClient(KeyVaultAuthentication(auth_callback))
print(client)

VAULT_URL = "https://test324.vault.azure.net/"
secret_bundle = client.get_secret(VAULT_URL, "akey","")
secret_bundle1 = client.get_secret(VAULT_URL, "test324","")
print(secret_bundle.value)
print(secret_bundle1.value)'''
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

subprocess.call(['bash','main.sh',databricks_instance,databricks_token,clusters_name])

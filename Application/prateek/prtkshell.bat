ECHO OFF
python -m pip install --upgrade pip --user
python -m pip install databricks-cli --user
python -m pip install pexpect --user
cp d:/local/appdata/python/python36/scripts/databricks.exe .
cp d:/local/appdata/python/python36/scripts/dbfs.exe .
git clone https://github.com/Prateekagarwal9/supplychain
python expect.py %1 %2
databricks workspace import  -f DBC -l SCALA supplychain/ARIMA.dbc /ARIMA
databricks workspace import  -f DBC -l SCALA supplychain/Prophet.dbc /Prophet
databricks workspace import  -f DBC -l SCALA supplychain/Holt-Winter /Holt-Winter
rmdir /q /s supplychain
databricks fs mkdirs dbfs:/databricks/init/%3/
databricks fs mkdirs dbfs:/databricks1/init/%3/
databricks fs cp installation.sh dbfs:/databricks/init/%3/
databricks fs cp installation1.sh dbfs:/databricks1/init/%3/
ECHO OFF
databricks jobs create --json-file json.json > runid.json
jq-win64.exe ".job_id" runid.json > runidnew.txt
set /p runidnew= < runidnew.txt
databricks jobs run-now --job-id %runidnew%
databricks jobs create --json-file json1.json > runid.json
jq-win64.exe ".job_id" runid.json > runidnew.txt
set /p runidnew= < runidnew.txt
databricks jobs run-now --job-id %runidnew%
databricks jobs create --json-file json2.json > runid.json
jq-win64.exe ".job_id" runid.json > runidnew.txt
set /p runidnew= < runidnew.txt
databricks jobs run-now --job-id %runidnew%

curl -X POST "<your-endpoint>/text/analytics/v3.1/languages?" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: <your-key>" --data-ascii "{'documents':           [{'id':1,'text':'hello'}]}"

#Tests total number of requests metric
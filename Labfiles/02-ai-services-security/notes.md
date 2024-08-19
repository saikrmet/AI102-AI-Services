# Service Principals

## How to create a Service Principal and connect it Key Vault

1. Create resource and key vault resource
2. Add resource key to key vault secrets
3. After using CLI to login, create service principal using:

```
 az ad sp create-for-rbac -n "api://<spName>" --role owner --scopes subscriptions/<subscriptionId>/resourceGroups/<resourceGroup>
 ```

 4. Save tenantID, appID, and appPassword
 5. Get service principal object ID using: 

 ```
 az ad sp show --id <appId>
 ```

 6. Connect service principal to key vault resource using: 

 ```
 az keyvault set-policy -n <keyVaultName> --object-id <objectId> --secret-permissions get list
 ```

 7. In code, create ClientSecretCredential (service principal) and pass it to SecretClient, 
 which takes a URI and service principal
 8. Use methods on SecretClient to access key value
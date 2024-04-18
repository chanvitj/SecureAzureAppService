# SecureAzureAppService
This is for demo how to secure Azure App Service.
Source code here is just sample source code of multi-tier application.

## Create Resource Group and VNET  

## Use VSCode connects to Azure and Deploy Web

## Use VSCode connects to Azure and Deploy App

## Create CosmosDB  
Create Cosmos DB for MongoDB
Select RU
Select Resource Group
Select AZ=Disable
Select Location
Select Capacity mode=Provisioned throughput
Review+Create
Get Connection String

Use MongoDB Shell
Enter Connection String
Enter the following commands
```
use jewdatabase
db.createCollection(“jewdemocollection”)
db.jewdemocollection.insertMany([  
  {
    product: "FortiGate", 
    qty: 38
  },
  {
    product: "FortiWeb",
    qty: 20
  }
])
```

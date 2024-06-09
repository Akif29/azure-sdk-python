from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters, Sku, Kind

# Set up your subscription ID
subscription_id = 'd654f2b3-4ca9-42bd-896f-7c5afa0c837c'

# Define the resource group and storage account names
resource_group_name = 'testgroup'
storage_account_name = 'teststorage5170'
location = 'UAE North'

# Authenticate with Azure
credential = DefaultAzureCredential()

# Initialize the resource management client
resource_client = ResourceManagementClient(credential, subscription_id)

# Create the resource group
resource_group_params = {'location': 'UAE North'}
resource_client.resource_groups.create_or_update(resource_group_name, resource_group_params)

# Initialize the storage management client
storage_client = StorageManagementClient(credential, subscription_id)

# Define the storage account parameters
storage_account_params = StorageAccountCreateParameters(
    sku=Sku(name='Standard_LRS'),
    kind=Kind.BLOB_STORAGE,
    location=location,
    access_tier='Hot'
)

# Create the storage account
async_storage_creation = storage_client.storage_accounts.begin_create(
    resource_group_name,
    storage_account_name,
    storage_account_params
)
storage_account = async_storage_creation.result()

print(f'Storage account {storage_account_name} created successfully in resource group {resource_group_name}')

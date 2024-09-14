# Create Resource Group
module "resource_group" {
  source              = "../modules/resourcegroup"
  resource_group_name = "temustutorial"
}

# Create Storage Accounts
module "storage_account" {
  source                   = "../modules/storage"
  storage_account_name     = "temussatutorial"
  resource_group_name      = "temustutorial"
  containers               = ["test"]
}
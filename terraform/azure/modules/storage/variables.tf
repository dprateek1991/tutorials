variable "storage_account_name" {
  type        = string
  description = "Storage Account name"
}

variable "resource_group_name" {
  type        = string
  description = "Resource Group name"
}

variable "location" {
  type        = string
  default     = "Southeast Asia"
  description = "Location of resources"
}

variable "account_tier" {
  type        = string
  default     = "Standard"
  description = "Storage Account tier type"
}

variable "account_replication_type" {
  type        = string
  default     = "LRS"
  description = "Storage Account replication strategy"
}

variable "account_kind" {
  type        = string
  default     = "StorageV2"
  description = "Storage Account kind"
}

variable "containers" {
  type        = list
  description = "Storage Account Containers"
}

variable "is_hns_enabled" {
  type        = bool
  default     = true
  description = "ADLS Gen2 Storage Account - Hierarchial Namespace Enabled"
}
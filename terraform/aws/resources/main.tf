module "s3" {
  source        = "../modules/s3"
  bucket_name   = "temus-s3-tutorial"
  aws_region    = var.aws_region
  acl           = "private"
}

module "s3_1" {
  source        = "../modules/s3"
  bucket_name   = "temus-s3-tutorial-public"
  aws_region    = var.aws_region
  acl           = "public-read"
}
module "s3" {
  source        = "../modules/s3"
  bucket_name   = "temus_s3_tutorial"
  aws_region    = var.aws_region
}
provider "aws" {
    profile = "arthur"
    region = "us-east-1"
}

terraform {
    backend "s3" {
        profile        = "arthur"
        bucket         = "eco-mercy-data"
        key            = "terraform/terraform.tfstate"
        encrypt        = true
        region         = "us-east-1"
    }
}

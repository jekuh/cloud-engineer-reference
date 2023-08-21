terraform {
  required_version = "1.5.3"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.8.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.4.3"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}

# Create DynamoDB table
resource "aws_dynamodb_table" "account_access" {
  name           = "oe_account_access"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "account_id"
  range_key      = "date"

  # Existing attributes

  attribute {
    name = "account_id"
    type = "S"
  }
  attribute {
    name = "date"
    type = "S"
  }
  attribute {
    name = "role"
    type = "S"
  }
  attribute {
    name = "user"
    type = "S"
  }
  attribute {
    name = "type"
    type = "S"
  }

  # Point-in-time recovery and server-side encryption configurations

  point_in_time_recovery {
    enabled = true
  }
  
  server_side_encryption {
    enabled = true
  }

  tags = {
    Name = "Account Access Table"
  }

  # New global secondary index configuration

  global_secondary_index {
    name               = "gsi_role_user"
    hash_key           = "role"
    range_key          = "user"
    projection_type    = "ALL"

    non_key_attributes = []
  }
}


# Create lambda function (oe_account_access)
resource "aws_lambda_function" "oe_account_access" {
  function_name    = "account_access"
  role             = aws_iam_role.oe_account_access_role.arn
  runtime          = "python3.9"
  handler          = "account_access.lambda_handler"
  filename         = "account_access.zip"
  source           = ("account_access.zip")
  timeout          = 300
  memory_size      = 256

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.account_access.name
    }
  }
}


# Create role for basic lambda function execution (oe_account_access_role)
resource "aws_iam_role" "oe_account_access_role" {
  name = "oe_account_access_role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

# Attach AWSLambdaBasicExecutionRole policy to the lambda function role
resource "aws_iam_role_policy_attachment" "oe_account_access_policy_attachment" {
  role       = aws_iam_role.oe_account_access_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}


# Create policy for lambda DynamoDB access (oe_account_access_policy)
resource "aws_iam_policy" "oe_account_access_policy" {
  name        = "oe_account_access_policy"
  description = "Allows access to DynamoDB table for oe_account_access lambda function"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:DeleteItem",
        "dynamodb:UpdateItem",
        "dynamodb:BatchGetItem",
        "dynamodb:BatchWriteItem"
      ],
      "Resource": "arn:aws:dynamodb:*:*:table/${aws_dynamodb_table.account_access.name}"
    }
  ]
}
EOF
}

# Attach the DynamoDB access policy to the lambda function role
resource "aws_iam_role_policy_attachment" "oe_account_access_dynamodb_policy_attachment" {
  role       = aws_iam_role.oe_account_access_role.name
  policy_arn = aws_iam_policy.oe_account_access_policy.arn
}


// module
module "account_access" {
  source = "./modules/account_access"
}
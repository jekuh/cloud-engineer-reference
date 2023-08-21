Task 1:  Account Access  Monitoring - ..


module.athena4cloudtrail
    Lambda: 
        account_access: s3 to dynamodb 
        add S3 policy for cross account access
        test, commit, pull request 

    eventBridge: Daily execution rule
    execute_athena_query: s3 to s3
    test, deploy and update 

    S3: 

module.accord 
Dynamodb:  
    add GSI

SNS: 
    analyse account access details stored in dynamodb and send weekly report on account access security and compliance.


Daily Start - Task Specific Commands  : Make small commits daily and avoid resolving large merge conflicts.

pipenv install 
git checkout dev
git pull
git status 
git add/rm
git commit


terraform init   -var-file="env_config/org_test/test.tfvars" -target=module.account_access

terraform init   -var-file="env_config/org_test/test.tfvars" -target=module.account_access

terraform apply   -var-file="env_config/org_test/test.tfvars" -target=module.accord.aws_dynamodb_table.account_access

terraform destroy -var-file="env_config/org_test/test.tfvars" -target=module.accord.aws_dynamodb_table.account_access

## Dev ()  (accord_account_id = "946732835423") : login to console using manager role.


using python lambda, provide step by step on how to copy cloud trail log from athena query from s3 to s3 

athena query ID : 1035a238-ff88-4d48-adcb-2c4fadd89c2a
athena query name: 	getassumedroles_from_yesterday

source: https://aws-athena-query-results-244717564362-eu-central-1.s3.eu-central-1.amazonaws.com/Unsaved/2023/08/02/5161104c-08e2-4785-af99-b93e05028be7.csv

Target: arn:aws:s3:::athena4cloudtrail-result



no need to hard coding query, call query id/name instead.


Run following athena saved query using python lambda on aws:

athena query ID : 1035a238-ff88-4d48-adcb-2c4fadd89c2a
athena query name: 	getassumedroles_from_yesterday

copy results from athena query to a new s3 

source: https://aws-athena-query-results-244717564362-eu-central-1.s3.eu-central-1.amazonaws.com/Unsaved/2023/08/02/5161104c-08e2-4785-af99-b93e05028be7.csv
Target: arn:aws:s3:::athena4cloudtrail-result


git diff
git add -A
git commit -m "feature/ATT-130-OU: Create module to deploy Orgs"

git push --set-upstream origin feature/SCO-119-account-acces-monitoring-athena-cloudtrail

aws codecommit create-pull-request \
  --title "feature/SCO-119-account-acces-monitoring-athena-cloudtrail" \
  --description "lambda account access and execute athena query" \
  --client-request-token feature/SCO-119-account-acces-monitoring-athena-cloudtrail \
  --targets repositoryName=terraform-cloud-management-ec1,sourceReference=feature/SCO-119-account-acces-monitoring-athena-cloudtrail,destinationReference=dev      


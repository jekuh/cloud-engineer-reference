Task 1:  Account Access  Monitoring : account_access
module
    athena4cloudtrail
        S3
        Lambda: 

    accord 
        Dynamodb:  

    avm
      aom-update-test

Daily: Make a small change and commit 

pipenv shell 
git pull
pipenv install

git status 
git add
git commit
git push

pre test before push 

terraform init   -var-file="env_config/org_test/test.tfvars" -target=module.accord

terraform apply   -var-file="env_config/org_test/test.tfvars" -target=module.accord

terraform apply   -var-file="env_config/org_test/test.tfvars" -target=module.athena4cloudtrail

terraform apply   -var-file="env_config/org_test/test.tfvars" -target=module.accord.aws_dynamodb_table.account_access

terraform destroy -var-file="env_config/org_test/test.tfvars" -target=module.accord.aws_dynamodb_table.account_access

terraform apply   -var-file="env_config/org_test/test.tfvars" -target=module.avm.lambda_check_update

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

Weekly - Create new pull request 
git diff
git add -A
git commit -m "feature/ATT-130-OU: Create module to deploy Orgs"

git push --set-upstream origin feature/SCO-119-account-acces-monitoring-athena-cloudtrail

aws codecommit create-pull-request \
  --title "feature/SCO-119-account-acces-monitoring-athena-cloudtrail" \
  --description "lambda account access and execute athena query" \
  --client-request-token feature/SCO-119-account-acces-monitoring-athena-cloudtrail \
  --targets repositoryName=terraform-cloud-management-ec1,sourceReference=feature/SCO-119-account-acces-monitoring-athena-cloudtrail,destinationReference=dev      


Task 2:  CICD Pipeline Athena4cloudtrail : account_access
code: 

error: 

Fair offer: 

1. Screen : 250

https://www.digitec.ch/de/s1/product/lg-ultrawide-34wp500-b-2560-x-1080-pixel-3410-monitor-22726045?utm_source=google&utm_medium=cpc&campaignid=20501673545&adgroupid=&adid=&dgCidg=CjwKCAjwvfmoBhAwEiwAG2tqzHLUoA1hegdQE_eYBm-bB8ZcdGMNwpfY4X7UB9xled3HTaN_PjoBwRoCrZ0QAvD_BwE&gclid=CjwKCAjwvfmoBhAwEiwAG2tqzHLUoA1hegdQE_eYBm-bB8ZcdGMNwpfY4X7UB9xled3HTaN_PjoBwRoCrZ0QAvD_BwE&gclsrc=aw.ds

2. Table : 

https://ergofino.eu/collections/schreibtisch/products/ergofino-dt30-hoehenverstellbarer-schreibtisch-dualer-motor-schwarz





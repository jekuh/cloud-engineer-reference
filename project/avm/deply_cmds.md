
tfinit   -var-file="env_config/org_test/test.tfvars" -target=module.avm
 
tfdestroy   -var-file="env_config/org_test/test.tfvars" -target=module.avm.aws_sfn_state_machine.aom_update_sfn -target=module.avm.module.lambda_check_order_update_type  -target=module.avm.module.aom_update_sfn_role
tfapply   -var-file="env_config/org_test/test.tfvars" -target=module.avm.module.lambda_check_order_update_type
tfapply   -var-file="env_config/org_test/test.tfvars" -target=module.avm.module.aom_update_sfn_role

tfapply   -var-file="env_config/org_test/test.tfvars" -target=module.avm.aws_sfn_state_machine.aom_update_sfn

tfdestroy   -var-file="env_config/org_test/test.tfvars" -target=module.avm.aws_sfn_state_machine.aom_update_sfn
tfdestroy   -var-file="env_config/org_test/test.tfvars" -target=module.avm.module.lambda_check_order_update_type
tfdestroy   -var-file="env_config/org_test/test.tfvars" -target=module.avm.module.aom_update_sfn_role



old changes to 

AWSReservedSSO_oe_devops_23cf6a8d2c77e560:~/environment/terraform-cloud-management-ec1 (feature/ATT-1416-aom-tag-update) $ git diff   modules/terraform-module-avm-ec1/aom_update_lambdas.tf
--- a/modules/terraform-module-avm-ec1/aom_update_lambdas.tf
+++ b/modules/terraform-module-avm-ec1/aom_update_lambdas.tf


  (use "git restore <file>..." to discard changes in working directory)
        modified:   modules/terraform-module-avm-ec1/aom_update_lambdas.tf
        modified:   modules/terraform-module-avm-ec1/aom_update_sfn.tf
        modified:   modules/terraform-module-avm-ec1/lambdas/check_order_update_type/src/check_order_update_type.py
        modified:   modules/terraform-module-avm-ec1/lambdas/check_order_update_type/src/parameters.py


git checkout -b feature/ATT-1446-update-order-type-choice-state

git checkout -b feature/ATT-1442-check-order-update-type-test


new task

order update file update: update oder file based on input from update cases.







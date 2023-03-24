Based off of https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html

* You will want a VPC with a public subnet
* Create a Security Group with the necessary ingress permissions (allowing everything ingress and egress is an option)


Uses the default cluster

`aws ecs register-task-definition --cli-input-json file://setup-nmap-scan-target-practice_aws-ec2-task-definition.json`


Notate the task definition name:rev pair
`aws ecs list-task-definitions`


Provide the appropriate subnet and sg IDs
```
aws ecs create-service --service-name nmap-scan-target-practice-service \
     --task-definition nmap-scan-target-practice:PROVIDE_REVISION_NUMBER_HERE \
     --desired-count 1 --launch-type "FARGATE" \
     --network-configuration "awsvpcConfiguration={subnets=[subnet-INSERT],securityGroups=[sg-INSERT],assignPublicIp=ENABLED}"


aws ecs list-services

aws ecs describe-services --services nmap-scan-target-practice-service

aws ecs list-tasks --service nmap-scan-target-practice-service
```

Provide the ARN of your task here
```
aws ecs describe-tasks --tasks arn:aws:ecs:us-west-2:############:task/INSERT/HERE
aws ecs describe-tasks --tasks arn:aws:ecs:us-west-2:############:task/INSERT/HERE | grep 'eni-'
```

Get the public IP address of the container instance
```
aws ec2 describe-network-interfaces --network-interface-id  eni-INSERT_HERE
aws ec2 describe-network-interfaces --network-interface-id  eni-INSERT_HERE | grep PublicDnsName
```

Alternative method of IP address collection
```
aws ec2 describe-network-interfaces --output text --query 'NetworkInterfaces[].[Association.PublicIp,Ipv6Addresses]' | grep -v None
```

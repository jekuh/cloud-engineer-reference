resource "aws_instance" "ec2_dev" {
  ami = "ami-0c4c4bd6cf0c5fe52"
  instance_type = "t2.micro"
}
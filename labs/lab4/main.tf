variable "create_vpc" {
 type    = bool
 default = true
}

variable "create_ec2" {
 type    = bool
 default = true
}
variable "myname" {
  
}

resource "aws_vpc" "custom_vpc" {
 count = var.create_vpc ? 1 : 0

 cidr_block = "10.0.0.0/16"
 enable_dns_hostnames =true
 enable_dns_support = true
 tags = {
   Name = "Or-vpc"
 }
}


resource "aws_instance" "example" {
 count = var.create_ec2 ? 1 : 0
 # please ENABLE THE a public ip FOR THE machine WHEN USING CUSTOM VPC (USE GOOGLE INSTEAD OF CHATGPT)

 ami           = "ami-0ecc0e0d5986a576d" # Ubuntu AMI
 instance_type = "t2.micro"

 subnet_id = var.create_vpc ? aws_subnet.custom_subnet[0].id : data.aws_subnet.default.id

 associate_public_ip_address = var.create_vpc ? true : false
 tags = {
   Name = "Or-ec2"
 }
 # Make sure that if i'm using a deafult vpc ... this wont cause an issue ...
 //depends_on = [aws_vpc.custom_vpc]

lifecycle {
  ignore_changes = [ subnet_id ]
}

}


resource "aws_subnet" "custom_subnet" {
 count = var.create_vpc ? 1 : 0

 vpc_id            = aws_vpc.custom_vpc[0].id
 cidr_block        = "10.0.1.0/24"
 map_public_ip_on_launch = true

 tags = {
   Name = "Or-subnet"
 }
}

data "aws_availability_zones" "available" {}
resource "random_shuffle" "az" {
  input        = data.aws_availability_zones.available.names
  result_count = 1
}

data "aws_subnet" "default" {
    vpc_id = data.aws_vpc.default.id

 filter {
   name   = "default-for-az"
   
   values = ["true"]
 }
  filter {
    name   = "availability-zone"
    values = [random_shuffle.az.result[0]]  # Use the randomly selected AZ
  }
}



data "aws_vpc" "default" {
  default = true
}




# OUTPUTS : please print to machine ip and [vpcid + subnetid] using the following "The following is your {VPCID} and {SUBNET}"
output "vm_public_ip" {
  value       = aws_instance.example[0].public_ip
  description = "Public IP address of the EC2 instance"
}

output "vpc_and_subnet" {
  value       = "The following is your VPC ID: ${var.create_vpc ? aws_vpc.custom_vpc[0].id : "default VPC"} and Subnet ID: ${var.create_vpc ? aws_subnet.custom_subnet[0].id : data.aws_subnet.default.id}"
  description = "VPC and Subnet information"
}

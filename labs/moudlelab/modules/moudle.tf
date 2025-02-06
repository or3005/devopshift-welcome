module "outputmodle" {
  source = "/home/ubuntu/workarea/jb/labs"
  ami_id             = "ami-0c02fb55956c7d316"
  instance_type    = "t2.micro"
    machine-name = "or-vm"
   ingress_port = 22
   ingress_protocol = "tcp"
    outgress_port = 0
    outgress_protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
}


output "print_outputmodle_info" {
    value = module.outputmodle
}


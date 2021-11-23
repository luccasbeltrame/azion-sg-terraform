resource "aws_security_group" "border_azion" {
  name        = "allow_tls_from_azion"
  description = "Allow TLS inbound traffic from azion Ips"
  vpc_id      = var.vpc_id

  ingress {
    description = "TLS from Azion"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = var.items_values
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_tls"
  }
}

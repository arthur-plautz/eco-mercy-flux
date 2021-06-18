resource "aws_db_instance" "eco_mercy" {
  identifier           = "eco-mercy"
  allocated_storage    = 10
  engine               = "postgres"
  engine_version       = "11.9"
  instance_class       = "db.t2.micro"
  name                 = "eco_mercy"
  username             = var.eco_mercy_db_user
  password             = var.eco_mercy_db_pass
  skip_final_snapshot  = true
  publicly_accessible  = true
  apply_immediately    = true
}
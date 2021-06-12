resource "aws_db_instance" "eco_mercy" {
  identifier           = "eco-mercy"
  allocated_storage    = 10
  engine               = "postgres"
  engine_version       = "11.9"
  instance_class       = "db.t2.micro"
  name                 = "eco_mercy"
  username             = "kevin"
  password             = "heykevin"
  skip_final_snapshot  = true
}
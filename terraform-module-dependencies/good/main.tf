module "bonjour" {
  source = "./print_string"

  string = "Bonjour "
}

module "synograph" {
  source = "./print_string"

  string = "Synograph "

  dependency = join(",", [module.bonjour.complete)
}

module "sourire" {
  source = "./print_string"

  string = ":D\n"

  dependency = join(",", [module.synograph.complete])
}

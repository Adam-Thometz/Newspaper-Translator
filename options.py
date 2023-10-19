# Egypt - Daily News Egypt
# Spain - El Pais
# France - Le Monde

# {
#     "country name": ("url", "classname for thing you want to scrape")
# }

country_newspapers = {
    "Egypt": ("https://www.dailynewsegypt.com/", ".p-url"),
	"Spain": ("https://elpais.com", ".c_t"),
	"France": ("https://www.lemonde.fr", ".article__title-label"),
}
import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/samsung/celular_NoIndex_True#applied_filter_id%3DBRAND%26applied_filter_name%3DMarca%26applied_filter_order%3D3%26applied_value_id%3D206%26applied_value_name%3DSamsung%26applied_value_order%3D2%26applied_value_results%3D952%26is_custom%3Dfalse"]

    def parse(self, response):
        pass

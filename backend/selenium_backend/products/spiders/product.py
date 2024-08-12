import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from products.items import ScrapedDataItem
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from pro_scrape.models import ScrapedData

class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = [
        "www.target.com", "www.bestbuy.ca", "www.newegg.com", "www.aliexpress.com", "www.logitechg.com",
        "cartco.pk", "www.walmart.ca", "www.daraz.pk", "www.ebay.com", "www.amazon.com", "www.bestbuy.com"
        "www.walmart.com", "www.asos.com", "www.banggood.com", "www.daraz.pk", "zahcomputers.pk", "globalcomputers.pk", "www.czone.com.pk", "www.tejar.pk",
        "elitegamingstore.pk", "logiguru.pk", "www.olx.com.pk", "www.technoo.pk", "www.carrefour.pk", "qne.com.pk", "greenvalley.pk", "www.junaidtech.pk", "alhamdtech.pk",
        "discountstore.pk", "www.bose.com", "vintagetrimmer.pk", "shopyard.pk", "onlymart.pk", "jerrysmart.pk", "daling.pk", "www.minemart.pk", "dakaan.pk", "priceoye.pk",
        "abmmart.pk", "heygirl.pk", "hnbstore.pk", "tagofashion.com.pk", "shopatshams.com.pk", "highstreetpakistan.com", "hudabeauty.com", "www.gtstore.pk",
        "www.myvitaminstore.pk", "grocerapp.pk", "direct.playstation.com", "generations.com.pk", "www.venturegames.com.pk", "www.starshop.pk", "www.tjmart.pk",
        "www.ubuy.com.pk", "www.paklap.pk", "vmart.pk", "www.kitchenmate.pk", "bryon.com.pk", "www.kitchenaid.com", "www.stationerystation.pk", "paperclip.pk", "waqarmart.pk",
        "katib.pk", "shahalami.pk", "copypencil.pk", "school2office.com", "techmatched.pk", "www.redragonpakistan.pk", "redragonzone.pk", "playtech.pk"

    ]

    def __init__(self, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        # Extracting URLs from command line arguments
        self.urls_to_parse = kwargs.get('urls', '').split(',')

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_requests(self):
        # Start scraping the provided URLs
        for url in self.urls_to_parse:
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url  
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        
        domain = urlparse(response.url).hostname
        if domain:
            if domain.startswith("www.newegg.com"):
                return self.parse_newegg(response)
            elif domain.startswith("www.aliexpress.com"):
                return self.parse_aliexpress(response)
            elif domain.startswith("cartco.pk"):
                return self.parse_cartco(response)
            elif domain.startswith("www.bestbuy.ca"):
                return self.parse_bestbuyca(response)
            elif domain.startswith("www.bestbuy.com"):
                return self.parse_bestbuycom(response)
            elif domain.startswith("www.target.com"):
                return self.parse_target(response)
            elif domain.startswith("www.walmart.ca"):
                return self.parse_walmart(response)
            elif domain.startswith("www.amazon.com"):
                return self.parse_amazon(response)
            elif domain.startswith("www.ebay.com"):
                return self.parse_ebay(response)
            elif domain.startswith("dakaan.pk"):
                return self.parse_dakaan(response)
            elif domain.startswith("priceoye.pk"):
                return self.parse_priceoye(response)
            elif domain.startswith("vintagetrimmer.pk"):
                return self.parse_vintagetrimmer(response)
            elif domain.startswith("shopyard.pk"):
                return self.parse_shopyard(response)
            elif domain.startswith("onlymart.pk"):
                return self.parse_onlymart(response)
            elif domain.startswith("jerrysmart.pk"):
                return self.parse_jerrysmart(response)
            elif domain.startswith("daling.pk"):
                return self.parse_daling(response)
            elif domain.startswith("www.minemart.pk"):
                return self.parse_minemart(response)
            elif domain.startswith("zahcomputers.pk"):
                return self.parse_zahcomputers(response)
            elif domain.startswith("globalcomputers.pk"):
                return self.parse_globalcomputers(response)
            elif domain.startswith("www.czone.com.pk"):
                return self.parse_czone(response)
            elif domain.startswith("elitegamingstore.pk"):
                return self.parse_elitegamingstore(response)
            elif domain.startswith("logiguru.pk"):
                return self.parse_logiguru(response)
            elif domain.startswith("www.olx.com.pk"):
                return self.parse_olx(response)
            elif domain.startswith("www.technoo.pk"):
                return self.parse_technoo(response)
            elif domain.startswith("www.gtstore.pk"):
                return self.parse_gtstore(response)
            elif domain.startswith("www.junaidtech.pk"):
                return self.parse_junaidtech(response)
            elif domain.startswith("www.logitechg.com"):
                return self.parse_logitechg(response)
            elif domain.startswith("www.tejar.pk"):
                return self.parse_tejar(response)
            elif domain.startswith("alhamdtech.pk"):
                return self.parse_alhamdtech(response)
            elif domain.startswith("discountstore.pk"):
                return self.parse_discountstore(response)
            elif domain.startswith("www.bose.com"):
                return self.parse_bose(response)
            elif domain.startswith("www.carrefour.pk"):
                return self.parse_carrefour(response)
            elif domain.startswith("qne.com.pk"):
                return self.parse_qne(response)
            elif domain.startswith("greenvalley.pk"):
                return self.parse_greenvalley(response)
            elif domain.startswith("www.daraz.pk"):
                return self.parse_daraz(response)
            elif domain.startswith("abmmart.pk"):
                return self.parse_abmmart(response)
            elif domain.startswith("heygirl.pk"):
                return self.parse_heygirl(response)
            elif domain.startswith("hnbstore.pk"):
                return self.parse_hnbstore(response)
            elif domain.startswith("tagofashion.com.pk"):
                return self.parse_tagofashion(response)
            elif domain.startswith("shopatshams.com.pk"):
                return self.parse_shopatshams(response)
            elif domain.startswith("highstreetpakistan.com"):
                return self.parse_highstreetpakistan(response)
            elif domain.startswith("hudabeauty.com"):
                return self.parse_hudabeauty(response)
            elif domain.startswith("www.myvitaminstore.pk"):
                return self.parse_myvitaminstore(response)
            elif domain.startswith("grocerapp.pk"):
                return self.parse_grocerapp(response)
            elif domain.startswith("direct.playstation.com"):
                return self.parse_playstation(response)
            elif domain.startswith("generations.com.pk"):
                return self.parse_generations(response)
            elif domain.startswith("www.venturegames.com.pk"):
                return self.parse_venturegames(response)
            elif domain.startswith("www.starshop.pk"):
                return self.parse_starshop(response)
            elif domain.startswith("www.tjmart.pk"):
                return self.parse_tjmart(response)
            elif domain.startswith("www.ubuy.com.pk"):
                return self.parse_ubuy(response)
            elif domain.startswith("www.paklap.pk"):
                return self.parse_paklap(response)
            elif domain.startswith("www.kitchenmate.pk"):
                return self.parse_kitchenmate(response)
            elif domain.startswith("bryon.com.pk"):
                return self.parse_bryon(response)
            elif domain.startswith("www.kitchenaid.com"):
                return self.parse_kitchenaid(response)
            elif domain.startswith("www.stationerystation.pk"):
                return self.parse_stationerystation(response)
            elif domain.startswith("paperclip.pk"):
                return self.parse_paperclip(response)
            elif domain.startswith("waqarmart.pk"):
                return self.parse_waqarmart(response)
            elif domain.startswith("katib.pk"):
                return self.parse_katib(response)
            elif domain.startswith("shahalami.pk"):
                return self.parse_shahalami(response)
            elif domain.startswith("copypencil.pk"):
                return self.parse_copypencil(response)
            elif domain.startswith("school2office.com"):
                return self.parse_school2office(response)
            elif domain.startswith("techmatched.pk"):
                return self.parse_techmatched(response)
            elif domain.startswith("www.redragonpakistan.pk"):
                return self.parse_redragonpakistan(response)
            elif domain.startswith("redragonzone.pk"):
                return self.parse_redragonzone(response)
            elif domain.startswith("playtech.pk"):
                return self.parse_playtech(response)
                
    def parse_playtech(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()

        # Extract title
        title = sel.css("h1.product-title::text").get()
        item['title'] = title.strip() if title else "Title not found"

        # Extract current price
        current_price = sel.css(".price-wrapper p.price ins span.woocommerce-Price-amount bdi::text").get()
        item['price'] = f"₨{current_price.strip()}" if current_price else "Price Not Found"

        item['link'] = response.url

        yield item

    def parse_redragonpakistan(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()

        # Extract title
        title = sel.css("h1.product-meta__title::text").get()
        item['title'] = title.strip() if title else "Title not found"

        # Extract price
        price = sel.css("div.price-list span.price::text").get()
        item['price'] = price.strip() if price else "Price Not Found"

        item['link'] = response.url

        yield item

    def parse_redragonzone(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()

        # Extract title
        title = sel.css("h1.page-heading::text").get()
        item['title'] = title.strip() if title else "Title not found"

        # Extract price
        sale_price = sel.css(".product-price div.detail-price span.price::text").get()
        item['price'] = sale_price.strip() if sale_price else "Price Not Found"

        item['link'] = response.url

        yield item
    
    def parse_techmatched(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()

        # Extract title
        title = sel.css("h1.product_title::text").get()
        item['title'] = title.strip() if title else "Title not found"

        # Extract price
        price = sel.css("p.price span.woocommerce-Price-amount bdi::text").get()
        item['price'] = f"₨{price.strip()}" if price else "Price Not Found"

        item['link'] = response.url

        yield item

    def parse_stationerystation(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to stationerystation.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h1.product-title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        current_price = sel.css("span#spnCurrentPrice::text").get()
        old_price = sel.css("span#spnOldPrice::text").get()
        price = f"Rs. {current_price.strip()}" if current_price else "Price Not Found"
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_paperclip(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to paperclip.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h2.pdp-mod-section-title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("p.price span.woocommerce-Price-amount bdi::text").get()
        price = f"₨{price_element.strip()}" if price_element else "Price Not Found"
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_waqarmart(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to waqarmart.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h1.mb-2.fs-20.fw-600::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("div.col-sm-10 strong.text-primary::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_copypencil(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to copypencil.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h1.product-title span::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("div.prices span.price::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_school2office(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to school2office.com
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h1.productView-title a::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("div.price__sale .price-item--sale::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_katib(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to katib.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h1.product-single__title span#truncatedTitle::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("span.product-single__price::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_shahalami(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to shahalami.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("div.product-page-info__title h1::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("div.product-page-info__price span.price span::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        item['price'] = price
        
        item['link'] = response.url
        
        yield item


    def parse_kitchenaid(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to kitchenaid.com
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h1.product-name span.product-title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("p.sale-price::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item


    def parse_bryon(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to bryon.com.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("div.SellTemperature h1.ClayDistance::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("div.BonePaint::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item


    def parse_kitchenmate(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to kitchenmate.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("div.QfrfFD h1[data-hook='product-title']::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("div.hM4gpp span[data-hook='formatted-primary-price']::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_paklap(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to paklap.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h1.page-title span.base::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("div.product-info-price span.price-container span.price-wrapper span.price::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_vmart(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to vmart.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h1.product-title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("p.price span.amount::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_ubuy(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to ubuy.com.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h1[itemprop='name']::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("h2.font-bold span::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_tjmart(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to tjmart.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("div.slider_bottomside h1::attr(producttitle)").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("div.p-price-page::text").get()
        
        if price_element:
            price = price_element.strip().split()[1]  # Extracting the price part only
        else:
            price = "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item           
                
    def parse_starshop(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to starshop.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("div.product-single-info h1::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css("span.price::text").get()
        
        if price_element:
            price = price_element.strip().split()[1]  # Extracting the price part only
        else:
            price = "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item

    def parse_venturegames(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to venturegames.com.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("h2.h1::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css(".price.price--large.product-price-current::attr(data-price)").get()
        
        if price_element:
            price = price_element.strip()
        else:
            price = "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item


    def parse_generations(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to generations.com.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css(".product_title.entry-title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css(".price .woocommerce-Price-amount.amount bdi::text").get()
        
        if price_element:
            price = price_element.strip()
        else:
            price = "Price Not Found"
        
        item['price'] = price
        
        item['link'] = response.url
        
        yield item
           
    def parse_playstation(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to direct.playstation.com
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css(".sony-text-h1::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_currency = sel.css(".price-currency.js-actual-price-symbol::text").get()
        price_whole = sel.css(".product-price.js-actual-price-whole::text").get()
        price_fraction = sel.css(".product-price-sup.price-change.js-actual-price-fraction::text").get()
        
        if price_whole:
            price = f"{price_currency}{price_whole}"
            if price_fraction:
                price += f".{price_fraction}"
        else:
            price = "Price Not Found"
        
        item['price'] = price.strip()
        
        item['link'] = response.url
        
        yield item

    def parse_grocerapp(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to grocerapp.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css(".MuiTypography-h1::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css(".MuiTypography-body1::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        item['price'] = price.replace('Rs. ', '').strip()  # Remove 'Rs.' and leading/trailing spaces
        
        item['link'] = response.url
        
        yield item

    def parse_myvitaminstore(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to myvitaminstore.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css(".t4s-product__title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css(".t4s-product-price::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        item['price'] = price.replace('PKR ', '').strip()  # Remove 'PKR' and leading/trailing spaces
        
        item['link'] = response.url
        
        yield item

    def parse_priceoye(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to priceoye.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css(".product-title h3::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css(".summary-price-label + .summary-price::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        item['price'] = price.replace('Rs ', '').strip()  # Remove 'Rs' and leading/trailing spaces
        
        item['link'] = response.url
        
        yield item
          
    def parse_dakaan(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        
        # Extract data specific to dakaan.pk
        item = ScrapedDataItem()
        
        # Extract title
        title = sel.css("#pro-title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        
        # Extract price
        price_element = sel.css(".text-danger span::text").get()
        price = price_element.strip() if price_element else "Price Not Found"
        item['price'] = price.replace('Rs. ', '')  # Remove 'Rs. ' from the price
        
        item['link'] = response.url
        
        yield item


    def parse_minemart(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".product-title::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.enj-product-price.engoj_price_main::text').get()
        if price:
            item['price'] = f"{price.strip()}"
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_daling(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".product__title h1::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.price-item--sale::text').get()
        if price:
            item['price'] = f"{price.strip()}"
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_jerrysmart(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".product-single__title::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.product__price.on-sale::text').get()
        if price:
            item['price'] = f"{price.strip()}"
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item


    def parse_onlymart(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".product_title.entry-title::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.price ins .woocommerce-Price-amount.amount bdi::text').get()
        if price:
            item['price'] = f"₨ {price.strip()}"
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_shopyard(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".product__title h1::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.price-item--sale.price-item--last::text').get()
        if price:
            item['price'] = price.strip()
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item


    def parse_bose(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".product-name::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.sales .value::text').get()
        if price:
            item['price'] = price.strip()
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_vintagetrimmer(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".product_title.entry-title::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('h4.elementor-heading-title.elementor-size-default::text').get()
        if price:
            item['price'] = price.strip()
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_discountstore(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".productView-title span::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.price__regular .price-item--regular::text').get()
        if price:
            item['price'] = f"{price.strip()}"
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_alhamdtech(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".product-detail__title.small-title::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.product-detail__price.product-price [data-product-price] .theme-money::text').get()
        if price:
            item['price'] = price.strip()
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_tejar(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css("h1.name::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.price-box span.price::text').get()
        if price:
            item['price'] = price.strip()
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_junaidtech(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css("#spnProductName::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('#spnCurrentPrice::text').get()
        if price:
            item['price'] = price.strip()
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item


    def parse_gtstore(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css("td > h1::text").get()
        item['title'] = title if title else "Title Not Found"
        price = sel.css('span.price21 strong::text').get()
        if price:
            item['price'] = price.strip()
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item
 
    def parse_logitechg(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".product-title.js-text-auto::text").get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = sel.css('.aem-content-ctn .aem-padding-options .price-atc-ctn.size-normal .pricing-info span::text').get()
        if price:
            item['price'] = f"{price.strip()}"
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_bestbuy(self, response):
        item = ScrapedDataItem()
        title = response.css('.sku-title a::text').get()
        item['title'] = title.strip() if title else "Title Not Found"
        price = response.css('.priceView-hero-price span::text').get()
        if price:
            item['price'] = f"${price.strip()}"
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_newegg(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to example1.com
        item = ScrapedDataItem()
        title = sel.css("div.product-wrap h1.product-title::text").get()
        if title is None:
            item['title'] = "Not Found"
        else:
            item['title'] = title
        price = sel.css('ul.price li.price-current strong::text').get()
        if price:
            item['price'] = "$" + price.strip()
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_aliexpress(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css(".title--wrap--Ms9Zv4A h1::text").get()
        if title is None:
            item['title'] = "Not Found"
        else:
            item['title'] = title
        price_parts = sel.css('.price--current--H7sGzqb .es--char53--VKKip5c::text').getall()
        if price_parts:
            formatted_price = ''.join(price_parts)
            item['price'] = f"PKR{formatted_price}"
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_cartco(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to example1.com
        item = ScrapedDataItem()
        title = sel.css("h1.page-title .base::text").get()
        if title is None:
            item['title'] = "Not Found"
        else:
            item['title'] = title
        price = sel.css("span#product-price-1098 .price::text").get()
        if price:
            item['price'] = price
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_ebay(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to example1.com
        item = ScrapedDataItem()
        title = sel.css(".x-item-title__mainTitle .ux-textspans.ux-textspans--BOLD::text").get()
        if title:
            item['title'] = title
        else:
            item['title'] = "Title Not Found"
        price = sel.css(".x-price-primary .ux-textspans::text").get()
        if price:
            item['price'] = price
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_amazon(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        item = ScrapedDataItem()
        title = sel.css("h1#title span.a-size-large.product-title-word-break::text").get()
        if title:
            item['title'] = title
        else:
            item['title'] = "Title Not Found"
        price_element = sel.css('.a-price .a-offscreen::text').get()
        if price_element:
            # Extracted price will be a string like "$99.99"
            item['price'] = price_element.strip()
        else:
            item['price'] = "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_daraz(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to daraz.pk
        item = ScrapedDataItem()
        title = sel.css("div.pdp-product-title span.pdp-mod-product-badge-title::text").get()
        if title:
            item['title'] = title
        else:
            item['title'] = "Title Not Found"
        price_element = sel.css('.pdp-mod-product-price span.pdp-price.pdp-price_type_normal.pdp-price_color_orange.pdp-price_size_xl::text').get()
        if price_element:
            item['price'] = price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item


    def parse_walmart(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to example1.com
        item = ScrapedDataItem()
        title = sel.css("h1#main-title::text").get()
        item['title'] = title if title else "Title Not Found"
        price = sel.css("span[itemprop='price']::text").get()
        item['price'] = price if price else "Price Not Found"
        item['link'] = response.url
        yield item

    def parse_bestbuyca(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to example1.com
        item = ScrapedDataItem()
        title = sel.css(".productSummaryContainer_kbflw h1.productName_2KoPa::text").get()
        item['title'] = title if title else "Title not found"
        price = sel.css("span.product-price .price_2j8lL.large_3uSI_::text").get()
        item['price'] = price if price else "Price not found"
        item['link'] = response.url
        yield item

    def parse_target(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to example1.com
        item = ScrapedDataItem()
        title = sel.css('h1.styles__StyledHeading-sc-1xmf98v-0.jhKFiw::text').get()
        item['title'] = title if title else "Title not found"
        price = sel.css('span.styles__CurrentPriceFontSize-sc-1mh0sjm-1.bksmYC::text').get()
        item['price'] = price if price else "Price not found"
        item['link'] = response.url
        yield item

    def parse_zahcomputers(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to zahcomputers.pk
        item = ScrapedDataItem()
        title = sel.css("h1.product_title.entry-title.wd-entities-title::text").get()
        item['title'] = title if title else "Title not found"
        price_element = sel.css('.elementor-widget-container .price .woocommerce-Price-amount.amount bdi::text').get()
        if price_element:
            item['price'] = "₨ " + price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_globalcomputers(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to globalcomputers.pk
        item = ScrapedDataItem()
        title = sel.css("h1.product_title.entry-title::text").get()
        item['title'] = title if title else "Title not found"
        price_element = sel.css('.price .woocommerce-Price-amount.amount bdi::text').get()
        if price_element:
            price = price_element.strip().replace(',', '')  # Remove commas from price
            item['price'] = "₨ " + price
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_czone(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to czone.com.pk
        item = ScrapedDataItem()
        title = sel.css("h1.product-productname::text").get()
        item['title'] = title.strip() if title else "Title not found"
        price_element = sel.css('.product-price #UpdatePanel2 .price-sales::text').get()
        if price_element:
            item['price'] = price_element.strip()
        else:
            item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_elitegamingstore(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to elitegamingstore.pk
        item = ScrapedDataItem()
        title = sel.css("h1.product_title.entry-title a::text").get()
        item['title'] = title if title else "Title not found"
        price_element = sel.css('.price span.woocommerce-Price-amount.amount bdi::text').get()
        if price_element:
            item['price'] = "₨ " + price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        yield item

    def parse_logiguru(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to logiguru.pk
        item = ScrapedDataItem()
        title_element = sel.css("h1.product_title.entry-title.wd-entities-title::text").get()
        if title_element:
            item['title'] = title_element
        else: 
            item['title'] = "not found"
        price_element = sel.css('.price span.woocommerce-Price-amount.amount bdi::text').get()
        if price_element:
            item['price'] = "₨ " + price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_olx(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to OLX
        item = ScrapedDataItem()
        title = sel.css("h1.a38b8112::text").get()
        item['title'] = title if title else "Title not found"
        price_element = sel.css('div._1075545d.d059c029._858a64cf span._56dab877::text').get()
        if price_element:
            item['price'] = price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_technoo(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to Technoo.pk
        item = ScrapedDataItem()
        title = sel.css("h1.product-meta__title.heading.h1::text").get()
        item['title'] = title if title else "Title not found"
        price_element = sel.css('div.price-list span.price::text').get()
        if price_element:
            item['price'] = price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_carrefour(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to Carrefour.pk
        item = ScrapedDataItem()
        title = sel.css("h1.css-106scfp::text").get()
        item['title'] = title if title else "Title not found"
        price_element = sel.css('h2.css-17ctnp::text').get()
        if price_element:
            item['price'] = price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_qne(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to QnE
        item = ScrapedDataItem()
        title_element = sel.css("h1.product-meta__title.heading.h1::text").get()
        if title_element:
            item['title'] = title_element.strip()
        price_element = sel.css('span.price.price--highlight::text').get()
        if price_element:
            item['price'] = price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_greenvalley(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to greenvalley.pk
        item = ScrapedDataItem()
        title = sel.css("h1.product_title.entry-title::text").get()
        item['title'] = title if title else "Title not found"
        price_element = sel.css('.price span.woocommerce-Price-amount.amount bdi::text').get()
        if price_element:
            item['price'] = "₨" + price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_abmmart(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to abmmart.pk
        item = ScrapedDataItem()
        title = sel.css("h1.product_title.entry-title.wd-entities-title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        price_element = sel.css('.price span.woocommerce-Price-amount.amount bdi::text').get()
        if price_element:
            item['price'] = "₨" + price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_heygirl(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to heygirl.pk
        item = ScrapedDataItem()
        title = sel.css("div.product__title h1::text").get()
        item['title'] = title.strip() if title else "Title not found"
        price_element = sel.css('.price__regular .price-item--sale::text').get()
        if price_element:
            item['price'] = price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_hnbstore(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to hnbstore.pk
        item = ScrapedDataItem()
        title = sel.css("h1.product-title span::text").get()
        item['title'] = title.strip() if title else "Title not found"
        price_element = sel.css('.prices span.price.on-sale::text').get()
        if price_element:
            item['price'] = "Rs. " + price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_tagofashion(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to tagofashion.com.pk
        item = ScrapedDataItem()
        title = sel.css("h1.productView-title.element-spacing::text").get()
        item['title'] = title.strip() if title else "Title not found"
        price_element = sel.css('.price__sale .price-item--sale::text').get()
        if price_element:
            item['price'] = price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_shopatshams(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to shopatshams.com.pk
        item = ScrapedDataItem()
        title = sel.css("h1.h2.product-single__title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        price_element = sel.css('.product-single__form-price span.product__price span::text').get()
        if price_element:
            item['price'] = "Rs. " + price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_highstreetpakistan(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to highstreetpakistan.com
        item = ScrapedDataItem()
        title = sel.css("h1.m-product-title::text").get()
        item['title'] = title.strip() if title else "Title not found"
        price_element = sel.css('.m-price__regular .m-price-item--regular::text').get().strip()
        if price_element:
            item['price'] = price_element
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def parse_hudabeauty(self, response):
        self.driver.get(response.url)
        sel = Selector(text=self.driver.page_source)
        # Extract data specific to hudabeauty.com
        item = ScrapedDataItem()
        title = sel.css("h1.product-name.order-md-1.order-3::text").get()
        item['title'] = title.strip() if title else "Title not found"
        price_element = sel.css('.prices .sales span.value::text').get()
        if price_element:
            item['price'] = "$" + price_element.strip()
        else:
             item['price'] = "Price Not Found" 
        item['link'] = response.url
        yield item

    def closed(self, reason):
        self.driver.quit()




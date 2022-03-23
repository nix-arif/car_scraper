import scrapy
from scrapy_splash import SplashRequest


class LithiaSpider(scrapy.Spider):
    name = "lithia"
    allowed_domains = ["lithia.com"]
    start_urls = ["https://www.lithia.com/new-inventory/index.htm"]

    def start_requests(self):
        filters_script = """
            function main(splash)
                assert(splash:go(splash.args.url))
                splash:wait(5)

                local get_element_dim_by_xpath = splash:jsfunction([[
                    function(xpath) {
                        var element = document.evaluate(xpath, document, null,
                            XPathResult.FIRST_ORDERES_NODE_TYPE, null).singleNodeValue;
                        var element_rect = element.getClientRects()[0];
                        return {"x": element_rect.left, "y": element_rect.top}
                    }
                ]])

                -- -- Find the YEAR drop down
                local year_drop_dimensions = get_element_dim_by_xpath(
                    -- '//h2[contains(@class, "label ") and contains(text(), "Year ")]'
                    '//div[contains(@id, "year--heading") and contains(@class, "justify-content-between") and contains(@id, "ae_facet_list_group_desc1")]'
                )
                splash:set_viewport_full()
                splash:mouse_click(year_drop_dimensions.x, year_drop_dimensions.y)
                splash:wait(1.5)

                -- -- Clicks the 202X year
                local year_dimensions = get_element_dim_by_xpath(
                    -- '//li[contains(@data-value, "2020")]/span'
                    '//input[contains(@id, "year-min")]'
                )
                splash:set_viewport_full()
                splash:mouse_click(year_dimensions.x, year_dimensions.y)
                splash:wait(5)

                -- Find the MAKE drop down
                local make_drop_dimensions = get_element_by_xpath(
                    '//h2[contains(@class, "label ") and contains(text(), "Make ")]'
                )
                splash:set_viewport_full()
                splash:mouse_click(make_drop_dimensions.x, make_drop_dimensions.y)
                splash:wait(1.5)

                -- Clicks the Toyota make
                local make_dimensions = get_element_by_xpath(
                    '//li[contains(@data-filters, "make-toyota")]/span'
                )
                splash:set_viewport_full()
                splash.mouse_click(make_dimensions.x, make_dimensions.y)
                splash:wait(5)
            """

    def parse(self, response):
        pass

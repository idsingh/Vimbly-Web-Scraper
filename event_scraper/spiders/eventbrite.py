from scrapy.spiders import Spider
from scrapy.selector import Selector

from event_scraper.items import EventScraperItem

def extractFirst(selector) :
    list = selector.extract();
    if len(list)>0 :
        return list[0];
    else :
        return "";
class EventbriteSpider(Spider):
    name = "vimbly"
    allowed_domains = ["vimbly.com"]
    start_urls = [
        #"https://www.vimbly.com/"
        "https://www.vimbly.com/nyc-watch-activities-%s" % page for page in xrange(1,100)] + \
        ["https://www.vimbly.com/nyc-featured-things-to-do-%s" % page for page in xrange(1,100)] + \
        ["https://www.vimbly.com/nyc-learn-activities-%s" % page for page in xrange(1,100)] + \
        ["https://www.vimbly.com/nyc-explore-activities-%s" % page for page in xrange(1,100)] + \
        ["https://www.vimbly.com/nyc-eat-activities-%s" % page for page in xrange(1,100)] + \
        ["https://www.vimbly.com/nyc-drink-activities-%s" % page for page in xrange(1,100)] + \
        ["https://www.vimbly.com/nyc-date-ideas-%s" % page for page in xrange(1,100)] + \
        ["https://www.vimbly.com/nyc-fighting-classes-%s" % page for page in xrange(1,100)]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*')
        items = []
        namesDict = {};
        for block in response.css('li.clearfix'):
            item = EventScraperItem();
            item['name'] = extractFirst(block.css('div.regularContent h2 a::text')).strip();
            item['description'] = extractFirst(block.css('div.regularContent div.description::text')).strip();
            item['date'] = extractFirst(block.css('div.regularContent div.moreInfo div a.firstTime::text')).strip();
            item['price'] = extractFirst(block.css('div.regularContent div.moreInfo  a.price span.currentPrice::text')).strip();
            item['venue'] = extractFirst(block.css('div.quickviewContent p.location::text')).strip();
            item['otherTimes'] = [];
            moreTimesGrid = block.css('div.moreTimesGrid ul')
            for time in moreTimesGrid:
                dateTimeString = extractFirst(time.css('a.clearfix span.date::text')).strip();
                dateTimeString = dateTimeString + ' ' + extractFirst(time.css('a.clearfix span.time::text')).strip();
                item['otherTimes'].append(dateTimeString)
            if item['name'] :
                items.append(item);
        return items

import scrapy

from .. import items


class VGMSpider(scrapy.Spider):
    name = "vgm"
    allowed_domains = ["vgmdb.net"]
    start_urls = [
        "http://vgmdb.net/album/52428",
        "http://vgmdb.net/album/30974",
        "http://vgmdb.net/album/46276",
        "http://vgmdb.net/album/50090"
    ]

    def parse(self, response):
        item = items.AlbumItem()
        item['name'] = response.css('h1 span[lang=en].albumtitle::text').extract()
        item['artist'] = response.css('#album_infobit_large span[lang=en].productname::text').extract()
        item['date'] = response.css('#album_infobit_large a[title^="View albums"]::text').extract()
        tracks = list()
        for track in response.css('div#tracklist span:first-child tr'):
            trackNum = track.css('td')[0].css('span::text').extract()
            trackName = track.css('td')[1].css('::text').extract()
            tracks.append({'num': trackNum, 'name': trackName})

        item['tracks'] = tracks

        yield item

# Follow along with Travery Media

import scrapy

class PostsSpider(scrapy.Spider):
  name = "Posts"

  source = 'https://mahj00n.wordpress.com/'
  
  def parse(self, response):
    for post in response.css('article.post').getall():
      yield {
      'title': post.css('.entry-header h2 a::text').get(),
      'date': post.css('.entry-header time::text').get()
      }
#    older_posts = response.css('a.')
# Here the problem is that my Blog uses infinite-view which seems to be
# a jquery event as opposed to an actual link
    
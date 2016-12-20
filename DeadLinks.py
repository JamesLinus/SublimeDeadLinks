import sublime
import sublime_plugin

# http://www.baidu.com
class CheckDeadLinksCommand(sublime_plugin.TextCommand):
    url_pattern = "\\bhttps?://[-A-Za-z0-9+&@#/%?=~_()|!:,.;']*[-A-Za-z0-9+&@#/%=~_(|]"

    def run(self, edit):
        self.find_urls()
        for url in self.urls:
            print(url)

    def find_urls(self):
        self.urls = []

        regions = self.view.find_all(self.url_pattern)
        for region in regions:
            self.urls.append({'region': region, 'url': self.view.substr(region) })

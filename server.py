from __future__ import unicode_literals

import asyncio

from ably import AblyRest
import web

from local_os import ABLY_API_KEY

# locally change to your ably API KAY
apiKey = ABLY_API_KEY
client = AblyRest(apiKey)

render = web.template.render('templates/')


class index:
    def GET(self):
        return render.index(apiKey)


class publish:
    def GET(self):
        return render.publish()

    def POST(self):
        message = web.input().get('message')
        if message is not None:
            channel = client.channels.get('sport')
            asyncio.run(channel.publish('update', message))
        raise web.seeother('/publish')


urls = (
    '/', index,
    '/publish', publish
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

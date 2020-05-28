from channels.routing import ProtocolTypeRouter, URLRouter
import group_control.routing
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
            group_control.routing.websocket_urlpatterns
        )
})
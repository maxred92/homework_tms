from app.forum import views
# настраиваем пути, которые будут вести к нашей странице
def setup_routes(app):
    app.router.add_get("/", views.index)
    app.router.add_view("/api/messages_list", views.ListMessage)
    app.router.add_view("/api/messages_add", views.AddMessage)
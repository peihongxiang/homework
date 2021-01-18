from po.page.Index_page import IndexPage


class TextIndex:
    def setup_class(self):
        #实例方法可以在别的方法中使用
        self.indexpage = IndexPage()
    def test_login(self):
        #1.跳转到登录页 2.执行登录
        self.indexpage.goto_login().login()
    def test_register(self):
        # 1.跳转到注册页 2.执行注册
        self.indexpage.goto_register().register()


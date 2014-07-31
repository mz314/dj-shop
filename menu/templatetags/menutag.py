from menu.models import Menu, MenuItem
from django import template


class MenuNode(template.Node):
    def __init__(self,menu_tag):
        self.menu_tag=menu_tag.replace('"',"")




    def render(self, context):
         try:
            menu=Menu.objects.get(tag=self.menu_tag)
         except Menu.DoesNotExist:
             raise template.TemplateSyntaxError("%s menu doesn't exist." % (self.menu_tag,))

         items=MenuItem.objects.filter(menu=menu).order_by('ordering')
         for i in items:
             if i.type=='slash':
                 i.href='/'+i.link
             elif i.type=='external':
                 i.href=i.link
             else:
                 i.href='#/'+i.link

         t = template.loader.get_template('menu.html')
         return t.render(template.Context({'menu':menu,'items':items}))

def menu_tag_proc(parser,token):
    try:
        tag_name,menu_tag=token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    return MenuNode(menu_tag)

register=template.Library()
register.tag('menutag', menu_tag_proc)
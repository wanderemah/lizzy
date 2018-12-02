from django.contrib import admin
from church.models import Event, signUp, Service, Grouped, chosenGroup, serviceTool, attendanceList, Video, Comment, \
    Responses, Audio, Document, Image, Staff, eventImage, Member, Tool, Pledge, Message, New, newsImages


# Register your models here.
class Stepline1(admin.StackedInline):
    model = chosenGroup


class UserInline1(admin.ModelAdmin):
    inlines = [Stepline1, ]


class Stepline2(admin.StackedInline):
    model = attendanceList


class Stepline6(admin.StackedInline):
    model = eventImage


class UserInline2(admin.ModelAdmin):
    inlines = [Stepline2, Stepline6, ]


class Stepline3(admin.StackedInline):
    model = serviceTool


class UserInline3(admin.ModelAdmin):
    inlines = [Stepline3, ]


class Stepline4(admin.StackedInline):
    model = Responses


class UserInline4(admin.ModelAdmin):
    inlines = [Stepline4, ]


class Stepline5(admin.StackedInline):
    model = Image


class Stepline7(admin.StackedInline):
    model = Member


class Stepline8(admin.StackedInline):
    model = Tool


class Stepline9(admin.StackedInline):
    model = Pledge


class UserInline5(admin.ModelAdmin):
    inlines = [Stepline5, Stepline7, Stepline8, Stepline9, ]


class Stepline10(admin.StackedInline):
    model = newsImages


class UserInline7(admin.ModelAdmin):
    inlines = [Stepline10, ]


admin.site.register(Event, UserInline2)
admin.site.register(signUp, UserInline1)
admin.site.register(Comment, UserInline4)
admin.site.register(Grouped, UserInline5)
admin.site.register(Video)
admin.site.register(New,UserInline7)
admin.site.register(Message)
admin.site.register(Audio)
admin.site.register(Staff)
admin.site.register(Document)
admin.site.register(Service, UserInline3)

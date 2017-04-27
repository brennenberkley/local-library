from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BooksInline(admin.TabularInline):
    model = Book
    extra = 0
    exclude = ['summary']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    ordering = ['title']
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)

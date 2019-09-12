from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from polls.models import Question
from cms.utils.urlutils import admin_reverse


class PollToolbar(CMSToolbar):

    # def populate(self):
    #     menu = self.toolbar.get_or_create_menu('polls_cms_integration-polls', 'Polls')

    #     menu.add_sideframe_item(
    #         name='Poll list',                              # name of the new menu item
    #         url=admin_reverse('polls_question_changelist'),    # the URL it should open with
    #     )

    #     menu.add_modal_item(
    #         name='Add a new poll',                # name of the new menu item
    #         url=admin_reverse('polls_question_add'),  # the URL it should open with
    #     )

    def populate(self):

        buttonlist = self.toolbar.add_button_list()

        buttonlist.add_sideframe_button(
            name='Poll list',
            url=admin_reverse('polls_question_changelist'),
        )

        buttonlist.add_modal_button(
            name='Add a new poll',
            url=admin_reverse('polls_question_add'),
        )


# register the toolbar
toolbar_pool.register(PollToolbar)


# from cms.utils.urlutils import admin_reverse
# from cms.toolbar_base import CMSToolbar
# from cms.toolbar_pool import toolbar_pool
# from polls.models import Question


# class PollToolbar(CMSToolbar):
#     supported_apps = ['polls']

#     def populate(self):

#         if not self.is_current_app:
#             return

#         menu = self.toolbar.get_or_create_menu('polls_cms_integration-polls', 'Polls')

#         menu.add_sideframe_item(
#             name='Poll list',
#             url=admin_reverse('polls_question_changelist'),
#         )

#         menu.add_modal_item(
#             name=('Add a new poll'),
#             url=admin_reverse('polls_question_add'),
#         )

#         buttonlist = self.toolbar.add_button_list()

#         buttonlist.add_sideframe_button(
#             name='Poll list',
#             url=admin_reverse('polls_question_changelist'),
#         )

#         buttonlist.add_modal_button(
#             name='Add a new poll',
#             url=admin_reverse('polls_question_add'),
#         )


# toolbar_pool.register(PollToolbar)

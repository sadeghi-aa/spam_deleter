# Spam Deleter Telegram Bot
A Telegram bot that deletes spam messages upon request of an adminstrator.

This code uses telebot library and is based on flask. This is how the bot works (for you as a group admin):



1- Add the bot to the group. It has to be a supergroup, i.e. previous messages should be visible to new members.

2- Make it an admin (at least with 'Delete messages' permission).

3- Reply to a member's message with /del command.

4- Their message and your command will be deleted by the bot.

5- A warning message mentioning the spammer will be sent to the group. (You can replace the warning text with your preferred message)



Note 1: If a non-admin user replies /del to a message, their message will be deleted and ignored.

Note 2: If an admin tries to delete another admin's message, it will be considered a mistake and will be ignored.

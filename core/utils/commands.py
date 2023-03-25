from aiogram import Bot
from aiogram import types
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(
            command='start',
            description='Начало работы'
        ),
        types.BotCommand(
            command='help',
            description='Помощь'
        ),
        types.BotCommand(
            command='cancel',
            description='Сбросить'
        ),
        types.BotCommand(
            command='inline',
            description='Показать инлайн клавиатуру'
        ),
        types.BotCommand(
            command='pay',
            description='Купить продукт'
        ),
        types.BotCommand(
            command='form',
            description='Начать опрос'
        ),
        types.BotCommand(
            command='audio',
            description='Прислать аудио'
        ),
        types.BotCommand(
            command='document',
            description='Прислать документ'
        ),
        types.BotCommand(
            command='mediagroup',
            description='Прислать медиагруппу'
        ),
        BotCommand(
            command='photo',
            description='Прислать фото'
        ),
        BotCommand(
            command='sticker',
            description='Прислать стикер'
        ),
        BotCommand(
            command='video',
            description='Прислать видео'
        ),
        BotCommand(
            command='video_note',
            description='Прислать видеосообщение'
        ),
        BotCommand(
            command='voice',
            description='Прислать голосовое сообщение'
        )
    ]

    commands1 = [
        types.BotCommand(
            command='HALT',
            description='все'
        )
    ]

    await bot.set_my_commands([
        BotCommand( 'HALT', 'ХАРЕ'),BotCommandScopeDefault
    ])


async def set_default_commands(bot):
    commands1 = [
        BotCommand(
            command='HALT',
            description='все'
        )
    ]
    commands2 = [
        BotCommand(
            command='start',
            description='NET'
        ),

        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='cancel',
            description='Сбросить'
        )
        # BotCommand(
        #     command='inline',
        #     description='Показать инлайн клавиатуру'
        # ),
        # BotCommand(
        #     command='pay',
        #     description='Купить продукт'
        # ),
        # BotCommand(
        #     command='form',
        #     description='Начать опрос'
        # ),
        # BotCommand(
        #     command='audio',
        #     description='Прислать аудио'
        # ),
        # BotCommand(
        #     command='document',
        #     description='Прислать документ'
        # ),
        # BotCommand(
        #     command='mediagroup',
        #     description='Прислать медиагруппу'
        # ),
        # BotCommand(
        #     command='photo',
        #     description='Прислать фото'
        # ),
        # BotCommand(
        #     command='sticker',
        #     description='Прислать стикер'
        # ),
        # BotCommand(
        #     command='video',
        #     description='Прислать видео'
        # ),
        # BotCommand(
        #     command='video_note',
        #     description='Прислать видеосообщение'
        # ),
        # BotCommand(
        #     command='voice',
        #     description='Прислать голосовое сообщение'
        # )
    ]

    await bot.set_my_commands(commands=commands2)
    # scope=BotCommandScopeDefault )
    #     types.BotCommand("start", "Запустить бота"),
    #     types.BotCommand("help", "Помощь"),
    #     types.BotCommand("test", "Тест"),
    #     types.BotCommand("form", "Форма"),
    #     types.BotCommand("menu", "Меню"),
    # ]

# =============================================================================
#  УРОКИ КУРСА — Финансовая грамотность
# =============================================================================

MODULES = {
    1: {"title": "Модуль 1 — Основы финансового мышления"},
    2: {"title": "Модуль 2 — Планирование и бюджет"},
    3: {"title": "Модуль 3 — Накопления и подушка безопасности"},
}

MODULE_BREAK_MESSAGE = {
    1: (
        "✅ <b>Модуль 1 завершён!</b>\n\n"
        "Отличная работа! Рекомендую сделать перерыв — дайте информации усвоиться.\n"
        "Модуль 2 уже открыт и ждёт вас 💪\n\n"
        "Нажмите «Уроки» когда будете готовы продолжить."
    ),
    2: (
        "✅ <b>Модуль 2 завершён!</b>\n\n"
        "Вы освоили планирование и бюджет — это фундамент финансовой грамотности!\n"
        "Рекомендую сделать перерыв перед финальным модулем.\n"
        "Модуль 3 уже открыт 🚀\n\n"
        "Нажмите «Уроки» когда будете готовы."
    ),
}

LESSONS = [
    # ── МОДУЛЬ 1 ──────────────────────────────────────────────────────────────
    {
        "id": 1, "module": 1,
        "title": "Урок 1 — Познакомимся для начала",
        "cover": "AgACAgIAAxkBAAM8abO2P3r_1vWaptE_N4ECuzxb1ogAAjEWaxt9DplJuJLIH4zdoIUBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/cV9A4jSLN-Q",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Первый урок курса. Давайте познакомимся!",
        "hw_type": "text",
        "hw_text": "✏️ <b>Задание:</b>\n\nРасскажи о себе. У тебя есть максимум <b>100 слов</b> — это лимит, за который нельзя выходить. Меньше можно, больше нельзя.",
        "apps_text": None,
    },
    {
        "id": 2, "module": 1,
        "title": "Урок 2 — Зачем основы, давай мясо",
        "cover": "AgACAgIAAxkBAAM-abO2YaXh-2CmkkQ20kgBd52j7lMAAjIWaxt9DplJHzd1FWN6x4YBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/7UbObNDeXrA",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Почему без основ не работает ничто — даже самые крутые лайфхаки.",
        "hw_type": None, "hw_text": None, "apps_text": None,
    },
    {
        "id": 3, "module": 1,
        "title": "Урок 3 — Стабильность или свобода",
        "cover": "AgACAgIAAxkBAAM_abO2Yj1_NXAgjcoIVv17tTZp9JwAAjMWaxt9DplJNUuIyGQ17o4BAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/FZWCJPKKfBw",
        "extra_video_url": "https://youtu.be/J4GTyiyZxts",
        "extra_video_label": "Совет",
        "text": "Что важнее — стабильность или финансовая свобода? Разбираемся вместе.",
        "hw_type": "text",
        "hw_text": "✏️ <b>Задание:</b>\n\nЧто бы вы делали, если бы вам не нужно было работать? Вам бы платили просто за то, что вы хороший человек — или плохой, без разницы.",
        "apps_text": None,
    },
    {
        "id": 4, "module": 1,
        "title": "Урок 4 — Правильное отношение к деньгам",
        "cover": "AgACAgIAAxkBAANBabO2YpAGS_STdl7OpeEHRljwAAG1AAI0FmsbfQ6ZSRWZ25DtiqvUAQADAgADeQADOgQ",
        "video_url": "https://youtu.be/jnb7ErsaZOI",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Как мы думаем о деньгах — именно это определяет, сколько их у нас будет.",
        "hw_type": "text",
        "hw_text": "✏️ <b>Задание:</b>\n\nПредставь, что ты <b>никогда</b> не сможешь зарабатывать больше, чем сегодня, или никогда не сможешь зарабатывать больше, чем средняя зарплата по стране — 300–400$/мес.\n\nОпиши свои эмоции и действия.",
        "apps_text": None,
    },
    {
        "id": 5, "module": 1,
        "title": "Урок 5 — Пять шагов",
        "cover": "AgACAgIAAxkBAANQabO2jft2FcQgLAYx_rZ-rOateZMAAjUWaxt9DplJ9zuzUqB43hkBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/LpUvCMW7SS0",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Пять конкретных шагов, с которых начинается путь к финансовой грамотности.",
        "hw_type": "info",
        "hw_text": "📌 <b>Задание:</b>\n\nПрочитать книгу <b>«Пёс по имени Мани»</b> и начать вести учёт расходов по одной статье бюджета.",
        "apps_text": None,
    },
    {
        "id": 6, "module": 1,
        "title": "Урок 6 — Тебе это всё точно нужно",
        "cover": "AgACAgIAAxkBAANSabO2kG_izzYmkAeRkw1dmx-Z3nQAAjcWaxt9DplJEmZGXiwIWVkBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/TayFHDthJ2U",
        "extra_video_url": "https://youtu.be/hnWCx0gtHMw",
        "extra_video_label": "Совет",
        "text": "Финальный урок модуля. Почему всё, что мы разобрали — это не теория, а необходимость.",
        "hw_type": None, "hw_text": None, "apps_text": None,
    },
    # ── МОДУЛЬ 2 ──────────────────────────────────────────────────────────────
    {
        "id": 7, "module": 2,
        "title": "Урок 1 — Успех равно планирование",
        "cover": "AgACAgIAAxkBAANUabO6xjAvzvBYJaebPZ6RId0qOxkAAmQWaxt9DplJHrz0f8-Jk5IBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/48u659l9l30",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Почему люди, которые планируют, достигают целей, а остальные — нет.",
        "hw_type": "info",
        "hw_text": "📌 <b>Задание:</b>\n\nЗавести <b>дневник успеха!</b> Можете бросить его в конце курса, но сейчас — нужно завести.",
        "apps_text": None,
    },
    {
        "id": 8, "module": 2,
        "title": "Урок 2 — S.M.A.R.T. значит умный",
        "cover": "AgACAgIAAxkBAANWabO6ykV2xnKxBROko6eopN0-yJYAAmUWaxt9DplJh9etneNIbn0BAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/I3GbEHXLnGw",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Система постановки целей, которую используют успешные люди по всему миру.",
        "hw_type": "text",
        "hw_text": "✏️ <b>Задание:</b>\n\nРасписать любую свою цель по системе S.M.A.R.T.\n\n<b>Дополнительно:</b> расписать цель «Стать финансово независимым» тоже по S.M.A.R.T.",
        "apps_text": None,
    },
    {
        "id": 9, "module": 2,
        "title": "Урок 3 — Учёт доходов и расходов",
        "cover": "AgACAgIAAxkBAANYabO6zl3Os1lgJwZBpszqu4Pm6fkAAmYWaxt9DplJRytqZIXqBA0BAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/XrGYpTC6aAo",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Без учёта невозможно управлять финансами. Разбираем как это делать правильно.",
        "hw_type": "text",
        "hw_text": "✏️ <b>Задание:</b>\n\nСоставить финансовый план и установить приложение для учёта финансов.",
        "apps_text": None,
    },
    {
        "id": 10, "module": 2,
        "title": "Урок 4 — Распределение финансов",
        "cover": "AgACAgIAAxkBAANaabO60T6U9Qv1Vf2CIynrSPvNAjsAAmkWaxt9DplJ0OP89gzPOngBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/vQaudNLQHVY",
        "extra_video_url": "https://youtu.be/Htf9EqhwVTI",
        "extra_video_label": "🎯 Всем ИПшникам, таксистам и ретейлерам посвящается",
        "text": "Как правильно распределять деньги, чтобы хватало на всё важное.",
        "hw_type": None, "hw_text": None, "apps_text": None,
    },
    {
        "id": 11, "module": 2,
        "title": "Урок 5 — Приоритетность в структуре плана",
        "cover": "AgACAgIAAxkBAANcabO61E46DhNCoHHW2Nr695kkU78AAmoWaxt9DplJbSrhlk0fm4YBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/DZrjEa1pJUQ",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Что платить в первую очередь, а что — потом. Система приоритетов.",
        "hw_type": "info",
        "hw_text": "📌 <b>Задание (необязательно, но рекомендую):</b>\n\nПопробуйте на себе, как работают конверты.",
        "apps_text": None,
    },
    {
        "id": 12, "module": 2,
        "title": "Урок 6 — Как избавиться от долгов",
        "cover": "AgACAgIAAxkBAANeabO62MQEs_tiuXGuMQlWFl7qMrgAAmsWaxt9DplJfPUOy1bPYsoBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/LUTrRRc49i4",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Конкретный план выхода из долговой ямы — шаг за шагом.",
        "hw_type": "text",
        "hw_text": "✏️ <b>Задание:</b>\n\nСколько раз пришлось пересмотреть это видео, чтобы разобраться? 😄\nНапиши свой ответ.",
        "apps_text": None,
    },
    {
        "id": 13, "module": 2,
        "title": "Урок 7 — Зачем нужно финансовое планирование",
        "cover": "AgACAgIAAxkBAANgabO63IKEYu_RfB7JfetLxVQzPBUAAmwWaxt9DplJOigIJBBiaOIBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/dvWZw5xz9Xg",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Финансовый план — это не скучная таблица, это карта к вашим целям.",
        "hw_type": "text",
        "hw_text": "✏️ <b>Задание:</b>\n\nДорабатывайте свой финансовый план, выстройте приоритетность.\nИ прочитайте книгу <b>«Самый богатый человек в Вавилоне»</b>.\n\n🎮 <b>Игра Time Flow:</b> [ссылка появится здесь]",
        "apps_text": None,
    },
    {
        "id": 14, "module": 2,
        "title": "Урок 8 — Программы для учёта",
        "cover": "AgACAgIAAxkBAANiabO64DUDTpSO3M6u5c_PEo0PVuYAAnAWaxt9DplJcziUcyrni0gBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/f_W1gX2cpDI",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Обзор лучших приложений для учёта финансов — выбирайте то, с которым удобно работать.",
        "hw_type": None, "hw_text": None,
        "apps_text": (
            "📱 <b>ПРИЛОЖЕНИЯ ДЛЯ УЧЁТА ФИНАНСОВ 💵</b>\n\n"
            "<b>Money OK</b>\n"
            "🍏 <a href='https://apps.apple.com/kz/app/money-ok-personal-finance/id606031670'>iOS</a> | "
            "🤖 <a href='https://play.google.com/store/apps/details?id=biz.mobion.moneyokan'>Android</a>\n\n"
            "<b>Monefy</b>\n"
            "🍎 <a href='https://apps.apple.com/kz/app/monefy-money-tracker/id1212024409'>iOS</a> | "
            "🤖 <a href='https://play.google.com/store/apps/details?id=com.monefy.app.lite'>Android</a>\n\n"
            "<b>Money Lover</b>\n"
            "🧃 <a href='https://apps.apple.com/kz/app/money-lover-expense-tracker/id486312413'>iOS</a> | "
            "🤖 <a href='https://play.google.com/store/apps/details?id=com.bookmark.money'>Android</a>\n\n"
            "<b>CoinKeeper</b>\n"
            "🍸 <a href='https://apps.apple.com/kz/app/coinkeeper-budget-planner/id849747345'>iOS</a> | "
            "🤖 <a href='https://play.google.com/store/apps/details?id=com.disrapp.coinkeeper.material'>Android</a>\n\n"
            "<i>P.S. Лучше скачать несколько, чтобы выбрать то, с которым будет приятно работать!</i>"
        ),
    },
    # ── МОДУЛЬ 3 ──────────────────────────────────────────────────────────────
    {
        "id": 15, "module": 3,
        "title": "Урок 1 — Богатый, бедный и так-пойдётный",
        "cover": "AgACAgIAAxkBAANmabO7f3XoeZ-BEeAzfe9-0cNwAokAAngWaxt9DplJerfEq5fwW0IBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/3g2OaammptE",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Три типа финансового мышления. Какой из них ваш?",
        "hw_type": "info",
        "hw_text": "📌 <b>Задание:</b>\n\nПрочитать книгу <b>«Богатый папа, бедный папа»</b>.",
        "apps_text": None,
    },
    {
        "id": 16, "module": 3,
        "title": "Урок 2 — Накопления, да где их взять-то",
        "cover": "AgACAgIAAxkBAANoabO7glwDXhmrk9jnWdeFWsNeNdQAAnkWaxt9DplJlVLPQlvLFmgBAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/UYKu4omCdtU",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Главный вопрос тех, кто хочет начать копить. Отвечаем честно.",
        "hw_type": None, "hw_text": None, "apps_text": None,
    },
    {
        "id": 17, "module": 3,
        "title": "Урок 3 — Ааа, вот где",
        "cover": "AgACAgIAAxkBAANqabO7hYZt_H5f8Tt8sBMllatpzokAAnoWaxt9DplJfsXByxBbzS4BAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/yNj4fDugg8s",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Находим деньги там, где вы их не замечали.",
        "hw_type": "text",
        "hw_text": "✏️ <b>Задание:</b>\n\nСоставить план накопления.",
        "apps_text": None,
    },
    {
        "id": 18, "module": 3,
        "title": "Урок 4 — Подушка безопасности",
        "cover": "AgACAgIAAxkBAANsabO7iI4KZLHpY2gms5-hWg1JuO0AAnsWaxt9DplJgNLmv7fnK40BAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/KY8D8_j4ebs",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Почему финансовая подушка — это не роскошь, а необходимость.",
        "hw_type": None, "hw_text": None, "apps_text": None,
    },
    {
        "id": 19, "module": 3,
        "title": "Урок 5 — То, без чего не работает план",
        "cover": "AgACAgIAAxkBAANuabO7jBrSERH1k8CwBe0XZMDoyccAAnwWaxt9DplJgiRstz04w98BAAMCAAN5AAM6BA",
        "video_url": "https://youtu.be/sSAqrrWnhRE",
        "extra_video_url": None, "extra_video_label": None,
        "text": "Финальный урок курса. Один ключевой элемент, без которого всё остальное рассыпается.",
        "hw_type": None, "hw_text": None, "apps_text": None,
    },
]

TOTAL_LESSONS = len(LESSONS)  # 19

FINAL_COVER = "AgACAgIAAxkBAAOdabO-ScCOQM2bL5_cVlQBrQnwtXIAAp4Waxt9DplJaXQzzwoKF84BAAMCAAN5AAM6BA"

FINAL_MESSAGE = (
    "🎉 <b>Поздравляю!</b>\n\n"
    "Вы только что сделали то, что большинство людей откладывают годами.\n\n"
    "Вы прошли путь от «деньги просто утекают сквозь пальцы» до понимания, "
    "как работает бюджет, накопление — да и вообще прокачали своё финансовое мышление.\n\n"
    "Но знания сами по себе не меняют жизнь. Меняет — их <b>применение</b>. "
    "Самое интересное начинается тогда, когда эти принципы применяются в вашей вселенной: "
    "с вашим доходом, вашими привычками и вашими целями.\n\n"
    "Если вы хотите двигаться дальше — я готов помочь и приглашаю вас на <b>личную консультацию</b>.\n\n"
    "🎁 Для выпускников мини-курса действует специальное предложение: <b>скидка 50%</b>\n\n"
    "Записаться можно тут: @sergofinance\n\n"
    "Для тех кто ещё не подписан на мой канал, добро пожаловать — там много реальных историй "
    "и полезных материалов, не вошедших в этот курс 👉 "
    "<a href='https://t.me/channelsergofinance'>t.me/channelsergofinance</a>\n\n"
    "А для тех, кто ищет общения про деньги есть специальная группа, там можно задавать вопросы "
    "и отвечать другим участникам 👉 "
    "<a href='https://t.me/+3GzLNGh5IaRiZDIy'>присоединиться к группе</a>"
)
